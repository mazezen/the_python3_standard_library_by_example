#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import glob
for name in sorted(glob.glob('dir/*')):
    print(name)
