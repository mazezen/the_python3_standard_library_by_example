#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import fractions

for s in ['1/2', '2/4', '3/6']:
    f = fractions.Fraction(s)
    print('{} = {}'.format(s, f))
