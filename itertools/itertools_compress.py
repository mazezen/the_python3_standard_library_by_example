#!/usr/bin/env python3
# encoding: utf-8

from itertools import *

every_thrid = cycle([False, False, True])
data = range(1, 10)

for i in compress(data, every_thrid):
    print(i, end=' ')
print()
