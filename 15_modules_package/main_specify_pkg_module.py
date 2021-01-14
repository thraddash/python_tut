#!/usr/bin/env python

# specify the package and module

from mspack.msmath import *

print(sum(10, 2))
print(subtract(10, 2))
print(multiplication(2, 2))
print()

'''
https://docs.python.org/3/library/index.html
'''
print("# python standard library")
from random import choice
list = [1, 2, 3, 4, 5]
for x in range(0, 3):
    print(choice(list))
print()

print("## list module attribute")
print("## import module")
print("## module.__dict__.keys()")
import random
print(random.__dict__.keys())
