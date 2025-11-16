#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import io

# Write to a buffer.
output = io.BytesIO()
wrapper = io.TextIOWrapper(
    output,
    encoding='utf-8',
    write_through=True,
)

wrapper.write('This goes into the buffer.')
wrapper.write('ACE')

# Retrieve the value written.
print(output.getvalue())

output.close()

# Initialize a read buffer.
input = io.BytesIO(
    b'Initial value for read buffer with uncode characters ' + 
    'ACE'.encode('utf-8')
)

wrapper = io.TextIOWrapper(input, encoding='utf-8')

# Read from the buffer.
print(wrapper.read())

