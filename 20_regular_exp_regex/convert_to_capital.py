#!/usr/bin/env python
a="""
###############################################
# Capital letter of month name
# date_data = '13/Feb/2020 new movie release'
# Convert month name to all capital letter
###############################################
"""
print(a)

import re

date_data = '13/Feb/2020 new movie release'
date_pattern = re.compile(r'(\d+)/([a-zA-Z]+)/(\d{4})')

def to_upper(m):
    return f'{m.group(3)} {m.group(2).upper()} {m.group(1)}'

date_modify = date_pattern.sub(to_upper, date_data)
print("After: ", date_modify)
