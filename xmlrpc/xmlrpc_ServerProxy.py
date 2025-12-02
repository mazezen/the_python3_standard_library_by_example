#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://localhost:9000')
print('Ping:', server.ping())
