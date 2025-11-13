#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import os.path

PATHS = [
    'filename.txt',
    'filename',
    '/path/to/filename.txt',
    '/',
    '',
    'my-archive.tar.gz',
    'no-extension.',
]

for path in PATHS:
    print('{!r:>2} : {!r}'.format(path, os.path.splitext(path)))
