#!/usr/bin/env python

print("### Capture groups ###")

import re

date_data = '13/Feb/2020 new release'
date_pattern = re.compile(r'(\d+)/([a-zA-Z]+)/(\d{4})')
result = date_pattern.match(date_data)
a="""
# index 0 = 13/Feb/2020
# index 1 = 13
# index 2 = Feb
# index 3 = 2020
"""
print(a)

for x in range(0, 4):
    print(result.group(x))

print(result.groups())

day, month, year = result.groups()
print("Today's day is: ", day)
