#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import os.path

PATHS = [
    '/one/two/three',
    '/one/two/three',
    '/',
    '.',
    '',
]

for path in PATHS:
    print('{!r:>17} : {!r}'.format(path, os.path.basename(path)))
