#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import os.path
import os

os.environ['MYVAR'] = 'VALUE'

print(os.path.expandvars('/path/to/#MYVAR'))
