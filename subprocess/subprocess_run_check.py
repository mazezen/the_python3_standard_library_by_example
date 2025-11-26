#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import subprocess

try:
    subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as err:
    print('ERROR:', err)
