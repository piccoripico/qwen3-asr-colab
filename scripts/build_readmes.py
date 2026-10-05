"""Build the root English README and localized README files."""
from __future__ import annotations

import json
from pathlib import Path

from languages import LANGUAGES

ROOT = Path(__file__).resolve().parents[1]
LOCALES_DIR = ROOT / "locales"
DOCS_README_DIR = ROOT / "docs" / "README"
REPO = "piccoripico/qwen3-asr-colab"


def load_locale(code: str) -> dict:
    return json.loads((LOCALES_DIR / f"{code}.json").read_text(encoding="utf-8"))


def colab_badge(code: str) -> str:
    notebook = f"notebooks/Qwen3_ASR_Colab_{code}.ipynb"
    url = f"https://colab.research.google.com/github/{REPO}/blob/main/{notebook}"
    return f"[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)]({url})"


def readme_link(code: str, localized: bool) -> str:
    if code == "en":
        return "../../README.md" if localized else "README.md"
    return f"README.{code}.md" if localized else f"docs/README/README.{code}.md"


def language_rows(localized: bool) -> list[str]:
    rows = []
    for code, info in LANGUAGES.items():
        link = readme_link(code, localized)
        rows.append(
            f"| {info['native_name']} | [`{Path(link).name}`]({link}) | {colab_badge(code)} |"
        )
    return rows


def repository_layout() -> str:
    return """```text
notebook_template/
  Qwen3_ASR_Colab.template.ipynb
locales/
  *.json
notebooks/
  Qwen3_ASR_Colab_<language-code>.ipynb
docs/
  README/
    README.<language-code>.md
  ARCHITECTURE.md
scripts/
  languages.py
  build_readmes.py
  build_notebooks.py
  check_notebooks.py
  translate_full_locales.py
.github/
  workflows/
    ci.yml
```"""


def build_text(locale: dict, localized: bool) -> str:
    r = locale["readme"]
    rows = [
        f"| {r['language_label']} | {r['readme_label']} | {r['notebook_label']} |",
        "| --- | --- | --- |",
        *language_rows(localized),
    ]
    parts = [
        r["title"], "", r["subtitle"], "",
        r["features_heading"], "",
        *[f"- {item}" for item in r["features"]], "",
        r["languages_heading"], "", *rows, "",
        f"## {r['repository_layout']}", "", repository_layout(), "",
        r["template_note"], "", r["generated_note"], "",
        f"## {r['build']}", "",
        "```bash\npython scripts/build_readmes.py\npython scripts/build_notebooks.py\n```", "",
        f"## {r['refresh_translations']}", "", r["refresh_note"], "",
        f"## {r['checks']}", "",
        "```bash\npython scripts/check_notebooks.py\n```", "", r["checks_note"], "",
        f"## {r['what_ci_can_test']}", "", r["ci_intro"], "",
        *[f"- {item}" for item in r["ci_items"]], "", r["ci_limit"], "",
        f"## {r['license']}", "", r["license_note"], "",
    ]
    return "\n".join(parts).rstrip() + "\n"


def build() -> list[Path]:
    found = {p.stem for p in LOCALES_DIR.glob("*.json")}
    required = set(LANGUAGES)
    if found != required:
        raise ValueError(
            "Locale set must match Qwen3-ASR's 30 published languages; "
            f"missing={sorted(required-found)}, extra={sorted(found-required)}"
        )

    DOCS_README_DIR.mkdir(parents=True, exist_ok=True)
    for stale in DOCS_README_DIR.glob("README.*.md"):
        stale.unlink()

    written: list[Path] = []
    root = ROOT / "README.md"
    root.write_text(build_text(load_locale("en"), localized=False), encoding="utf-8")
    written.append(root)

    for code in LANGUAGES:
        if code == "en":
            continue
        out = DOCS_README_DIR / f"README.{code}.md"
        out.write_text(build_text(load_locale(code), localized=True), encoding="utf-8")
        written.append(out)
    return written


if __name__ == "__main__":
    for path in build():
        print(path.relative_to(ROOT).as_posix())
