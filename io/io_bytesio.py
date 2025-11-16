#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import io

# Write to buffer.
output = io.BytesIO()
output.write('This goes into the buffer. '.encode('utf-8'))
output.write('ACE'.encode('utf-8'))

# Retrieve the value written.
print(output.getvalue())

output.close()

# Initialize a read buffer.
input = io.BytesIO(b'Inital value for read buffer')

# Read from the buffer.
print(input.read())
