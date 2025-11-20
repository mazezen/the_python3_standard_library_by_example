#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import zlib

lorem = open('lorem.txt', 'rb').read()
compressed = zlib.compress(lorem)
combined = compressed + lorem

decompressor = zlib.decompressobj()
decompressed = decompressor.decompress(combined)

decmpressed_matches = decompressed == lorem
print('Decompressed matches lorem:', decmpressed_matches)

unused_matches = decompressor.unused_data == lorem
print('Unused data matches lorem :', unused_matches)
