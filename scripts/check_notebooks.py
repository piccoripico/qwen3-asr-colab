"""Static repository checks suitable for GitHub Actions."""
from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

from languages import (
    FORCED_ALIGNER_LANGUAGES,
    LANGUAGES,
    default_timestamp_mode,
    source_language_options,
)

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
EXPECTED_VERSION = "v1.0.0"
TEMPLATE_DIR = ROOT / "notebook_template"
GENERATED_DIR = ROOT / "notebooks"
LOCALES_DIR = ROOT / "locales"
README_DIR = ROOT / "docs" / "README"

SECRET_PATTERNS = {
    "OpenAI API key": re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "Google API key": re.compile(r"AIza[0-9A-Za-z_-]{25,}"),
}

REQUIRED_RUNTIME_TOKENS = [
    "qwen-asr==0.0.6",
    "Qwen/Qwen3-ASR-",
    "Qwen/Qwen3-ForcedAligner-0.6B",
    "repair_alignment_timestamps",
    "punctuation_mapping_exact",
    "cue_text_exact",
    "timestamp_mapping_monotonic",
    "alignment_raw",
]

PUBLIC_FORBIDDEN_PHRASES = [
    "fixed by project policy",
    "プロジェクト方針により固定",
]


def source_to_text(source: object) -> str:
    if isinstance(source, list):
        return "".join(str(part) for part in source)
    return str(source or "")


def notebook_text(nb: dict) -> str:
    return "\n".join(source_to_text(c.get("source", [])) for c in nb.get("cells", []))


def template_placeholder_keys(template: dict) -> set[str]:
    return set(re.findall(r"\{\{([A-Za-z0-9_.-]+)\}\}", notebook_text(template)))


def check_locales(template: dict) -> list[str]:
    errors: list[str] = []
    locale_paths = sorted(LOCALES_DIR.glob("*.json"))
    found = {p.stem for p in locale_paths}
    required = set(LANGUAGES)
    if found != required:
        errors.append(
            "locale set mismatch; "
            f"missing={sorted(required-found)}, extra={sorted(found-required)}"
        )

    expected_placeholders = template_placeholder_keys(template)
    try:
        ja = json.loads((LOCALES_DIR / "ja.json").read_text(encoding="utf-8"))
        en = json.loads((LOCALES_DIR / "en.json").read_text(encoding="utf-8"))
    except Exception as exc:
        return errors + [f"cannot read canonical locales: {exc}"]

    if not ja.get("canonical"):
        errors.append("locales/ja.json must be marked canonical=true")
    if set(ja.get("placeholders", {})) != expected_placeholders:
        errors.append("template/ja placeholder contract mismatch")
    expected_readme = set(en.get("readme", {}))

    for code in LANGUAGES:
        path = LOCALES_DIR / f"{code}.json"
        if not path.exists():
            continue
        try:
            locale = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path}: invalid JSON: {exc}")
            continue
        if locale.get("language") != code:
            errors.append(f"{path}: language must equal filename stem")
        if locale.get("native_name") != LANGUAGES[code]["native_name"]:
            errors.append(f"{path}: native_name differs from languages.py")
        if locale.get("direction") != LANGUAGES[code]["direction"]:
            errors.append(f"{path}: direction differs from languages.py")
        pkeys = set(locale.get("placeholders", {}))
        if pkeys != expected_placeholders:
            errors.append(
                f"{path}: placeholder mismatch; "
                f"missing={sorted(expected_placeholders-pkeys)}, "
                f"extra={sorted(pkeys-expected_placeholders)}"
            )
        rkeys = set(locale.get("readme", {}))
        if rkeys != expected_readme:
            errors.append(
                f"{path}: README locale-key mismatch; "
                f"missing={sorted(expected_readme-rkeys)}, extra={sorted(rkeys-expected_readme)}"
            )
        if len(locale.get("readme", {}).get("features", [])) != 8:
            errors.append(f"{path}: README features must contain 8 items")
        if len(locale.get("readme", {}).get("ci_items", [])) != 7:
            errors.append(f"{path}: README ci_items must contain 7 items")

    # User-approved Japanese wording is a release invariant.
    ja_intro = ja.get("placeholders", {}).get("intro_markdown", "")
    if "中国語・広東語は合計22の方言に対応しています。" not in ja_intro:
        errors.append("ja intro is missing the approved 22-dialect wording")
    if "60 分の音声またはビデオ ファイルの文字起こしには10分程度" not in ja_intro:
        errors.append("ja intro is missing the approved ~10-minute wording")
    return errors


