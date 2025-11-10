#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2011 Doug Hellmann All rights reserved.
#

import re

def test_patterns(text, patterns):
    """
    Given source text and a list of patterns, look for
    matched for each pattern within the text and print 
    them to stdoout.
    """
    # Loog fro each pattern in the text and print the results.
    for pattern, desc in patterns:
        print('{!r} ({})\n'.format(pattern, desc))
        print(' {!r}'.format(text))
        for match in re.finditer(pattern=pattern, string=text):
            s = match.start()
            e = match.end()
            prefix = ' ' * (s)
            print(
                ' {}{!r}{} '.format(prefix,
                text[s:e],
                ' ' * (len(text) - e)),
                end=' ',
            )
            print(match.groups())
            if match.groupdict():
                print('{}{}'.format(
                    ' ' * (len(text) - s),
                    match.groupdict()),
                )
        print()
    return
