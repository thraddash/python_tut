#!/usr/bin/env python

print("### Match all occurrences ###")

import re

date_data = '13/Feb/2020 test 14/Mar/2020 pass 15/Apr/2020 fail'
date_pattern = re.compile(r'\d+/[a-zA-Z]+/\d{4}')

result = date_pattern.findall(date_data)
print(result)
print("##########################################")
regex = "^13"
print(date_data)
x = re.findall(regex, date_data)
if x:
    print("string starts with 13")
else:
    print("string does not start with 13")

regex = "fail$"
x = re.findall(regex, date_data)
if x:
    print("string ends with 'fail'")
else:
    print("string does not end with 'fail'")
