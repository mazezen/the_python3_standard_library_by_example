#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import dbm

with dbm.open('/tmp/example.db', 'w') as db:
    try:
        db['one'] = 1
    except TypeError as err:
        print(err)
