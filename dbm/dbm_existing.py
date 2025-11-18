#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import dbm

with dbm.open('/tmp/example.db', 'r') as db:
    print('keys(): ', db.keys())
    
    for k in db.keys():
        print('key: ', k)
        print('iterating: ', k, db[k])
    print('db["author"] = ', db["author"])
