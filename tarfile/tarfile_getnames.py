#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import tarfile

with tarfile.open('example.tat', 'r') as t:
    print(t.getnames())
