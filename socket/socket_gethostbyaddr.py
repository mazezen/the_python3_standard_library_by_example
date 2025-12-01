#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import socket

hostname, aliases, address = socket.gethostbyaddr('121.228.183.3')

print('Hostname: ', hostname)
print('Aliases: ', aliases)
print('Address: ', address)
