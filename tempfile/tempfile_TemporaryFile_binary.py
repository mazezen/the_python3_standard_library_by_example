#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import os
import tempfile

with tempfile.TemporaryFile() as temp:
    temp.write(b'Some data')

    temp.seek(0)
    print(temp.read())
