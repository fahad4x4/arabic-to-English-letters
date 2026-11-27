# arabic-to-English-letters

> Rename MP3 files with Arabic names to the same names written in English (Latin) letters.

[English](#english) | [العربية](#arabic)

![Python](https://img.shields.io/badge/python-3-blue?logo=python&logoColor=white)
![License: GPL v3](https://img.shields.io/badge/license-GPLv3-blue)

---

<a id="english"></a>

## English

### Overview

`arabic.py` is a small Python 3 script that goes through a folder and renames every `.mp3` file whose name contains Arabic characters, replacing each Arabic letter with its Latin-letter equivalent. It is handy for music players, car stereos, and devices that cannot display Arabic file names.

> **Warning:** the script renames files **in place**. Back up your folder before running it.

### Features

- Transliterates Arabic letters to Latin letters (e.g. `ش` → `sh`, `خ` → `kh`, `ع` → `aa`).
- Converts Arabic-Indic digits (`٠`–`٩`) to `0`–`9`.
- Strips Arabic diacritics (tashkeel) and tatweel (`ـ`).
- Keeps Western digits, Latin letters, spaces, and the file extension unchanged.
- Processes `.mp3` files in any letter case (e.g. `.MP3`); the renamed file gets a lowercase `.mp3` extension.
- Never overwrites an existing file: if the new name is taken, `_2`, `_3`, … is appended.
- Skips files whose name would not change, and prints each rename plus a final count.
- Accepts an optional folder path; by default it works in the folder where `arabic.py` is located.

### Requirements

- Python 3 (standard library only, no extra packages).

### Installation

```bash
git clone https://github.com/fahad4x4/arabic-to-English-letters.git
cd arabic-to-English-letters
```

### Usage

```bash
# Rename the MP3 files in a specific folder
python3 arabic.py /path/to/folder

# Or rename the MP3 files in the same folder as arabic.py
python3 arabic.py
```

Example output:

```text
01 الفاتحة.mp3  ->  01 alfathh.mp3
02 البَقَرَة.MP3  ->  02 albqrh.mp3
Conversion completed successfully! (2 files renamed)
Script by Fahad ALGhathbar
```

If `01 alfathh.mp3` already existed, the new file would be named `01 alfathh_2.mp3`.

### Project structure

```text
arabic-to-English-letters/
├── arabic.py    # the renaming script
├── LICENSE      # GNU GPL v3
└── README.md
```

### License

Released under the GNU General Public License v3.0. See [LICENSE](LICENSE).

### Author

**Fahad ALGhathbar** — GitHub: [@fahad4x4](https://github.com/fahad4x4)

Special thanks to Eng. Fahad Al-Duraibi ([@fduraibi](https://github.com/fduraibi)) — see the original discussion at <https://aosus.org/t/topic/188>.

---

<a id="arabic"></a>

<div dir="rtl">

## العربية

### نظرة عامة

`arabic.py` سكربت صغير بلغة Python 3 يمرّ على ملفات مجلد معيّن، ويعيد تسمية كل ملف `.mp3` يحتوي اسمه على حروف عربية، بحيث يُستبدل كل حرف عربي بما يقابله من الحروف اللاتينية (الإنجليزية). وهو مفيد لمشغلات الصوت وأنظمة السيارات والأجهزة التي لا تعرض أسماء الملفات العربية.

> **تنبيه:** يعيد السكربت تسمية الملفات **في مكانها مباشرة**، لذا احتفظ بنسخة احتياطية من المجلد قبل التشغيل.

### المزايا

- تحويل الحروف العربية إلى حروف لاتينية (مثل `ش` ← `sh`، و`خ` ← `kh`، و`ع` ← `aa`).
- تحويل الأرقام العربية الهندية (`٠`–`٩`) إلى `0`–`9`.
- حذف التشكيل وحرف التطويل (`ـ`).
- الإبقاء على الأرقام والحروف الإنجليزية والمسافات وامتداد الملف كما هي.
- معالجة ملفات `.mp3` بأي حالة أحرف (مثل `.MP3`)، ويُحفظ الملف الجديد بامتداد `.mp3` بأحرف صغيرة.
- عدم الكتابة فوق أي ملف موجود: إذا كان الاسم الجديد مستخدمًا تُضاف اللاحقة `_2` أو `_3` وهكذا.
- تجاهل الملفات التي لن يتغير اسمها، مع طباعة كل عملية إعادة تسمية وعدد الملفات في النهاية.
- يقبل مسار مجلد اختياريًا، وإذا لم يُحدَّد يعمل على المجلد الموجود فيه `arabic.py`.

### المتطلبات

- Python 3 (المكتبة القياسية فقط، دون حزم إضافية).

### التثبيت

```bash
git clone https://github.com/fahad4x4/arabic-to-English-letters.git
cd arabic-to-English-letters
```

### طريقة الاستخدام

```bash
# إعادة تسمية ملفات MP3 في مجلد محدد
python3 arabic.py /path/to/folder

# أو إعادة تسمية ملفات MP3 الموجودة في نفس مجلد السكربت
python3 arabic.py
```

مثال على المخرجات:

```text
01 الفاتحة.mp3  ->  01 alfathh.mp3
02 البَقَرَة.MP3  ->  02 albqrh.mp3
Conversion completed successfully! (2 files renamed)
Script by Fahad ALGhathbar
```

ولو كان الملف `01 alfathh.mp3` موجودًا مسبقًا، فسيُسمّى الملف الجديد `01 alfathh_2.mp3`.

### هيكل المشروع

```text
arabic-to-English-letters/
├── arabic.py    # سكربت إعادة التسمية
├── LICENSE      # رخصة GNU GPL v3
└── README.md
```

### الرخصة

المشروع منشور بموجب رخصة GNU العمومية العامة، الإصدار 3.0. راجع ملف [LICENSE](LICENSE).

### المؤلف

**فهد الغثبر** — حساب GitHub: [@fahad4x4](https://github.com/fahad4x4)

شكر خاص للمهندس فهد الدريبي ([@fduraibi](https://github.com/fduraibi))، ويمكن الاطلاع على النقاش الأصلي عبر <https://aosus.org/t/topic/188>.

</div>
