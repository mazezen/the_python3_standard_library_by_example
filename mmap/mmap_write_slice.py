#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import mmap
import shutil

# Copy the example file.
shutil.copyfile('lorem.txt', 'lorem_copy.txt')

word = b'consectetuer'

reversed = word[::-1]
print('Looking for  :', word)
print('Replcing with :', reversed)

with open('lorem_copy.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0) as m:
        print('Before:\n{}'.format(m.readline().rstrip()))
        m.seek(0)  # Rewind

        loc = m.find(word)
        m[loc:loc + len(word)] = reversed

        m.seek(0)
        print('After :\n{}'.format(m.readline().rstrip()))

        f.seek(0)
        print('File :\n{}'.format(f.readline().rstrip()))
