#!/usr/bin/env python

# Private and Public doesn't exist in python
# python convention with underscore _ before a variable means it is private, internal use, not public
# there is no difference print(math.x) print(math._x), by convention it is wrong to have print(math._x) 

class Math:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def sum(self):
        return self._x + self._y

math = Math(2, 4)
print(math._x)
print(math.sum())
