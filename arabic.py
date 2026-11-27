#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rename .mp3 files with Arabic names to the same names written in English letters.
تحويل أسماء ملفات mp3 العربية إلى أسماء بحروف إنجليزية.

Script by Fahad ALGhathbar
"""
import argparse
import os
import re

# قائمة الحروف العربية والحروف المقابلة لها بالأبجدية الإنجليزية
ARABIC_TO_ENGLISH = {
    'ا': 'a', 'أ': 'a', 'إ': 'a', 'آ': 'a', 'ء': 'a', 'ئ': 'e', 'ؤ': 'o', 'ى': 'a',
    'ب': 'b', 'ت': 't', 'ث': 'th', 'ج': 'j',
    'ح': 'h', 'خ': 'kh', 'د': 'd', 'ذ': 'th',
    'ر': 'r', 'ز': 'z', 'س': 's', 'ش': 'sh',
    'ص': 's', 'ض': 'd', 'ط': 't', 'ظ': 'z',
    'ع': 'aa', 'غ': 'gh', 'ف': 'f', 'ق': 'q',
    'ك': 'k', 'ل': 'l', 'م': 'm', 'ن': 'n',
    'ه': 'h', 'ة': 'h', 'و': 'w', 'ي': 'y',
    # أرقام عربية هندية
    '٠': '0', '١': '1', '٢': '2', '٣': '3', '٤': '4',
    '٥': '5', '٦': '6', '٧': '7', '٨': '8', '٩': '9',
}

# التشكيل والتطويل تُحذف
DIACRITICS = re.compile(r'[\u064B-\u0652\u0670\u0640]')


def replace_arabic_with_english(text):
    """تعويض الحروف العربية بالحروف المقابلة لها بالأبجدية الإنجليزية."""
    text = DIACRITICS.sub('', text)
    return ''.join(ARABIC_TO_ENGLISH.get(ch, ch) for ch in text)


def unique_path(path, reserved=()):
    """إذا الاسم موجود (أو محجوز في التجربة)، أضف رقم بدل ما نكتب فوق ملف ثاني."""
    def taken(p):
        return os.path.exists(p) or p in reserved
    if not taken(path):
        return path
    base, ext = os.path.splitext(path)
    n = 2
    while taken(f"{base}_{n}{ext}"):
        n += 1
    return f"{base}_{n}{ext}"


def rename_files_in_directory(directory, dry_run=False):
    """تحديث اسم جميع ملفات mp3 داخل المجلد. ترجع عدد الملفات المعدلة.

    مع dry_run=True تُطبع الأسماء الجديدة فقط بدون أي تغيير على الملفات.
    """
    renamed = 0
    planned = set()  # أسماء محجوزة، عشان التجربة تطابق التشغيل الفعلي
    for file_name in sorted(os.listdir(directory)):
        file_path = os.path.join(directory, file_name)
        stem, ext = os.path.splitext(file_name)
        if not os.path.isfile(file_path) or ext.lower() != '.mp3':
            continue
        # نحافظ على الأرقام والحروف الإنجليزية والامتداد كما هي
        new_stem = replace_arabic_with_english(stem).strip()
        if not new_stem or new_stem == stem:
            continue
        new_path = unique_path(os.path.join(directory, new_stem + ext.lower()), planned)
        planned.add(new_path)
        if not dry_run:
            os.rename(file_path, new_path)
        print(f"{file_name}  ->  {os.path.basename(new_path)}")
        renamed += 1
    return renamed


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Rename .mp3 files with Arabic names to English (Latin) letters.")
    parser.add_argument(
        "directory", nargs="?",
        default=os.path.dirname(os.path.abspath(__file__)),
        help="folder to process (default: the folder containing arabic.py)")
    parser.add_argument(
        "-n", "--dry-run", action="store_true",
        help="only print the planned renames; do not rename anything")
    return parser.parse_args(argv)


if __name__ == '__main__':
    args = parse_args()
    count = rename_files_in_directory(args.directory, dry_run=args.dry_run)
    if args.dry_run:
        print(f"Dry run: nothing was renamed. ({count} files would be renamed)")
    else:
        print(f"Conversion completed successfully! ({count} files renamed)")
    print("Script by Fahad ALGhathbar")
