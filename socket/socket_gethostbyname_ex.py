#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import socket

HOSTS = [
    'apu',
    'pymotw.com',
    'www.python.org',
    'nosuchname',
]

for host in HOSTS:
    print(host)
    try:
        name, aliases, address = socket.gethostbyname_ex(host)
        print('hostname: ', host)
        print('aliases: ', aliases)
        print('address: ', address)
    except socket.error as msg:
        print('error: ', msg)
    print()
