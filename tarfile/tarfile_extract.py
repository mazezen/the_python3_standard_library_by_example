#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import tarfile
import os

os.mkdir('outdir')
with tarfile.open('example.tar', 'r') as t:
    t.extract('README.txt', 'outdir')
print(os.listdir('outdir'))
