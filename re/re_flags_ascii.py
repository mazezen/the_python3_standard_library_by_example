#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import re

text = u'Français łzoty Österreich'
pattern = r'\w+'
ascii_pattern = re.compile(pattern, re.ASCII)
unicode_pattern = re.compile(pattern)

print('Text :', text)
print('Pattern :', pattern)
print('ASCII :', list(ascii_pattern.findall(text)))
print('Unicode :', list(unicode_pattern.findall(text)))

