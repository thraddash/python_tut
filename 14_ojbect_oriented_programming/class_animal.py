#!/usr/bin/env python
# self - parameter access attributes and methods of class
# __init__() function provide values for the attributes of a class

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name + " walks")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sound(self):
        print(self.name + " barks")

a = Dog("puppy", 1)
a.walk()
a.sound()
