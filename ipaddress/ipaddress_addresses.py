#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import binascii
import ipaddress

ADDRESSS = [
    '10.9.0.6',
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
]

for ip in ADDRESSS:
    addr = ipaddress.ip_address(ip)
    print('{!r}'.format(addr))
    print(' IP version: ', addr.version)
    print(' is private:', addr.is_private)
    print(' packed form:', binascii.hexlify(addr.packed))
    print(' integer:', int(addr))
    print()