#!/usr/bin/env python
#------------------------------
# Comprehension Syntax
#------------------------------
'''
Produced one series of values based on 
processing of another series
Syntax List in square bracket
[ expression for value in iterable if condition ]
'''

c="""
##########################################################
## List comprehension
### odd number only with using if condition
num_squares = [v * v for v in range(1, 11) if v%2 != 0]
print(num_squares)
"""
print(c)
num_squares = [v * v for v in range(1, 11) if v%2 != 0]
print(num_squares)
print()
d="""
##########################################################
## Normal way
num_squares=[]
for v in range(1, 11):
    if v%2 != 0:
        num_squares += [v * v]
print(num_squares)
"""
print(d)
num_squares=[]
for v in range(1, 11):
    if v%2 != 0:
        num_squares += [v * v]
print(num_squares)

