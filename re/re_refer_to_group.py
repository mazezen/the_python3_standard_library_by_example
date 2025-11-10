#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import re

address = re.compile(
    r'''
    # The regular name
    (\w+) # First name
    \s+
    (([\w.]+)\s+)? # Optional middle name or initial
    (\w+) # Last name
    \s+
    <
    # The address: first_name.last_name@domain.tld
    (?P<email>
    \1 # First name
    \.
    \4 # Last name
    @
    ([\w\d.]+\.)+ # Domain name prefix
    (com|org|edu) # Limit the allowed top-level domains.
    )
    >
    ''',
    re.VERBOSE | re.IGNORECASE)

candidates = [
    u'First Last <first.last@example.com>',
    u'Different Name <first.last@example.com>',
    u'First Middle Last <first.last@example.com>',
    u'First M. Last <first.last@example.com>',
]

for candidate in candidates:
    print('Candidate: ', candidate)
    match = address.search(candidate)
    if match:
        print(' Match name :', match.group(1), match.group(4))
        print(' Match email :', match.group(5))
    else:
        print(' No match')