#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import pathlib

p = pathlib.Path('example_dir')


print('Creating {}'.format(p))
p.mkdir()
