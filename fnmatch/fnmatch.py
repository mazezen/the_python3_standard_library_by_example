#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import fnmatch
import os

pattern = 'fnmatch_*.py'
print('Pattern:', pattern)
print()

files = os.listdir('./fnmatch')
for name in files:
    print('Filename: {:<25} {}'.format(
        name, fnmatch.fnmatch(name, pattern)))