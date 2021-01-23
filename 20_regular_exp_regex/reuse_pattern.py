#!/usr/bin/env python
print("### compiling pattern for reuse ###")
import re

date_data = '13/Feb/2019 new movie release'
date_pattern = re.compile(r'\d+/[a-zA-Z]+/\d{4}')

if date_pattern.match(date_data):
    print("Matched")
else:
    print("Mismatched")
