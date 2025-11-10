#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import re

address = re.compile(
    '''
    [\w\d.+-]+ # Username
    @
    ([\w\d.]+\.)+ # Domain name prefix
    (com|org|edu) # TODO: support more top-level domains
    ''',
    re.VERBOSE
)

condidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
]

for candidate in condidates:
    match = address.search(candidate)
    print('{:<30} {}'.format(
        candidate, 'Matches' if match else 'No match'
    ))
