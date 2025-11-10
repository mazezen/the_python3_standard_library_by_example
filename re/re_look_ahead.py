#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import re
address = re.compile(
    '''
    # A name is made up of letters, and may include "."
    # for title abbreviations and middle initials.
    ((?P<name>
    ([\w.,]+\s+)*[\w.,]+
    )
    \s+
    ) # The name is no longer optional.
    # LOOKAHEAD
    # Email addresses are wrapped in angle brackets, but only
    # if both are present or neither is.
    (?= (<.*>$) # Remainder wrapped in angle brackets
    |
    ([^<].*[^>]$) # Remainder *not* wrapped in angle brackets
    )
    <? # Optional opening angle bracket
    # The address itself: username@domain.tld
    (?P<email>
    [\w\d.+-]+ # Username
    @
    ([\w\d.]+\.)+ # Domain name prefix
    (com|org|edu) # Limit the allowed top-level domains.
    )
    >? # Optional closing angle bracket
    ''',
    re.VERBOSE)

candidates = [
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'Open Bracket <first.last@example.com',
    u'Close Bracket first.last@example.com>',
] 

for condidate in candidates:
    print('Candidate: ', condidate)
    match = address.search(condidate)
    if match:
        print(' Name :', match.groupdict()['name'])
        print(' Email :', match.groupdict()['email'])
    else:
        print(' No match')
