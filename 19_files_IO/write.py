#!/usr/bin/env python

a="""
####################################################
# Write text in a file , add mode in 2nd parameter
w = write # erase existing content if any
a = append
r = read # default

OR

wt = write
at = append
rt = read
t is for text mode which is st by default
###########################################
with open('number.txt', 'w') as fobj:
    fobj.write('1')
    fobj.write('\\n')
    fobj.write('22211\\n')
###########################################
OUTPUT:
1
22211
"""
print(a)

with open('number.txt', 'w') as fobj:
    fobj.write('1')
    fobj.write('\n')
    fobj.write('22211\n')
