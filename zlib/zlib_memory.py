#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import zlib
import binascii

original_data = b'This is the original text.'
print('Original  :', len(original_data), original_data)

compressed = zlib.compress(original_data)
print('Compressed :', len(compressed), binascii.hexlify(compressed))
