#!/usr/bin/env python

# Class variable and Instance variable

class Alien:
    legs = 5 # class variable

    def __init__(self, name):
        self.name = name # instance variable

## Instantiation
alien1 = Alien('ET')
alien2 = Alien('Predator')

print(alien1.name, alien2.name) # accessing instance variable
print(alien1.legs, alien2.legs) # accessing class variable

# update class variable
Alien.legs = 10
print(alien1.legs, alien2.legs) # accessing class variable

# creates shadow instance with 99 ,instance variable gets more priority 5 
alien1.legs = 99
print(alien1.legs, alien2.legs) # accessing class variable

# to modify the instance variable of a class
# use __class__ , changes class variable to instance obj
# option2: use class name Alien.legs = 99
alien1.__class__.legs = 99
print(alien1.legs, alien2.legs) # accessing class variable

