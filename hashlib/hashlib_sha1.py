#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import hashlib

from hashlib_data import lorem

h = hashlib.sha1()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())
