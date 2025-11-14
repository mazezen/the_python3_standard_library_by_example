#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import shutil

for format, exts, description in shutil.get_unpack_formats():
    print('{:<5}: {}, names ending in {}'.format(
        format, description, exts
    ))
