#!/usr/bin/env python
# Class
# Global variable
restaurant_name = '7 Eleven'
restaurant_owner = 'Seven'

def restaurant_details(): #function
    print(restaurant_name, restaurant_owner)

def another_restaurant(): #local variable
    restaurant_address = 'Bogra'
    print(restaurant_name, restaurant_owner)
    print(restaurant_address)

restaurant_details()
another_restaurant()

# Syntax
'''
class ClassName(ParentClass): #inherit
    class variables
    instance methods
'''

