#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

from urllib.parse import urlencode

query_args = {
    'q': 'query string',
    'for': 'bar',
}
encoded_args = urlencode(query_args)
print(encoded_args)
