#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

from urllib.parse import urlparse

url = 'http://netloc/path;param?query=arg#frag'

parsed = urlparse(url)
print(parsed)
