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

a = """
#############################################
## List comprehension
num_squares = [v * v for v in range(1, 11)]
1 * 1 = 1
2 * 2 = 4
3 * 3 = 9
4 * 4 = 16
etc...
"""
print(a)
num_squares = [v * v for v in range(1, 11)]
print(num_squares)
print()
b="""
#############################################
## Normal way
num_squares = []    #define empty list
for v in range(1,11):
    num_squares += [v * v]
print(num_squares)
"""
print(b)
num_squares = []
for v in range(1,11):
    num_squares += [v * v]
print(num_squares)

