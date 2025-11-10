#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.findall(pattern=pattern, string=text):
    print('Found {!r}'.format(match))