#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import unicodedata
from codecs_to_hex import to_hex

text = 'francais'

print('Raw   :{!r}'.format(text))

for c in text:
    print('  {!r}: {}'.format(c, unicodedata.name(c, c)))
print('UTF-8 : {!r}'.format(to_hex(text.encode('utf-8'), 1)))
print('UTF-16 : {!r}'.format(to_hex(text.encode('utf-16'), 1)))
