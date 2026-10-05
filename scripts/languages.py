"""Qwen3-ASR language capabilities used by repository generators.

Keep model capability data separate from localized UI copy.
"""
from __future__ import annotations

LANGUAGES = {
    "zh": {"qwen_name": "Chinese", "english_name": "Chinese", "native_name": "中文", "direction": "ltr"},
    "en": {"qwen_name": "English", "english_name": "English", "native_name": "English", "direction": "ltr"},
    "yue": {"qwen_name": "Cantonese", "english_name": "Cantonese", "native_name": "廣東話", "direction": "ltr"},
    "ar": {"qwen_name": "Arabic", "english_name": "Arabic", "native_name": "العربية", "direction": "rtl"},
    "de": {"qwen_name": "German", "english_name": "German", "native_name": "Deutsch", "direction": "ltr"},
    "fr": {"qwen_name": "French", "english_name": "French", "native_name": "Français", "direction": "ltr"},
    "es": {"qwen_name": "Spanish", "english_name": "Spanish", "native_name": "Español", "direction": "ltr"},
    "pt": {"qwen_name": "Portuguese", "english_name": "Portuguese", "native_name": "Português", "direction": "ltr"},
    "id": {"qwen_name": "Indonesian", "english_name": "Indonesian", "native_name": "Bahasa Indonesia", "direction": "ltr"},
    "it": {"qwen_name": "Italian", "english_name": "Italian", "native_name": "Italiano", "direction": "ltr"},
    "ko": {"qwen_name": "Korean", "english_name": "Korean", "native_name": "한국어", "direction": "ltr"},
    "ru": {"qwen_name": "Russian", "english_name": "Russian", "native_name": "Русский", "direction": "ltr"},
    "th": {"qwen_name": "Thai", "english_name": "Thai", "native_name": "ไทย", "direction": "ltr"},
    "vi": {"qwen_name": "Vietnamese", "english_name": "Vietnamese", "native_name": "Tiếng Việt", "direction": "ltr"},
    "ja": {"qwen_name": "Japanese", "english_name": "Japanese", "native_name": "日本語", "direction": "ltr"},
    "tr": {"qwen_name": "Turkish", "english_name": "Turkish", "native_name": "Türkçe", "direction": "ltr"},
    "hi": {"qwen_name": "Hindi", "english_name": "Hindi", "native_name": "हिन्दी", "direction": "ltr"},
    "ms": {"qwen_name": "Malay", "english_name": "Malay", "native_name": "Bahasa Melayu", "direction": "ltr"},
    "nl": {"qwen_name": "Dutch", "english_name": "Dutch", "native_name": "Nederlands", "direction": "ltr"},
    "sv": {"qwen_name": "Swedish", "english_name": "Swedish", "native_name": "Svenska", "direction": "ltr"},
    "da": {"qwen_name": "Danish", "english_name": "Danish", "native_name": "Dansk", "direction": "ltr"},
    "fi": {"qwen_name": "Finnish", "english_name": "Finnish", "native_name": "Suomi", "direction": "ltr"},
    "pl": {"qwen_name": "Polish", "english_name": "Polish", "native_name": "Polski", "direction": "ltr"},
    "cs": {"qwen_name": "Czech", "english_name": "Czech", "native_name": "Čeština", "direction": "ltr"},
    "fil": {"qwen_name": "Filipino", "english_name": "Filipino", "native_name": "Filipino", "direction": "ltr"},
    "fa": {"qwen_name": "Persian", "english_name": "Persian", "native_name": "فارسی", "direction": "rtl"},
    "el": {"qwen_name": "Greek", "english_name": "Greek", "native_name": "Ελληνικά", "direction": "ltr"},
    "hu": {"qwen_name": "Hungarian", "english_name": "Hungarian", "native_name": "Magyar", "direction": "ltr"},
    "mk": {"qwen_name": "Macedonian", "english_name": "Macedonian", "native_name": "Македонски", "direction": "ltr"},
    "ro": {"qwen_name": "Romanian", "english_name": "Romanian", "native_name": "Română", "direction": "ltr"},
}

FORCED_ALIGNER_LANGUAGES = {
    "Chinese", "English", "Cantonese", "French", "German", "Italian",
    "Japanese", "Korean", "Portuguese", "Russian", "Spanish",
}

CHINESE_DIALECT_COUNT = 22


def default_timestamp_mode(code: str) -> str:
    return "subtitle" if LANGUAGES[code]["qwen_name"] in FORCED_ALIGNER_LANGUAGES else "none"


def source_language_options() -> list[str]:
    return ["Auto", *[item["qwen_name"] for item in LANGUAGES.values()]]
