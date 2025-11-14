#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import io
import os
import shutil
import sys

class VerbosesStringIO(io.StringIO):

    def read(self, n=-1):
        next = io.StringIO.read(self, n)
        print('read({}) got {} bytes'.format(n, len(next)))
        return next
    
lorem_ipsum = '''Lorem ipsum dolor sit amet, consectetuer
adipiscing elit. Vestibulum aliquam mollis dolor. Donec
vulputate nunc ut diam. Ut rutrum mi vel sem. Vestibulum
ante ipsum.'''

print('Default:')
input = VerbosesStringIO(lorem_ipsum)
output = io.StringIO()
shutil.copyfileobj(input, output)

print()

print('All at once:')

input = VerbosesStringIO(lorem_ipsum)
output = io.StringIO()
shutil.copyfileobj(input, output, -1)
shutil.copyfileobj(input, output, -1)

print()

print('Blocks of 256:')
input = VerbosesStringIO(lorem_ipsum)
output  = io.StringIO()
shutil.copyfileobj(input, output, 256)