def check_notebook(path: Path, template: bool = False) -> list[str]:
    errors: list[str] = []
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"{path}: invalid JSON: {exc}"]

    if nb.get("nbformat") != 4:
        errors.append(f"{path}: expected nbformat=4")

    meta = nb.get("metadata", {})
    if not template:
        code = path.stem.removeprefix("Qwen3_ASR_Colab_")
        if code not in LANGUAGES:
            errors.append(f"{path}: unexpected generated locale {code!r}")
            return errors
        info = LANGUAGES[code]
        if meta.get("qwen3_asr_colab_version") != EXPECTED_VERSION:
            errors.append(f"{path}: metadata version must be {EXPECTED_VERSION}")
        if meta.get("qwen3_asr_colab_language") != code:
            errors.append(f"{path}: metadata language mismatch")
        if meta.get("qwen3_asr_source_language") != info["qwen_name"]:
            errors.append(f"{path}: metadata source-language mismatch")
        if meta.get("colab", {}).get("name") != path.name:
            errors.append(f"{path}: Colab metadata name mismatch")

    seen_ids: set[str] = set()
    texts: list[str] = []
    for index, cell in enumerate(nb.get("cells", []), start=1):
        cid = cell.get("id")
        if not cid:
            errors.append(f"{path}: cell {index} is missing id")
        elif cid in seen_ids:
            errors.append(f"{path}: duplicate cell id {cid!r}")
        else:
            seen_ids.add(cid)

        text = source_to_text(cell.get("source", []))
        texts.append(text)
        if not template:
            if re.search(r"\{\{[A-Za-z0-9_.-]+\}\}", text):
                errors.append(f"{path}: cell {index} contains unresolved locale placeholder")
            if re.search(r"@@[A-Z0-9_]+@@", text):
                errors.append(f"{path}: cell {index} contains unresolved build token")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{path}: cell {index} contains possible {label}")

        if cell.get("cell_type") == "code":
            if cell.get("execution_count") is not None:
                errors.append(f"{path}: cell {index} has execution_count")
            if cell.get("outputs"):
                errors.append(f"{path}: cell {index} has saved outputs")
            if not template:
                try:
                    ast.parse(text or "\n")
                except SyntaxError as exc:
                    errors.append(f"{path}: cell {index} Python syntax error: {exc}")

    if not template:
        code = path.stem.removeprefix("Qwen3_ASR_Colab_")
        joined = "\n".join(texts)
        for token in REQUIRED_RUNTIME_TOKENS:
            if token not in joined:
                errors.append(f"{path}: missing required runtime token {token!r}")

        expected_source = LANGUAGES[code]["qwen_name"]
        expected_timestamp = default_timestamp_mode(code)
        if f'SOURCE_LANGUAGE = "{expected_source}"' not in joined:
            errors.append(f"{path}: wrong default SOURCE_LANGUAGE")
        if f'TIMESTAMP_MODE = "{expected_timestamp}"' not in joined:
            errors.append(f"{path}: wrong default TIMESTAMP_MODE")

        options_literal = json.dumps(source_language_options(), ensure_ascii=False)
        expected_param = f"# @param {options_literal}"
        if expected_param not in joined:
            errors.append(f"{path}: SOURCE_LANGUAGE selector is not exact Auto + 30-language list")

        for language in FORCED_ALIGNER_LANGUAGES:
            if json.dumps(language, ensure_ascii=False) not in joined:
                errors.append(f"{path}: ForcedAligner capability set is incomplete")
                break
        gate_tokens = [
            'SOURCE_LANGUAGE != "Auto"',
            "RETURN_TIMESTAMPS",
            "SOURCE_LANGUAGE not in FORCED_ALIGNER_LANGUAGES",
            "errors.timestamp_language_unsupported",
        ]
        # The localized error placeholder is rendered, so only structural gate tokens
        # other than the placeholder key remain in generated output.
        if gate_tokens[0] not in joined or gate_tokens[1] not in joined or gate_tokens[2] not in joined:
            errors.append(f"{path}: explicit-language ForcedAligner gate is missing")
    return errors


