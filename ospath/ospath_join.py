#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import os.path

PATHS = [
    ('one', 'two', 'three'),
    ('/','one', 'three'),
    ('/one', '/two', '/three'),
]

for parts in PATHS:
    print('{} : {!r}'.format(parts, os.path.join(*parts)))
