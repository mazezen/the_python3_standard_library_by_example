#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

from http import cookies
import datetime

def show_cookie(c):
    print(c)
    for key, morsel in c.items():
        print()
        print('key =', morsel.key)
        print(' value =', morsel.value)
        print(' coded_value = ', morsel.coded_value)
        for name in morsel.keys():
            if morsel[name]:
                print(' {} = {} '.format(name, morsel[name]))
    

c = cookies.SimpleCookie()

c['encoded_value_cookie'] = '"cookie,value"'
c['encoded_value_cookie']['comment'] = 'Has escaped punctuation'

c['restricted_cookie'] = 'cookie_value'
c['restricted_cookie']['path'] = '/sub/path'
c['restricted_cookie']['domain'] = 'PyMOTW'
c['restricted_cookie']['secure'] = True

c['with_max_age'] = 'expires in 5 minutes'
c['with_max_age']['max-age'] = 300 # Seconds



show_cookie(c)


