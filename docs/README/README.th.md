# Qwen3-ASR Colab

โน้ตบุ๊ก Google Colab สำหรับถอดเสียงไฟล์เสียงและวิดีโอด้วย Qwen3-ASR

## คุณสมบัติ

- **ใช้งานฟรี:** ใช้ [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) กับ GPU ฟรีของ Google Colab
- **ประทับเวลาและคำบรรยาย:** สำหรับภาษาที่ Qwen3-ForcedAligner รองรับ `Qwen3-ForcedAligner-0.6B` ให้ประทับเวลาที่จัดแนวและสร้าง SRT
- **ไม่มีขีดจำกัดขนาดไฟล์ตายตัวจากฝั่งโน้ตบุ๊ก:** ประมวลผลไฟล์ยาวได้
- **ประมวลผลแบบกลุ่ม:** หลายไฟล์ในการรันเดียว
- **Google Drive:** อัปโหลดโดยตรงหรืออ่านจาก Google Drive
- **ออนไลน์ทั้งหมด:** ดาวน์โหลดโมเดลและถอดเสียงบน Google Colab
- **หลายรูปแบบ:** JSON, TXT, CSV, Markdown, Excel และ SRT
- **บริบท:** `CONTEXT_INFO` ใช้ระบุชื่อ องค์กร และคำศัพท์เทคนิคได้

## ภาษา

| ภาษา | README | Notebook |
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

## โครงสร้าง Repository

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

Notebook template เป็นแหล่งโค้ดร่วม ไฟล์ locale ให้ข้อความเฉพาะภาษาแก่หน้าจอ Colab เช่น `# @title`, `# @markdown`, คอมเมนต์ และข้อความผู้ใช้บางส่วน ทุก locale มีชุด placeholder ครบถ้วนเหมือน notebook ภาษาญี่ปุ่นที่ปรับแต่งแล้ว

Notebook ที่สร้างจะถูก commit เพื่อให้ลิงก์ Colab คงที่

## Build

```bash
python scripts/build_readmes.py
python scripts/build_notebooks.py
```

## อัปเดตคำแปล

`translate_full_locales.py` เป็นเครื่องมือบำรุงรักษาที่อัปเดต locale อื่นจากภาษาอังกฤษ โดยรักษา code token, model identifier และการตั้งค่า Colab ควรตรวจทานคำแปลก่อน release อย่างเป็นทางการ

## การตรวจสอบ

```bash
python scripts/check_notebooks.py
```

CI สร้าง README/notebook ใหม่และตรวจ diff, Notebook JSON, ไวยากรณ์ Python, placeholder ที่ยังไม่แทน, output ที่บันทึกไว้, secret ที่เห็นชัด และความสอดคล้องของ artefact ทั้ง 30 ภาษา

## สิ่งที่ CI ตรวจสอบได้

Repository นี้ตรวจ notebook ในฐานะ artefact สำหรับแจกจ่ายได้ดังนี้:

- สร้างแบบ deterministic จาก template และ locale
- ความถูกต้องของ Notebook JSON
- execution output ว่าง
- ไวยากรณ์ Python ใน code cell
- ไม่มี placeholder ที่ยังไม่แทน
- ไม่มี secret ที่หลุดมาอย่างเห็นได้ชัด
- README/notebook ที่ commit ตรงกับ source

เส้นทางถอดเสียงเต็มรูปแบบต้องใช้ API เฉพาะ Colab, การดาวน์โหลดโมเดล, GPU ที่พร้อมใช้งาน และไฟล์สื่อของผู้ใช้ ดังนั้นการตรวจ GPU end-to-end ยังคงเป็น UAT แบบ manual เส้นทางภาษาญี่ปุ่นได้รับการตรวจด้วยเสียงยาวจริงบน Google Colab แล้ว

## สัญญาอนุญาต

Notebook scaffolding และ build script ของ repository นี้เผยแพร่ภายใต้ MIT License ส่วน Qwen3-ASR, น้ำหนักโมเดล และ dependency ภายนอกอยู่ภายใต้ license ของแต่ละรายการ
