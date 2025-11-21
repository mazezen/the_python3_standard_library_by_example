#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import zipfile

with zipfile.ZipFile('example.zip', 'r') as zf:
    print(zf.namelist())
