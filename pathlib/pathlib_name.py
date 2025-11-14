#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import pathlib

p = pathlib.PurePosixPath('./source/pathlib/pahtlib_name.py')
print('path    :{}'.format(p))
print('name : {}'.format(p.name))
print('suffix: {}'.format(p.suffix))
print('stem : {}'.format(p.stem))
