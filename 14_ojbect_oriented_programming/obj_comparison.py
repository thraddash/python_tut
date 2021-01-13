#!/usr/bin/env python

# Object comparison '==' vs 'is'
# == object comparison, checks if values for the two variables are the same
# is , identity comparison, if both variables points to same object
x = [1, 2, 3]
xx = x
print("x == xx, where x = [1, 2, 3], xx = x")
print(x == xx)
print("x is xx")
print(x is xx)
print()
y = list(x)
print("x == y")
print(x == y)
print("x is y, where y = list(x)")
print(x is y)
