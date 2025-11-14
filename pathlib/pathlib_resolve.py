#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import pathlib

usr_local = pathlib.Path('/usr/local')
share = usr_local / '..' / 'share'
print(share.resolve())
