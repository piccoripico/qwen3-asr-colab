# Repository Architecture

## Source of truth

The repository separates shared runtime logic, model capability data, localized
copy, and generated distribution artifacts.

1. `notebook_template/Qwen3_ASR_Colab.template.ipynb`
   - shared notebook structure and runtime logic
   - locale placeholders for Colab-facing copy
   - build tokens for per-language defaults
2. `scripts/languages.py`
   - the 30 Qwen3-ASR language codes and canonical model language names
   - the 11 Qwen3-ForcedAligner languages
   - per-language default timestamp mode
3. `locales/*.json`
   - one complete locale for each of the 30 Qwen3-ASR languages
   - notebook UI/Markdown/messages and README copy
   - Japanese is the curated canonical locale for the notebook copy
4. `notebooks/Qwen3_ASR_Colab_<language-code>.ipynb`
   - 30 generated distributable notebooks committed for stable Colab URLs
5. `README.md` and `docs/README/README.<language-code>.md`
   - root English README plus 29 localized README files
   - every README contains the same 30-language notebook table

Missing or extra locales, placeholder-key differences, generated-file count
mismatches, or incorrect per-language defaults fail generation/checks rather
than silently falling back to another locale.

## Language and timestamp behavior

Every generated notebook exposes `Auto` plus all 30 Qwen3-ASR languages in
`SOURCE_LANGUAGE`.

For an explicitly selected source language, `word` and `subtitle` timestamp
modes are rejected before model execution when that language is outside the 11
languages published for Qwen3-ForcedAligner. `TIMESTAMP_MODE = "none"` remains
available for all 30 languages.

When `SOURCE_LANGUAGE = "Auto"`, timestamp modes are not pre-blocked. The model
and aligner are allowed to attempt the request, and any actual runtime failure
is surfaced normally.

The 11 ForcedAligner-supported locale notebooks default to `subtitle`; the other
19 default to `none`. The default source language matches each notebook locale.

## Canonical Japanese notebook

The Japanese notebook implementation has been validated end-to-end in Google
Colab with real long-form audio. Localization generation keeps the ASR,
ForcedAligner, punctuation reconstruction, timestamp repair, and export logic
shared across all notebook variants.

## Build

```bash
python scripts/build_readmes.py
python scripts/build_notebooks.py
python scripts/check_notebooks.py
```

`translate_full_locales.py` is a maintenance helper for refreshing translated
copy. It is intentionally not part of ordinary CI.

## CI

GitHub Actions rebuilds all generated README/notebook artifacts, performs static
checks, and requires the committed generated files to match their sources. Full
GPU transcription remains a manual Colab validation because it depends on Colab
APIs, model downloads, GPU availability, and input media.
