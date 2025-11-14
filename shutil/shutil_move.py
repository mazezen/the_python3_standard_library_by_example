#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import glob
import shutil

with open('/file_to_change.txt', 'wt') as f:
    f.write('contentx')

print('BEFORE: ', glob.glob('example*'))
shutil.move('example.txt', 'example.out')

print('AFTER: ', glob.glob('example*'))
