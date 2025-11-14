#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import pathlib

p = pathlib.Path('.')

for f in p.iterdir():
    print(f)