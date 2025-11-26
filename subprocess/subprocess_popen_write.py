#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import subprocess

print('write:')
proc = subprocess.Popen(
    ['cat', '-'],
    stdin = subprocess.PIPE,
)
proc.communicate('stdin: to stdin\n'.encode('utf-8'))
