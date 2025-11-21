#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import tarfile

for filename in ['README.txt', 'example.tar',
                 'bad_example.tar', 'notthere.tar']:
    try:
        print('{:>15} {}'.format(filename, tarfile.is_tarfile(
            filename
        )))
    except IOError as err:
        print('{:>15} {}'.format(filename, err))
