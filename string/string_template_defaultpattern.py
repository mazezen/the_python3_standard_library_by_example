#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import string

t = string.Template('$var')
print(t.pattern.pattern)
