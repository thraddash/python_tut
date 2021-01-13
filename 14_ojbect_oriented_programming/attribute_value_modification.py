#!/usr/bin/env python

class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, name):
        self.name = name

    def details(self):
        print(self.name, self.age, sep=' | ')

## Directly change
person_x = Person(name='The Rock', age = 49)
person_x.details()

person_x.name = "Stone Cold"
person_x.details()

## Indirectly change by instance's method
person_x.change_name('Triple X')
person_x.details()
