#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import dbm

with dbm.open('/tmp/example.db', 'n') as db:
    db['key'] = 'value'
    db['today'] = 'Sunday'
    db['author'] = 'Doug'
