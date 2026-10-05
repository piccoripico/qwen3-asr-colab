# Qwen3-ASR Colab

Google Colab notebooks for transcribing audio and video files with Qwen3-ASR.

## Features

- **Free to use:** Uses [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) with Google Colab's free GPU runtime.
- **Timestamps and subtitles:** For languages supported by Qwen3-ForcedAligner, `Qwen3-ForcedAligner-0.6B` provides aligned timestamps and SRT subtitle generation.
- **No fixed notebook-side file size limit:** Long audio and video files can be processed.
- **Batch processing:** Multiple audio and video files can be processed in one run.
- **Google Drive support:** Files can be uploaded directly or read from Google Drive.
- **Fully online:** Model download and transcription run on Google Colab.
- **Multiple output formats:** JSON, TXT, CSV, Markdown, Excel, and SRT are supported.
- **Context hints:** `CONTEXT_INFO` can provide names, organizations, and technical terms.

## Languages

| Language | README | Notebook |
| --- | --- | --- |
| 中文 | [`README.zh.md`](docs/README/README.zh.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_zh.ipynb) |
| English | [`README.md`](README.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_en.ipynb) |
| 廣東話 | [`README.yue.md`](docs/README/README.yue.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_yue.ipynb) |
| العربية | [`README.ar.md`](docs/README/README.ar.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_ar.ipynb) |
| Deutsch | [`README.de.md`](docs/README/README.de.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_de.ipynb) |
| Français | [`README.fr.md`](docs/README/README.fr.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_fr.ipynb) |
| Español | [`README.es.md`](docs/README/README.es.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_es.ipynb) |
| Português | [`README.pt.md`](docs/README/README.pt.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_pt.ipynb) |
| Bahasa Indonesia | [`README.id.md`](docs/README/README.id.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_id.ipynb) |
| Italiano | [`README.it.md`](docs/README/README.it.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_it.ipynb) |
| 한국어 | [`README.ko.md`](docs/README/README.ko.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_ko.ipynb) |
| Русский | [`README.ru.md`](docs/README/README.ru.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_ru.ipynb) |
| ไทย | [`README.th.md`](docs/README/README.th.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_th.ipynb) |
| Tiếng Việt | [`README.vi.md`](docs/README/README.vi.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_vi.ipynb) |
| 日本語 | [`README.ja.md`](docs/README/README.ja.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_ja.ipynb) |
| Türkçe | [`README.tr.md`](docs/README/README.tr.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_tr.ipynb) |
| हिन्दी | [`README.hi.md`](docs/README/README.hi.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_hi.ipynb) |
| Bahasa Melayu | [`README.ms.md`](docs/README/README.ms.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_ms.ipynb) |
| Nederlands | [`README.nl.md`](docs/README/README.nl.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_nl.ipynb) |
| Svenska | [`README.sv.md`](docs/README/README.sv.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_sv.ipynb) |
| Dansk | [`README.da.md`](docs/README/README.da.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_da.ipynb) |
| Suomi | [`README.fi.md`](docs/README/README.fi.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_fi.ipynb) |
| Polski | [`README.pl.md`](docs/README/README.pl.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_pl.ipynb) |
| Čeština | [`README.cs.md`](docs/README/README.cs.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_cs.ipynb) |
| Filipino | [`README.fil.md`](docs/README/README.fil.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_fil.ipynb) |
| فارسی | [`README.fa.md`](docs/README/README.fa.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_fa.ipynb) |
| Ελληνικά | [`README.el.md`](docs/README/README.el.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_el.ipynb) |
| Magyar | [`README.hu.md`](docs/README/README.hu.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_hu.ipynb) |
| Македонски | [`README.mk.md`](docs/README/README.mk.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_mk.ipynb) |
| Română | [`README.ro.md`](docs/README/README.ro.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_ro.ipynb) |

## Repository Layout

```text
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
```

The template notebook is the shared code source of truth. Locale files provide language-specific values for Colab-facing copy such as `# @title`, `# @markdown`, comments, and selected user messages. Every locale contains the complete placeholder set from the curated Japanese notebook.

Generated notebooks are committed so Colab links stay stable.

## Build

```bash
python scripts/build_readmes.py
python scripts/build_notebooks.py
```

## Refresh Translations

`translate_full_locales.py` is a maintenance helper that refreshes other locales from the English locale while preserving code tokens, model identifiers, and Colab settings. Review translated copy before a formal release.

## Checks

```bash
python scripts/check_notebooks.py
```

CI rebuilds README/notebook artifacts and checks generated diffs, notebook JSON, Python syntax, unresolved placeholders, saved outputs, obvious secrets, and consistency across all 30 language artifacts.

## What CI Can Test

This repository can test the notebook as a distributable artifact:

- deterministic generation from the template and locale files
- notebook JSON validity
- empty execution outputs
- Python syntax in code cells
- no unresolved placeholders
- obvious accidental secrets
- committed generated README/notebook files matching their sources

The full transcription path requires Colab-specific APIs, model downloads, GPU availability, and user-provided media. GPU end-to-end validation remains a manual UAT. The Japanese path has been validated in Google Colab with real long-form audio.

## License

This repository's notebook scaffolding and build scripts are released under the MIT License. Qwen3-ASR, model weights, and third-party dependencies are governed by their respective licenses.
