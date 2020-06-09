#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir, rename
from os.path import isfile, join

# اكمل المصفوفة بالقيم الكاملة للاستبدال
arabizi = {'ا':'A', 'ب':'B', 'ت':'T', 'ث':'TH', 'ج':'J', 'ح':'7', 'خ':'5', 'د':'d', 'د':'d', 'ذ':'4', 'د':'d', 'ر':'R', 'ز':'Z', 'س':'S', 'ش':'SH', 'ص':'9', 'د':'d', 'ض':'^9', 'د':'d', 'ط':'6', 'د':'d', 'ظ':'^6', 'د':'d', 'ع':'3', 'د':'d', 'غ':'^3', 'د':'d', 'ف':'F', 'ق':'8', 'د':'d', 'ك':'K', 'ل':'L', 'م':'M', 'ن':'N', 'ه':'H', 'ء':'2', 'د':'d', 'ي':'E', 'و':'W', 'أ':'A', 'ة':'H'}

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

# حدد المسار الذي تريد او ابقه كما هو لاستخدام المسار المحلي
filepath = "./"

for araby in listdir(filepath):
    if isfile(join(filepath, araby)):   # لعرض الملفات فقط دون المجلدات
        englized = replace_all(araby, arabizi)
        if araby != englized:
            print araby
            print englized
            rename(join(filepath, araby), join(filepath, englized))
