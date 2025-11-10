#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#


import re

bold = re.compile(pattern=r'\*{2}(.*?)\*{2}')


text = 'Make this **bold**. This **too**.'
print('Text:', text)
print('Bold: ', bold.sub(r'<b>\1</b>', text, count=1))
print('Bold: ', bold.sub(r'<b>\1</b>', text, count=2))
