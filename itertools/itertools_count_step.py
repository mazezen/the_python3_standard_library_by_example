#!/usr/bin/env python3
# encoding: utf-8

import fractions
from itertools import *

start = fractions.Fraction(1, 3)
step = fractions.Fraction(1, 3)

for i in zip(count(start=start, step=step),  ['a', 'b', 'c']):
    print('{} : {}'.format(*i))
