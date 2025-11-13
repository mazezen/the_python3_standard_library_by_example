#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import os.path

paths = ['/one/two/three/four', '/one/two/threefold','/one/two/three']

for path in paths:
    print('PATH:', path)

print()
print('PREFIX:', os.path.commonpath(paths))
