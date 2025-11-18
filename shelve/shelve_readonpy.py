#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import dbm
import shelve

with shelve.open('test_shelf.db', flag='r') as s:
    print('Existing: ', s['key1'])
    try:
        s['key1'] = 'new value'
    except dbm.error as err:
        print('Error: {}'.format(err))
