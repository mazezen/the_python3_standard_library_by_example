#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

from urllib import request

response = request.urlopen("https://www.baidu.com")
print('Response: ', response)
print('URL:', response.geturl())

headers = response.info()
print('DATE:', headers['date'])
print('HEADERS :')
print('---------')

print(headers)

data = response.read().decode('utf-8')
print('LENGTH: ', len(data))
print('DATA :')
print('---------')

print(data)
