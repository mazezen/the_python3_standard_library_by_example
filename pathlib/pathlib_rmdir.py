#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import pathlib

p = pathlib.Path('example_dir')

print('Removing {}'.format(p))
p.rmdir()
