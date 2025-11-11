#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

bob = ('Bob', 30, 'male')
print('Representation: ', bob)

jane = ('Jane', 29, 'female')
print('\nField by index: ', jane[0])

print('\nFields by index:')
for p in [bob, jane]:
    print('{} is a {} year old {}'.format(*p))
