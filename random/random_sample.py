#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import random

with open('/usr/share/dict/words', 'rt') as f:
    words = f.readlines()

words = [w.rstrip() for w in words]

for w in random.sample(words, 5):
    print(w)
