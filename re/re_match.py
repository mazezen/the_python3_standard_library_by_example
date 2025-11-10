#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import re

text = 'This is some text -- with punctuation.'
pattern = 'is'

print('Text   :', text)
print('Pattern:', pattern)


m = re.match(pattern=pattern, string=text)
print('Match :', m)
s = re.search(pattern=pattern, string=text)
print('Search :', s)
