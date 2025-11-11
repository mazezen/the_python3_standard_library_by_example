#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import collections

c = collections.Counter()
print('Initial: ', c)

c.update('abcdaab')
print('Sequence: ', c)

c.update({'a': 1, 'd': 5})
print('Dict :', c)
