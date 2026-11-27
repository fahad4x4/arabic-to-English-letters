#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rename .mp3 files with Arabic names to the same names written in English letters.
تحويل أسماء ملفات mp3 العربية إلى أسماء بحروف إنجليزية.

Script by Fahad ALGhathbar
"""
import os
import re
import sys

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


def unique_path(path):
    """إذا الاسم موجود، أضف رقم بدل ما نكتب فوق ملف ثاني."""
    if not os.path.exists(path):
        return path
    base, ext = os.path.splitext(path)
    n = 2
    while os.path.exists(f"{base}_{n}{ext}"):
        n += 1
    return f"{base}_{n}{ext}"


def rename_files_in_directory(directory):
    """تحديث اسم جميع ملفات mp3 داخل المجلد. ترجع عدد الملفات المعدلة."""
    renamed = 0
    for file_name in sorted(os.listdir(directory)):
        file_path = os.path.join(directory, file_name)
        stem, ext = os.path.splitext(file_name)
        if not os.path.isfile(file_path) or ext.lower() != '.mp3':
            continue
        # نحافظ على الأرقام والحروف الإنجليزية والامتداد كما هي
        new_stem = replace_arabic_with_english(stem).strip()
        if not new_stem or new_stem == stem:
            continue
        new_path = unique_path(os.path.join(directory, new_stem + ext.lower()))
        os.rename(file_path, new_path)
        print(f"{file_name}  ->  {os.path.basename(new_path)}")
        renamed += 1
    return renamed


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    count = rename_files_in_directory(target)
    print(f"Conversion completed successfully! ({count} files renamed)")
    print("Script by Fahad ALGhathbar")
