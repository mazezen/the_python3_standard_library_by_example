#!/usr/bin/env python3
# encoding: utf-8

from itertools import *

r1 = range(3)
r2 = range(2)

print('zip stops early:')
print('list(zip(r1, r2))')

r1 = range(3)
r2 = range(2)

print('\nzip_longest process all of the values:')
print(list(zip_longest(r1, r2)))