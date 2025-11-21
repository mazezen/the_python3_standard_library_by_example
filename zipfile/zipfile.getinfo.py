#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import zipfile

with zipfile.ZipFile('example.zip') as zf:
    for filename in ['README.txt', 'nothere.txt']:
        try:
            info = zf.getinfo(filename)
        except KeyError:
            print('ERROR: Did not find {} in zip file'.format(
                filename))
        else:
            print('{} is {} bytes'.format(
                info.filename, info.file_size))
