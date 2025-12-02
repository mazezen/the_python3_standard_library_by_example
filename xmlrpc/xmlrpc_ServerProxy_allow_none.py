#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://localhost:9000', allow_none=False)

try:
    server.show_type(None)
except TypeError as err:
    print('ERROR: ', err)

server = xmlrpc.client.ServerProxy('http://localhost:9000',
                                   allow_none=True)
print('Allowed:', server.show_type(None))
