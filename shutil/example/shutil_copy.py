#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import glob
import os
import shutil

os.mkdir('example')
print('BEFORE:', glob.glob('example/*'))

shutil.copy('shutil_copy.py', 'example')

print('AFTER:', glob.glob('example/*'))


