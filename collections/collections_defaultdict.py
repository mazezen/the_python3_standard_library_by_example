#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import collections

def default_factory():
    return 'default value'

d = collections.defaultdict(default_factory, foor='bar')
print('d: ', d)
print('foo =>', d['foor'])
print('bar =>', d['bar'])
