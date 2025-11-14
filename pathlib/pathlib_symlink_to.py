#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import pathlib

p = pathlib.Path('example_link')
p.symlink_to('index.rst')

print(p)
print(p.resolve().name)
