#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import shelve

with shelve.open('test_shelf.db') as s:
    existing = s['key1']

print(existing)
