#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import collections

# Add to the right.
d1 = collections.deque()
print('d1 => ', d1)
d1.extend('abcdefg')
print('d1 => ', d1)
d1.append('h')
print('d1 => ', d1)

# Add to the left.
d2 = collections.deque()
d2.extendleft(range(6))
print('d2 => ', d2)
d2.appendleft(6)
print('d2 => ', d2)
