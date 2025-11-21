#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import zipfile

with zipfile.ZipFile('example.zip') as zf:
    for filename in ['README.txt', 'nothere.txt']:
        try:
            data = zf.read(filename)
        except KeyError:
            print('ERROR: Did not find {} in zip file'.format(
                filename))
        else:
            print(filename, ":")
            print(data)
        print()