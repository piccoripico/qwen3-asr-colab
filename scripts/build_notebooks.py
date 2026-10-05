"""Build localized Colab notebooks from the shared template.

Japanese is the curated canonical notebook copy. Every published Qwen3-ASR
language has a complete locale file. Model capability data lives in
scripts/languages.py rather than being duplicated across locale files.
"""
from __future__ import annotations

import copy
import json
import re
from pathlib import Path

from languages import (
    FORCED_ALIGNER_LANGUAGES,
    LANGUAGES,
    default_timestamp_mode,
    source_language_options,
)

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
TEMPLATE_PATH = ROOT / "notebook_template" / "Qwen3_ASR_Colab.template.ipynb"
LOCALES_DIR = ROOT / "locales"
OUTPUT_DIR = ROOT / "notebooks"
CANONICAL_LOCALE = "ja"

BUILD_TOKENS = {
    "@@SOURCE_LANGUAGE_OPTIONS@@",
    "@@DEFAULT_SOURCE_LANGUAGE@@",
    "@@DEFAULT_TIMESTAMP_MODE@@",
    "@@FORCED_ALIGNER_LANGUAGES@@",
}


def source_to_text(source: object) -> str:
    if isinstance(source, list):
        return "".join(str(part) for part in source)
    return str(source or "")


def text_to_source(text: str) -> list[str]:
    return text.splitlines(keepends=True)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def clear_outputs(nb: dict) -> None:
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            cell["execution_count"] = None
            cell["outputs"] = []


def locale_placeholder_keys(template: dict) -> set[str]:
    text = "\n".join(source_to_text(c.get("source", [])) for c in template.get("cells", []))
    return set(re.findall(r"\{\{([A-Za-z0-9_.-]+)\}\}", text))


def validate_locale(locale: dict, expected_keys: set[str], path: Path) -> None:
    code = locale.get("language")
    if code != path.stem:
        raise ValueError(f"{path}: language must equal filename stem")
    if code not in LANGUAGES:
        raise ValueError(f"{path}: unsupported locale code {code!r}")
    keys = set(locale.get("placeholders", {}))
    missing = expected_keys - keys
    extra = keys - expected_keys
    if missing or extra:
        raise ValueError(
            f"{path}: placeholder key mismatch; missing={sorted(missing)}, extra={sorted(extra)}"
        )


def render_locale(template: dict, locale: dict) -> dict:
    nb = copy.deepcopy(template)
    language = locale["language"]
    info = LANGUAGES[language]
    placeholders = locale["placeholders"]

    source_options = json.dumps(source_language_options(), ensure_ascii=False)
    aligner_languages = "{" + ", ".join(
        json.dumps(x, ensure_ascii=False) for x in sorted(FORCED_ALIGNER_LANGUAGES)
    ) + "}"
    build_values = {
        "@@SOURCE_LANGUAGE_OPTIONS@@": source_options,
        "@@DEFAULT_SOURCE_LANGUAGE@@": info["qwen_name"],
        "@@DEFAULT_TIMESTAMP_MODE@@": default_timestamp_mode(language),
        "@@FORCED_ALIGNER_LANGUAGES@@": aligner_languages,
    }

    for cell in nb.get("cells", []):
        text = source_to_text(cell.get("source", []))
        for token, value in build_values.items():
            text = text.replace(token, value)
        for key, value in placeholders.items():
            text = text.replace(
                f'"{{{{{key}}}}}"',
                json.dumps(str(value), ensure_ascii=False),
            )
            text = text.replace(f"{{{{{key}}}}}", str(value))
        cell["source"] = text_to_source(text)

    metadata = nb.setdefault("metadata", {})
    metadata["qwen3_asr_colab_version"] = VERSION
    metadata["qwen3_asr_colab_language"] = language
    metadata["qwen3_asr_source_language"] = info["qwen_name"]
    metadata["qwen3_asr_colab_source_template"] = str(TEMPLATE_PATH.relative_to(ROOT).as_posix())
    metadata.setdefault("colab", {})["name"] = f"Qwen3_ASR_Colab_{language}.ipynb"
    clear_outputs(nb)
    return nb


def remove_stale_notebooks() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for path in OUTPUT_DIR.glob("Qwen3_ASR_Colab_*.ipynb"):
        path.unlink()


def build() -> list[Path]:
    template = load_json(TEMPLATE_PATH)
    canonical = load_json(LOCALES_DIR / f"{CANONICAL_LOCALE}.json")
    expected_keys = locale_placeholder_keys(template)
    if set(canonical.get("placeholders", {})) != expected_keys:
        raise ValueError("template/ja locale placeholder contract mismatch")

    locale_paths = sorted(LOCALES_DIR.glob("*.json"))
    found = {p.stem for p in locale_paths}
    required = set(LANGUAGES)
    if found != required:
        raise ValueError(
            "Locale set must match Qwen3-ASR's 30 published languages; "
            f"missing={sorted(required-found)}, extra={sorted(found-required)}"
        )

    remove_stale_notebooks()
    written: list[Path] = []
    for code in LANGUAGES:
        locale_path = LOCALES_DIR / f"{code}.json"
        locale = load_json(locale_path)
        validate_locale(locale, expected_keys, locale_path)
        rendered = render_locale(template, locale)
        out = OUTPUT_DIR / f"Qwen3_ASR_Colab_{code}.ipynb"
        out.write_text(json.dumps(rendered, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        written.append(out)
    return written


if __name__ == "__main__":
    for path in build():
        print(path.relative_to(ROOT).as_posix())
