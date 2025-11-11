#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import collections

print('From the right: ')
d = collections.deque('abcdefg')
while True:
    try:
        print(d.pop(), end='')
    except IndexError:
        break
print

print('\nFrom the left:')
d2 = collections.deque(range(6))
while True:
    try:
        print(d2.popleft(), end='')
    except IndexError:
        break
print
