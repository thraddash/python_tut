#!/usr/bin/env python

#--------------------------
# Conditional Expression
#--------------------------
'''
In Java, C++ ternary operator, takes 3 operands
condition ? expression1: expression2

In Python 3 equivalent is called conditional expression
expression1 if condition else expression2
'''

sum = 100
num = 10
a = """
######################################
sum += num if num % 2 == 0 else 0
"""
print(a)
sum += num if num % 2 == 0 else 0
print(sum)

print()
sum = 100
num = 10
b = """
######################################
sum = 100
num = 10

if num % 2 == 0:
    sum += num
    print(sum)
else: 
    sum += 0
"""
print(b)

if num % 2 == 0:
    sum += num
    print(sum)
else: 
    sum += 0

