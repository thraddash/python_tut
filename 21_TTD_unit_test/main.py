#!/usr/bin/env python

#########################
# Unit Test
#########################

from mspack import msmath
from mspack import msstring
a="""
print("Sum: ", msmath.sum(10, 20))
print("Division: ", msmath.division(25, 5))
print("Full Name: ", msstring.MsName("Rob", "Jones").full_name())
"""
print(a)

print("Sum: ", msmath.sum(10, 20))
print("Division: ", msmath.division(25, 5))
print("Full Name: ", msstring.MsName("Rob", "Jones").full_name())

