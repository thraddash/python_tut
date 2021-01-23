#!/usr/bin/env python
a="""
##########################
r'\d'
12 blah 2 1
OUTPUT: 1, 2, 2, 1, 2, 1
###########################
r'\d+'
OUTPUT: 12, 2, 1, 21
##########################
"""
print(a)

import re

num = re.compile(r'\d')
list = num.findall('12 blah 2 1 21')
print(list)

num2 = re.compile(r'\d+')
list2 = num2.findall('12 blah 2 1 21')
print(list2)
