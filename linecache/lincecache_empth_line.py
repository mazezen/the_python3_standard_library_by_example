#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import linecache
from linecache_data import *

filename = make_tempfile()

# Blank lines include the newline.
print('BLANK : {!r}'.format(linecache.getline(filename, 8)))

cleanup(filename)
