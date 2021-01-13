#!/usr/bin/env python
# Multiple Inheritance

class Math: # Parent class
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sum(self):
        return self.x + self.y

class MathExtended1(Math): # Child class , MathExtended1 inherited Math features sum (single inheritance)
    def __init(self, x, y): 
        supper().__init__(x, y) # super() func makes connection to parent class with child class
    def subtract(self):
        return self.x - self.y

# Multiple Inheritance
class MathExtra:
    def division(self, x, y):
        return x /y

class MathExtended2(MathExtended1, MathExtra): # Child class, (multi class inheritance)
    def __init__(self, x, y):
        super().__init__(x,y)

    def multiplication(self):
        return self.x * self.y

math_ext2 = MathExtended2(10, 2)
print("10 2")
print("Sum ", str(math_ext2.sum()))
print("Subtract ", str(math_ext2.subtract()))
print("Multiplication ", str(math_ext2.multiplication()))
print("Division ", str(math_ext2.division(x=math_ext2.x,y=math_ext2.y))) #MathExtra does not have self reference variable, does not reference any class varaibles, must pass x , y value for division function
