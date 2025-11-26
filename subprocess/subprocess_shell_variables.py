#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import subprocess

completed = subprocess.run('echo $HOME', shell=True)
print('returncode:', completed.returncode)
