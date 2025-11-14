#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import tempfile

with tempfile.SpooledTemporaryFile(max_size=1000, mode='w+t',
                                   encoding='utf-8') as temp:
    print('temp: {!r}'.format(temp))

    for i in range(3):
        temp.write('This line is repeated over and over.\n')
        print(temp.rolled, temp._file)
    print('rolling over')
    temp.rollover()
    print(temp.rolled, temp._file)
