#!/usr/bin/env python

## Raw string

import re

date_data = '13/Feb/2020 \nnew release'

a="""
# r'\d+/[a-zA-Z]+/\d{4}' Raw String doesn't interpret \\n escape char 
# use r to remove escape
# use repr to keep escape

date_data = '13/Feb/2020 \\nnew release'
"""
print(a)

if re.match('\\d+/[a-zA-Z]+/\\d{4}', date_data):
    print("Matched")
else:
    print("Mismatched")

print(" ## repr ##")
print(repr(date_data))
