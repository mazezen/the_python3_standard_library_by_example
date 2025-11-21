#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import bz2
import contextlib

with bz2.BZ2File('example.bz2', 'rb') as input:
    print('Entire file:')
    all_data = input.read()
    print(all_data)

    expected = all_data[5:15]

    # Rewind to beginning
    input.seek(0)

    # Move ahead 5 bytes
    input.seek(5)
    print('Starting at position 5 for 10 bytes:')
    partial = input.read(10)
    print(partial)

    print()
    print(expected == partial)
