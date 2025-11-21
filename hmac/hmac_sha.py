#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import hmac
import hashlib

digest_maker = hmac.new(
    b'secret-shared-key-goes-there',
    b'',
    'sha1',
)

with open('hmac_sha.py', 'rb') as f:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)
digest = digest_maker.hexdigest()
print(digest)
