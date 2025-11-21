#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import bz2
import binascii

original_data = b'This is the original text.'
print('Original   : {} bytes.'.format(len(original_data)))
print(original_data)

print()

comporessed = bz2.compress(original_data)
print('Compressed  : {} bytes'.format(len(comporessed)))

hex_version = binascii.hexlify(comporessed)
for i in range(len(hex_version) // 40 + 1):
    print(hex_version[i * 40:(i + 1) * 40])

print()
decompressed = bz2.decompress(comporessed)
print('Decompressed : {} bytes'.format(len(decompressed)))
print(decompressed)
