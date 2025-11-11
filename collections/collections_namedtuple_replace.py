#!/usr/bin/env python3
# encoding: utf-8

import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('\nBefore:', bob)
bob2 = bob._replace(name='Rebort')
print('After:', bob2)
print('Same?:', bob is bob2)
