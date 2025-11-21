#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import zipfile

for filename in ['README.txt', 'example.zip', 'bad_example.zip', 'notthere.zip']:
    print('{:>15} {}'.format(
        filename, zipfile.is_zipfile(filename)
    ))
