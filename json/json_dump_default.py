#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import json
import json_myobj

obi = json_myobj.MyObj('instance value goes here')

print('First attempt')
try:
    print(json.dumps(obi))
except TypeError as err:
    print('ERROR: ', err)

def convert_to_builtin_type(obj):
    print('default(', repr(obj), ')')

    d = {
        '__class__': obj.__class__.__name__,
        '__module__': obj.__module__,
    }

    d.update(obj.__dict__)
    return d

print()
print('With default')
print(json.dumps(obi, default=convert_to_builtin_type))
