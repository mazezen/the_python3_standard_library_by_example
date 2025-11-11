#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import difflib
from difflib_data import text1, text2

d = difflib.Differ()
diff = d.compare(a=text1, b=text2)
print(''.join(diff))
