#!/usr/bin/env python3
# encoding: utf-8

from itertools import *

def should_take(x):
    print('Testing: ',x)
    return x < 2

for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)
