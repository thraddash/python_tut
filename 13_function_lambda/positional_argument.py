#!/usr/bin/env python
# Positional Arguement

def positional(a,b):
    first = f"a is {a}"
    second = f"b is {b}"
    return first, second

print(positional(4,10))
print(positional(10,4))

def key(a,b):
    first = f"a is {a}"
    second = f"b is {b}"
    return first, second
'''
print(key(a=2)) # error missing argument for b
'''
print(key(a=5, b=2))

