#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

from http import cookies
import textwrap

c = cookies.SimpleCookie()
c['mycookie'] = 'cookie_value'
c['another_cookie'] = 'second_value'
js_text = c.js_output()
print(textwrap.dedent(js_text).lstrip())
