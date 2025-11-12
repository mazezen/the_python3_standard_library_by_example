#!/usr/bin/env python3
# encoding: utf-8

from operator import *

a = 1
b = 0.5

print('a = ', a)
print('b = ', b)

for func in (lt, le , eq, ne , ge, gt):
    print('{}(a, b): {}'.format(func.__name__, func(a, b)))
