#!/usr/bin/env python3
# encoding: utf-8

import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('Representation:', bob)
print('Filds:', bob._fields)