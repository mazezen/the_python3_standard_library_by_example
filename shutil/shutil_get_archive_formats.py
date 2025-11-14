#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import shutil

for format, description in shutil.get_archive_formats():
    print('{:<5}: {}'.format(format, description))
