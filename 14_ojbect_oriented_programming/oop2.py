#!/usr/bin/env python

# class second example

class Person:
    # initialize attributes using constructor
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def details(self):
        print(self.name, self.age, sep=' | ')

bill1 = Person()
bill1.details()

# Create another object
bill2 = Person('Bill',33) # self pass automatically
bill2.details()

## Third example
# store class obj in list 
people_list = []
for x in range(0,3):
    person = Person("Person "+str(x), 30+x)
    people_list += [person]

for x in people_list:
    x.details()
