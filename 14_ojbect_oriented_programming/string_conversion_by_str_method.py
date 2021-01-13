#!/usr/bin/env python

# string conversion of a class by __str__ method
#l = [1, 2, 3]
# print(l)

class Person:
    def __init__(self, name):
        self.name = name

# magic method __str__
    def __str__(self):
        return f'{self.__class__.__name__} class, obj name: {self.name}'

p1 = Person("Bill")
p2 = Person("Steve")

print(p1)
print(p2)

class employee:
    def __init__(self):
       	self.name='Swati'
       	self.salary=10000

    def __str__(self):
        return 'name='+self.name+' salary=$'+str(self.salary)

e1 = employee()
print(e1)
print("### magic method ###")
print(dir(int))

