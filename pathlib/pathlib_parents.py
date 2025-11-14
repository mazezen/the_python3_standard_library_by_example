#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import pathlib

p = pathlib.PurePosixPath('/usr/local/lib')

print('parent: {}'.format(p.parent))

print('\nhierarchy:')
for up in p.parents:
    print(up)
