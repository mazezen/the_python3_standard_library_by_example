#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

from http import cookies

c = cookies.SimpleCookie()
c['mycookie'] = 'cookie_value'
print(c)
