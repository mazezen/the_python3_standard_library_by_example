#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import collections

c = collections.Counter('extremelly')
c['z'] = 0
print(c)
print(list(c.elements()))