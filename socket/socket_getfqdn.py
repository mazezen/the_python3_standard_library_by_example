#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import socket

for host in ['apu', 'pymotw.com', "mazezen.gitub.io"]:
    print('{:>10} : {}'.format(host, socket.getfqdn(host)))
