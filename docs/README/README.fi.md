# Qwen3-ASR Colab

Google Colab -notebookit ääni- ja videotiedostojen litterointiin Qwen3-ASR:llä.

## Ominaisuudet

- **Ilmainen:** käyttää [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) -mallia Google Colabin ilmaisella GPU:lla.
- **Aikaleimat ja tekstitykset:** Qwen3-ForcedAligner-tuetuilla kielillä `Qwen3-ForcedAligner-0.6B` antaa kohdistetut aikaleimat ja SRT:n.
- **Ei kiinteää tiedostokokorajaa notebookin puolella:** pitkiä tiedostoja voidaan käsitellä.
- **Eräkäsittely:** useita tiedostoja yhdellä ajolla.
- **Google Drive:** suora upload tai luku Google Drivesta.
- **Täysin verkossa:** mallin lataus ja litterointi Google Colabissa.
- **Useita muotoja:** JSON, TXT, CSV, Markdown, Excel ja SRT.
- **Konteksti:** `CONTEXT_INFO` voi sisältää nimiä, organisaatioita ja teknisiä termejä.

## Kielet

| Kieli | README | Notebook |
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

## Repositoryn rakenne

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

Template-notebook on yhteinen koodilähde. Locale-tiedostot tarjoavat kielikohtaiset Colab-tekstit kuten `# @title`, `# @markdown`, kommentit ja valitut käyttäjäviestit. Jokaisessa localessa on koko placeholder-joukko kuratoidusta japanilaisesta notebookista.

Luodut notebookit commitoidaan, jotta Colab-linkit pysyvät vakaina.

## Build

```bash
python scripts/build_readmes.py
python scripts/build_notebooks.py
```

## Päivitä käännökset

`translate_full_locales.py` on ylläpitotyökalu, joka päivittää muut localet englannista suojaten code tokenit, mallitunnisteet ja Colab-asetukset. Tarkista käännökset ennen virallista julkaisua.

## Tarkistukset

```bash
python scripts/check_notebooks.py
```

CI luo README/notebookit uudelleen ja tarkistaa generointierot, Notebook JSONin, Python-syntaksin, ratkaisemattomat placeholderit, tallennetut solutulosteet, ilmeiset secretit ja kaikkien 30 kielen artefaktien johdonmukaisuuden.

## Mitä CI voi testata

Tämä repository voi testata notebookia jaettavana artefaktina:

- deterministinen generointi templatesta ja localeista
- Notebook JSONin kelvollisuus
- tyhjät suoritustulosteet
- Python-syntaksi koodisoluissa
- ei ratkaisemattomia placeholdereita
- ei ilmeisiä vahingossa lisättyjä secretejä
- commitoidut README/notebookit vastaavat lähteitä

Täysi litterointipolku tarvitsee Colab-kohtaiset API:t, mallien lataukset, GPU:n saatavuuden ja käyttäjän median. GPU end-to-end -validointi on siksi edelleen manuaalinen UAT. Japanilainen polku on validoitu Google Colabissa oikealla pitkällä äänellä.

## Lisenssi

Tämän repositoryn notebook-scaffolding ja build-skriptit julkaistaan MIT License -ehdoin. Qwen3-ASR, mallipainot ja kolmannen osapuolen dependencies ovat omien lisenssiensä alaisia.
