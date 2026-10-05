"""Refresh non-Japanese locales from the English locale.

Maintenance helper only; ordinary CI does not run this script. The committed
locale files are the distributable source used by build_notebooks.py and
build_readmes.py. Japanese is intentionally left untouched because it is the
curated canonical notebook copy.
"""
from __future__ import annotations

import json
import re
import time
from pathlib import Path

from deep_translator import GoogleTranslator

from languages import LANGUAGES

ROOT = Path(__file__).resolve().parents[1]
LOCALES_DIR = ROOT / "locales"

TARGETS = {
    "zh": "zh-CN", "en": "en", "yue": None, "ar": "ar", "de": "de",
    "fr": "fr", "es": "es", "pt": "pt", "id": "id", "it": "it",
    "ko": "ko", "ru": "ru", "th": "th", "vi": "vi", "ja": "ja",
    "tr": "tr", "hi": "hi", "ms": "ms", "nl": "nl", "sv": "sv",
    "da": "da", "fi": "fi", "pl": "pl", "cs": "cs", "fil": "tl",
    "fa": "fa", "el": "el", "hu": "hu", "mk": "mk", "ro": "ro",
}

PROTECT_PATTERNS = [
    re.compile(r"\[[^\]]+\]\([^)]+\)"),
    re.compile(r"`[^`]+`"),
    re.compile(r"https?://\S+"),
    re.compile(r"\bGoogle Colab\b"), re.compile(r"\bGoogle Drive\b"),
    re.compile(r"\bQwen3-ASR\b"), re.compile(r"\bQwen3-ForcedAligner-0\.6B\b"),
    re.compile(r"\bCUDA\b"), re.compile(r"\bGPU\b"), re.compile(r"\bBF16\b"),
    re.compile(r"\bJSON\b"), re.compile(r"\bTXT\b"), re.compile(r"\bCSV\b"),
    re.compile(r"\bXLSX\b"), re.compile(r"\bSRT\b"), re.compile(r"\bZIP\b"),
    re.compile(r"\b[A-Z][A-Z0-9_]{2,}\b"),
]
PROTECT_RE = re.compile("|".join(f"(?:{p.pattern})" for p in PROTECT_PATTERNS))
PREFIXES = [
    re.compile(r"^(# @title \d+\. )(.*)$", re.S),
    re.compile(r"^(# \d+\. )(.*)$", re.S),
    re.compile(r"^(# @markdown #{2,3} )(.*)$", re.S),
    re.compile(r"^(# @markdown - )(.*)$", re.S),
    re.compile(r"^(# )(.*)$", re.S),
]


def protect(text):
    tokens={}
    def repl(m):
        token=f"@@P{len(tokens):04d}@@"; tokens[token]=m.group(0); return token
    return PROTECT_RE.sub(repl,text),tokens


def restore(text,tokens):
    for k,v in tokens.items(): text=text.replace(k,v)
    return text


def split_prefix(text):
    for p in PREFIXES:
        m=p.match(text)
        if m: return m.group(1),m.group(2)
    return "",text


def translate_text(translator,text):
    prefix,body=split_prefix(text)
    protected,tokens=protect(body)
    for attempt in range(4):
        try:
            result=translator.translate(protected)
            return prefix+restore(result,tokens)
        except Exception:
            if attempt==3: raise
            time.sleep(2*(attempt+1))


def translate_value(translator,value):
    if isinstance(value,str): return translate_text(translator,value)
    if isinstance(value,list): return [translate_text(translator,x) for x in value]
    return value


def main():
    en=json.loads((LOCALES_DIR/'en.json').read_text(encoding='utf-8'))
    for code in LANGUAGES:
        if code in {'en','ja'}: continue
        target=TARGETS[code]
        if target is None:
            print(f'Skipping {code}: no suitable translation target; keep committed locale.', flush=True)
            continue
        print(f'Translating {code} -> {target}...',flush=True)
        tr=GoogleTranslator(source='en',target=target)
        data=json.loads(json.dumps(en,ensure_ascii=False))
        data['language']=code
        data['language_name']=LANGUAGES[code]['native_name']
        data['native_name']=LANGUAGES[code]['native_name']
        data['direction']=LANGUAGES[code]['direction']
        data['canonical']=False
        data['translation_source']='machine-translated from en; review before release'
        data['placeholders']={k:translate_value(tr,v) for k,v in en['placeholders'].items()}
        data['readme']={k:translate_value(tr,v) for k,v in en['readme'].items()}
        (LOCALES_DIR/f'{code}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__': main()
