#!/usr/bin/env python

## Read a binary data file
with open('binary', 'rb') as fobj:
    binary_data = fobj.read()
    decoded_data = binary_data.decode('utf-8')
    print(decoded_data)
