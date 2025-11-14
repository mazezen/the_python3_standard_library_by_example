#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import linecache
from linecache_data import *

filename = make_tempfile()

# The cache always returns a string, and uses
# an empty string to indicate a line that does
# not exist.
not_there = linecache.getline(filename, 500)

print('NOT THERE: {!r} includes {} characters'.format(
    not_there, len(not_there)
))

cleanup(filename)
