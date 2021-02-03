#!/usr/bin/env python

a ="""
re.sub() replaces matches found in a string
##########################################################
3 parameters
regex - regular expression pattern
rep1 - the string replacement
string - the string to replace

txt  = "I love Python, because Python is fun to learn"
res  re.sub("Python", "Nodejs", txt)
##########################################################
"""

import re

txt  = "I love Python, because Python is fun to learn"
res = re.sub("Python", "Nodejs", txt)
print(a)
print(res)

