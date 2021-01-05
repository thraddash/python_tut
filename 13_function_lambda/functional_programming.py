#!/usr/bin/env python

#Functional programming

def str_upper(str):
    return str.upper()

# Functional programming
# map (function, iter)

up_list = list(map(str_upper, ["life", "is", "Cool"]))
print(up_list)

def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

