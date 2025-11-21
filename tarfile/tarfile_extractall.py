#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import tarfile
import os

os.mkdir('outdir')
with tarfile.open('example.tar', 'r') as t:
    t.extractall('outdir')
print(os.listdir('outdir'))
