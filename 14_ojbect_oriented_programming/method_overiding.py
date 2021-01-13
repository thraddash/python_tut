#!/usr/bin/env python

# Method overriding

class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sum(self):
        return self.x + self.y

class MathExtend1(Math): # Child class
    def __init__(self, x, y):
        super().__init__(x,y)
    
    def subtract(self):
        return self.x - self.y

    def sum(self): # Override parent sum method
        return self.x +self.y + 100

    def show_all(self):
        print("Sum: " + str(self.sum())) #call the sum method in child class if exist, if not,  parents class
        print("Subtract: " + str(self.subtract()))
        
math_ext_obj = MathExtend1(10, 2)
math_ext_obj.show_all()

