#!/usr/bin/env python3
# encoding: utf-8

from itertools import *

for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print(i, end=' ')
print()
