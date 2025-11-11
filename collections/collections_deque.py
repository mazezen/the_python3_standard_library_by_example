#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import collections

d = collections.deque('abcdefg')
print('Deque: ', d)
print('Length: ', len(d))
print('Left end: ', d[0])
print('Right end: ', d[-1])

d.remove('c')
print('remove(c): ', d)
