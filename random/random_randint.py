#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import random

print('[1, 100]:', end=' ')
for i in range(3):
    print(random.randint(1, 100), end=' ')

print('\n[-5, 5]:', end=' ')
for i in range(3):
    print(random.randint(-5, 5), end=' ')
print()
