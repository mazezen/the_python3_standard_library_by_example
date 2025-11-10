#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import re

address = re.compile(
    '''
    ^
    # A name is made up of letters, and may include "."
    # for title abbreviations and middle initials.
    (?P<name>
    ([\w.]+\s+)*[\w.]+
    )?
    \s*
    # Email addresses are wrapped in angle brackets, but
    # only if a name is found.
    (?(name)
    # Remainder wrapped in angle brackets because
    # there is a name
    (?P<brackets>(?=(<.*>$)))
    |
    # Remainder does not include angle brackets without name
    (?=([^<].*[^>]$))
    )
    # Look for a bracket only if the look-ahead assertion
    # found both of them.
    (?(brackets)<|\s*)
    # The address itself: username@domain.tld
    (?P<email>
    [\w\d.+-]+ # Username
    @
    ([\w\d.]+\.)+ # Domain name prefix
    (com|org|edu) # Limit the allowed top-level domains.
    )
    # Look for a bracket only if the look-ahead assertion
    # found both of them.
    (?(brackets)>|\s*)
    $
    ''',
    re.VERBOSE)

candidates = [
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'Open Bracket <first.last@example.com',
    u'Close Bracket first.last@example.com>',
    u'no.brackets@example.com',
]

for candidate in candidates:
    print('Candidate: ', candidate)
    match = address.search(candidate)
    if match:
        print(' Match name :', match.groupdict()['name'])
        print(' Match email:', match.groupdict()['email'])
    else:
        print(' No match')