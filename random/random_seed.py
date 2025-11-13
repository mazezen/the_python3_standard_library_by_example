#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import random
random.seed(100)

for i in range(5):
    print('{:04.3f}'.format(random.random()), end=' ')
print()
