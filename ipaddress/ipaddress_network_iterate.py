#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import ipaddress

ADDRESSS = [
    '10.9.0.6',
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
]

for n in ADDRESSS:
    net = ipaddress.ip_network(n)
    print('{!r}'.format(net))
    for i, ip in zip(range(3), net):
        print(ip)

    print()
