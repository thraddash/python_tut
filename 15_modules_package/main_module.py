#!/usr/bin/env python

# ------------------
# Import 
# ------------------

# Import entire module
import mymath
print("# import mymath")
print(mymath.sum(10, 2))
print(mymath.subtract(10, 2))
print()
# Import module without repeating module name
'''
from mymath import sum, subtract
print(sum(10, 2))
print(subtract(10, 2))
'''
print("# from mymath import sum, subtract")
print("print(sum(10, 2))")
print("print(subtract(10, 2))")
print()

print("# from mymath import *")
