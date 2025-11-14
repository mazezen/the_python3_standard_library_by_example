#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import pathlib
import time

p = pathlib.Path('touched')
if p.exists():
    print('already exists')
else:
    print('creating new ')

p.touch()
start = p.stat()

time.sleep(2)
end = p.stat()

print('Start: ', time.ctime(start.st_mtime()))
print('End: ', time.ctime(end.st_mtime()))