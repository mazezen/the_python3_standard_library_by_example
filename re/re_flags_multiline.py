#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import re

text = 'This is some text -- with punctuation.'
pattern = r'(^\w+)|(\w+\S*$)'
single_line = re.compile(pattern=pattern)
multiline = re.compile(pattern=pattern, flags=re.MULTILINE)

print("Text:\n {!r}".format(text))
print('Pattern:\n {}'.format(pattern))
print('Single Line :')

for match in single_line.findall(text):
    print(' {!r}'.format(match))
print('Multline :')
for match in multiline.findall(text):
    print(' {!r}'.format(match))