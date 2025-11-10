#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

from re_test_patterns import test_patterns

test_patterns(
    'This is some text -- with punctuation',
    [('[^-.]+', 'sequences without -, ., or space')],
)
