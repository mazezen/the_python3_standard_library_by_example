#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import tempfile

tempfile.tempdir = '/I/changed/this/path'
print('gettempdir():', tempfile.gettempdir())
