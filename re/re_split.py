#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import re

text = '''Paragraph one
on two lines.

Paragraph two.

Paragraph three.'''

print('With findall.')
for num, para in enumerate(re.findall(r'(.+?)(\n{2,}|$)',
                                      text,
                                      flags=re.DOTALL)):
    print(num, repr(para))
    print()
print()
print('With split:')

for num, para in enumerate(re.split(r'\n{2,}', text)):
    print(num, repr(para))
    print()