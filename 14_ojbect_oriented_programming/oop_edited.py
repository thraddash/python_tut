#!/usr/bin/env python
# Class
# Global variable

class Restaurant:
    def details(self): 
        print(self.name, self.owner)

    def details_with_address(self, address):
        #print(self.name, self.owner)
        self.details()
        print(address)

## Instantiation
restaurant1 = Restaurant()
# creating instance variable
restaurant1.name = '7 Eleven'
restaurant1.owner= 'Seven'

# calling instance method will replace self argument
# instance object here restaurant1
restaurant1.details()
restaurant1.details_with_address('Elm Street')

#check object type, is an instance of the restaurant class
print(type(restaurant1))

