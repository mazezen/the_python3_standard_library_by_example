#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import re

twitter = re.compile(
    '''
    # A twitter handle: @username
    (?<=@)
    ([\w\d_]+) # Username
    ''',
    re.VERBOSE)

text = '''This text includes two Twitter handles.
One for @ThePSF, and one for the auhor, @doughellmann. 
'''

print(text)
for match in twitter.findall(text):
    print('Handle:', match)
