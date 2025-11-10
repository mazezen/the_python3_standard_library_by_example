#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import textwrap
from textwrap_example import sample_text
dedented_text = textwrap.dedent(sample_text)
print('Dedented:')
print(dedented_text)
