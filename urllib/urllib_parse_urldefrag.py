#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

from urllib.parse import urldefrag

original = 'http://netloc/path;param?query=arg#frag'
print('original:', original)
d = urldefrag(original)
print('url :', d.url)
print('fragment:', d.fragment)
