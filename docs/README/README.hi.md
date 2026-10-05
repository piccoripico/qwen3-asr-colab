# Qwen3-ASR Colab

Qwen3-ASR से ऑडियो और वीडियो फ़ाइलें ट्रांसक्राइब करने के लिए Google Colab नोटबुक।

## विशेषताएँ

- **मुफ़्त उपयोग:** [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) और Google Colab मुफ़्त GPU का उपयोग।
- **टाइमस्टैम्प और सबटाइटल:** Qwen3-ForcedAligner समर्थित भाषाओं में `Qwen3-ForcedAligner-0.6B` aligned टाइमस्टैम्प और SRT प्रदान करता है।
- **नोटबुक की ओर से कोई स्थिर फ़ाइल आकार सीमा नहीं:** लंबी फ़ाइलें प्रोसेस की जा सकती हैं।
- **बैच प्रोसेसिंग:** एक रन में कई फ़ाइलें।
- **Google Drive:** सीधे अपलोड या Google Drive से पढ़ें।
- **पूरी तरह ऑनलाइन:** मॉडल डाउनलोड और ट्रांसक्रिप्शन Google Colab पर।
- **कई प्रारूप:** JSON, TXT, CSV, Markdown, Excel और SRT।
- **कॉन्टेक्स्ट:** `CONTEXT_INFO` नाम, संगठन और तकनीकी शब्द दे सकता है।

## भाषाएँ

| भाषा | README | Notebook |
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

## Repository संरचना

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

Template notebook साझा code source है। Locale फ़ाइलें `# @title`, `# @markdown`, टिप्पणियाँ और कुछ user messages जैसे Colab-facing text के भाषा-विशिष्ट मान देती हैं। हर locale में curated जापानी notebook के समान पूरा placeholder set होता है।

Generated notebooks को Colab links स्थिर रखने के लिए repository में commit किया जाता है।

## Build

```bash
python scripts/build_readmes.py
python scripts/build_notebooks.py
```

## अनुवाद अपडेट करें

`translate_full_locales.py` एक maintenance tool है जो code tokens, model identifiers और Colab settings को सुरक्षित रखते हुए English locale से अन्य locales को अपडेट करता है। Formal release से पहले अनुवाद जाँचें।

## जाँच

```bash
python scripts/check_notebooks.py
```

CI README/notebooks को दोबारा generate करता है और generation diff, Notebook JSON, Python syntax, unresolved placeholders, saved cell outputs, स्पष्ट secrets और सभी 30 भाषा artefacts की consistency जाँचता है।

## CI क्या जाँच सकता है

यह repository notebook को distributable artefact के रूप में इन बिंदुओं पर जाँच सकता है:

- template और locale से deterministic generation
- Notebook JSON validity
- empty execution outputs
- code cells में Python syntax
- कोई unresolved placeholder नहीं
- स्पष्ट accidental secrets
- committed README/notebook sources से मेल खाते हैं

पूर्ण transcription path को Colab-specific APIs, model downloads, GPU availability और user-provided media की आवश्यकता है। इसलिए GPU end-to-end validation manual UAT रहता है। जापानी path को Google Colab पर वास्तविक long-form audio के साथ validate किया गया है।

## लाइसेंस

इस repository का notebook scaffolding और build scripts MIT License के अंतर्गत जारी हैं। Qwen3-ASR, model weights और third-party dependencies अपने-अपने licenses के अधीन हैं।
