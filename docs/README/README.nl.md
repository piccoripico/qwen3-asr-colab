# Qwen3-ASR Colab

Google Colab-notebooks voor het transcriberen van audio- en videobestanden met Qwen3-ASR.

## Functies

- **Gratis:** gebruikt [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) met de gratis GPU van Google Colab.
- **Tijdstempels en ondertitels:** voor Qwen3-ForcedAligner-talen levert `Qwen3-ForcedAligner-0.6B` uitgelijnde tijdstempels en SRT.
- **Geen vaste bestandsgroottelimiet aan notebookzijde:** lange bestanden kunnen worden verwerkt.
- **Batchverwerking:** meerdere bestanden in één run.
- **Google Drive:** direct uploaden of lezen vanuit Google Drive.
- **Volledig online:** modeldownload en transcriptie draaien op Google Colab.
- **Meerdere formaten:** JSON, TXT, CSV, Markdown, Excel en SRT.
- **Context:** `CONTEXT_INFO` kan namen, organisaties en technische termen bevatten.

## Talen

| Taal | README | Notebook |
| --- | --- | --- |
| 中文 | [`README.zh.md`](README.zh.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_zh.ipynb) |
| English | [`README.md`](../../README.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_en.ipynb) |
| 廣東話 | [`README.yue.md`](README.yue.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_yue.ipynb) |
| العربية | [`README.ar.md`](README.ar.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_ar.ipynb) |
| Deutsch | [`README.de.md`](README.de.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_de.ipynb) |
| Français | [`README.fr.md`](README.fr.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_fr.ipynb) |
| Español | [`README.es.md`](README.es.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_es.ipynb) |
| Português | [`README.pt.md`](README.pt.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_pt.ipynb) |
| Bahasa Indonesia | [`README.id.md`](README.id.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_id.ipynb) |
| Italiano | [`README.it.md`](README.it.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_it.ipynb) |
| 한국어 | [`README.ko.md`](README.ko.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_ko.ipynb) |
| Русский | [`README.ru.md`](README.ru.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_ru.ipynb) |
| ไทย | [`README.th.md`](README.th.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_th.ipynb) |
| Tiếng Việt | [`README.vi.md`](README.vi.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_vi.ipynb) |
| 日本語 | [`README.ja.md`](README.ja.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_ja.ipynb) |
| Türkçe | [`README.tr.md`](README.tr.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_tr.ipynb) |
| हिन्दी | [`README.hi.md`](README.hi.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_hi.ipynb) |
| Bahasa Melayu | [`README.ms.md`](README.ms.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_ms.ipynb) |
| Nederlands | [`README.nl.md`](README.nl.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_nl.ipynb) |
| Svenska | [`README.sv.md`](README.sv.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_sv.ipynb) |
| Dansk | [`README.da.md`](README.da.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_da.ipynb) |
| Suomi | [`README.fi.md`](README.fi.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_fi.ipynb) |
| Polski | [`README.pl.md`](README.pl.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_pl.ipynb) |
| Čeština | [`README.cs.md`](README.cs.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_cs.ipynb) |
| Filipino | [`README.fil.md`](README.fil.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_fil.ipynb) |
| فارسی | [`README.fa.md`](README.fa.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_fa.ipynb) |
| Ελληνικά | [`README.el.md`](README.el.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_el.ipynb) |
| Magyar | [`README.hu.md`](README.hu.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_hu.ipynb) |
| Македонски | [`README.mk.md`](README.mk.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_mk.ipynb) |
| Română | [`README.ro.md`](README.ro.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/qwen3-asr-colab/blob/main/notebooks/Qwen3_ASR_Colab_ro.ipynb) |

## Repository-indeling

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

Het template-notebook is de gedeelde codebron. Locale-bestanden leveren taalspecifieke tekst voor Colab, zoals `# @title`, `# @markdown`, opmerkingen en geselecteerde gebruikersmeldingen. Elke locale bevat de volledige placeholder-set van het handmatig verzorgde Japanse notebook.

Gegenereerde notebooks worden gecommit zodat Colab-links stabiel blijven.

## Build

```bash
python scripts/build_readmes.py
python scripts/build_notebooks.py
```

## Vertalingen vernieuwen

`translate_full_locales.py` is een onderhoudstool die andere locales vanuit Engels vernieuwt terwijl code-tokens, model-ID’s en Colab-instellingen worden beschermd. Controleer vertalingen vóór een formele release.

## Controles

```bash
python scripts/check_notebooks.py
```

CI genereert README/notebooks opnieuw en controleert verschillen, Notebook JSON, Python-syntaxis, onopgeloste placeholders, opgeslagen celuitvoer, duidelijke secrets en consistentie van alle 30 taal-artefacten.

## Wat CI kan testen

Deze repository kan het notebook als distributie-artefact testen op:

- deterministische generatie uit template en locale
- geldigheid van Notebook JSON
- lege uitvoerresultaten
- Python-syntaxis in codecellen
- geen onopgeloste placeholders
- duidelijke per ongeluk toegevoegde secrets
- gecommitte README/notebooks komen overeen met hun bronnen

Het volledige transcriptiepad vereist Colab-specifieke API’s, modeldownloads, GPU-beschikbaarheid en media van de gebruiker. GPU end-to-end-validatie blijft daarom handmatige UAT. Het Japanse pad is in Google Colab met echte lange audio gevalideerd.

## Licentie

De notebook-scaffolding en build-scripts van deze repository vallen onder de MIT License. Qwen3-ASR, modelgewichten en externe dependencies vallen onder hun eigen licenties.
