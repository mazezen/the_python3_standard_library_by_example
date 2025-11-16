#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import io

# Write to a buffer.
output = io.StringIO()
output.write('This goes into the buffer.')
print('And so desc this.', file=output)

# Retrieve the value written.
print(output.getvalue())

output.close()

# Initialize a read buffer.
input = io.StringIO('Initval value for read buffer')

# Read from the buffer.
print(input.read())
