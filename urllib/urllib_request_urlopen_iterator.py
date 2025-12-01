#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

from urllib import request

response = request.urlopen('https://www.baidu.com')
for line in response:
    print(line.decode('utf-8').rstrip())
