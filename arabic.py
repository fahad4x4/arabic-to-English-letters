#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

# قائمة الحروف العربية والحروف المقابلة لها بالأبجدية الإنجليزية
ARABIC_TO_ENGLISH = {
    'ا': 'a', 'أ': 'a', 'إ': 'a', 'آ': 'a', 'ب': 'b', 'ت': 't', 'ث': 'th', 'ج': 'j',
    'ح': 'h', 'خ': 'kh', 'د': 'd', 'ذ': 'th', 'ر': 'r', 'ز': 'z', 'س': 's', 'ش': 'sh',
    'ص': 's', 'ض': 'd', 'ط': 't', 'ظ': 'z', 'ع': 'aa', 'غ': 'gh', 'ف': 'f', 'ق': 'q',
    'ك': 'k', 'ل': 'l', 'م': 'm', 'ن': 'n', 'ه': 'h', 'ة': 'h', 'و': 'w', 'ي': 'y'
}

# تعويض الحروف العربية بالحروف المقابلة لها بالأبجدية الإنجليزية
def replace_arabic_with_english(text):
    for arabic, english in ARABIC_TO_ENGLISH.items():
        text = text.replace(arabic, english)
    return text

# تحديث اسم الملف
def rename_file(file_path, new_file_path):
    os.rename(file_path, new_file_path)

# تحديث اسم جميع الملفات داخل المجلد الحالي
def rename_files_in_directory(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.mp3'):
            # حذف الأرقام والأحرف اللاتينية
            new_file_name = re.sub(r'\d+|[a-zA-Z]+', '', file_name)
            new_file_name = replace_arabic_with_english(new_file_name.lower()) + '.mp3'
            new_file_path = os.path.join(directory, new_file_name)
            if file_path != new_file_path:
                rename_file(file_path, new_file_path)

# التأكد من وجود المجلد الحالي وتحديث أسماء الملفات
if __name__ == '__main__':
    current_directory = os.path.dirname(os.path.abspath(__file__))
    rename_files_in_directory(current_directory)
    print("Conversion completed successfully!")
    print("Script by Fahad ALGhathbar")
