#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import uuid

hostnames = ['www.doughellmann.com', 'blog.doughellmann.com']

for name in hostnames:
    print(name)
    print(' MD5 :', uuid.uuid3(uuid.NAMESPACE_DNS, name))
    print(' SHA-1 :', uuid.uuid5(uuid.NAMESPACE_DNS, name))
    print()
