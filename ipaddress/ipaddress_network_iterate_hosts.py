#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import ipaddress

ADDRESSS = [
    '10.9.0.0/24',
    'fdfd:87b5:b475:5e3e::/64',
]


for n in ADDRESSS:
    net = ipaddress.ip_network(n)
    print('{!r}'.format(net))
    for i, ip in zip(range(3), net.hosts()):
        print(ip)
    print()
