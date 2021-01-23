#!/usr/bin/env python
a="""
##################################
## Search and Replace
## Convert to 2020-Feb-13
##################################
"""
print(a)

import re

date_data = '13/Feb/2020 new movie release'

date_pattern = re.compile(r'(\d+)/([a-zA-Z]+)/(\d{4})')

print("Before: ", date_data)

date_modify = date_pattern.sub(r'\3-\2-\1', date_data)

print("After: ", date_modify)
