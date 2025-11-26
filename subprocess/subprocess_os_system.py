#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import subprocess

completed = subprocess.run(['ls', '-1'])
print('returncode:', completed.returncode)
