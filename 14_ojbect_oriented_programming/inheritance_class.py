#!/usr/bin/env python

class Math: # Parent class
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sum(self):
        return self.x + self.y

class MathExtended1(Math): # Child class , MathExtended1 inherited Math features sum
    def __init(self, x, y): 
        supper().__init__(x, y) # super() func makes connection to parent class with child class
    def subtract(self):
        return self.x - self.y

math_obj = Math(2, 4)
print(math_obj.sum())

math_ext_obj= MathExtended1(10, 2)
print(math_ext_obj.subtract())
print(math_ext_obj.sum())

