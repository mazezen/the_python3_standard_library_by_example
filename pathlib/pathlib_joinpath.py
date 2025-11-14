#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import pathlib

root = pathlib.PurePosixPath('/')
subdirs = ['usr', 'local']
usr_lcoal = root.joinpath(*subdirs)
print(usr_lcoal)