def check_readmes() -> list[str]:
    errors: list[str] = []
    expected_docs = {f"README.{code}.md" for code in LANGUAGES if code != "en"}
    found_docs = {p.name for p in README_DIR.glob("README.*.md")}
    if found_docs != expected_docs:
        errors.append(
            "localized README set mismatch; "
            f"missing={sorted(expected_docs-found_docs)}, extra={sorted(found_docs-expected_docs)}"
        )
    if (README_DIR / "README.en.md").exists():
        errors.append("README.en.md must not exist; English uses root README.md")

    paths = [ROOT / "README.md", *[README_DIR / f"README.{c}.md" for c in LANGUAGES if c != "en"]]
    row_re = re.compile(r"^\| .+ \| \[`README(?:\.[A-Za-z-]+)?\.md`\]\([^)]+\) \| \[!\[Open in Colab\]", re.M)
    for path in paths:
        if not path.exists():
            errors.append(f"{path}: missing README")
            continue
        text = path.read_text(encoding="utf-8")
        row_count = len(row_re.findall(text))
        if row_count != len(LANGUAGES):
            errors.append(f"{path}: language table has {row_count} rows, expected {len(LANGUAGES)}")
        for code in LANGUAGES:
            notebook = f"Qwen3_ASR_Colab_{code}.ipynb"
            if notebook not in text:
                errors.append(f"{path}: language table missing notebook {notebook}")
        for phrase in PUBLIC_FORBIDDEN_PHRASES:
            if phrase in text:
                errors.append(f"{path}: contains forbidden internal wording {phrase!r}")

    arch = ROOT / "docs" / "ARCHITECTURE.md"
    if arch.exists():
        text = arch.read_text(encoding="utf-8")
        for phrase in PUBLIC_FORBIDDEN_PHRASES:
            if phrase in text:
                errors.append(f"{arch}: contains forbidden internal wording {phrase!r}")
    return errors


def main() -> int:
    errors: list[str] = []
    if VERSION != EXPECTED_VERSION:
        errors.append(f"VERSION must be exactly {EXPECTED_VERSION}, got {VERSION!r}")
    if len(LANGUAGES) != 30:
        errors.append(f"languages.py must contain exactly 30 languages, got {len(LANGUAGES)}")
    if len(FORCED_ALIGNER_LANGUAGES) != 11:
        errors.append(
            f"ForcedAligner capability set must contain exactly 11 languages, "
            f"got {len(FORCED_ALIGNER_LANGUAGES)}"
        )

    template_paths = sorted(TEMPLATE_DIR.glob("*.ipynb"))
    if len(template_paths) != 1:
        errors.append(f"expected exactly one notebook template, found {len(template_paths)}")
        template = {}
    else:
        try:
            template = json.loads(template_paths[0].read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"template invalid JSON: {exc}")
            template = {}
        errors.extend(check_notebook(template_paths[0], template=True))

    if template:
        errors.extend(check_locales(template))

    generated = sorted(GENERATED_DIR.glob("Qwen3_ASR_Colab_*.ipynb"))
    expected_names = {f"Qwen3_ASR_Colab_{c}.ipynb" for c in LANGUAGES}
    found_names = {p.name for p in generated}
    if found_names != expected_names:
        errors.append(
            "generated notebook set mismatch; "
            f"missing={sorted(expected_names-found_names)}, extra={sorted(found_names-expected_names)}"
        )
    for path in generated:
        errors.extend(check_notebook(path))

    errors.extend(check_readmes())

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(
        f"Checked 30 locales, {len(generated)} generated notebooks, "
        f"and 30 README language tables; version={VERSION}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
