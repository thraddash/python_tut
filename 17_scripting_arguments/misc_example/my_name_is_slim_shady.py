#!/usr/bin/env python

# my_name_is_slim_shady.py
# __name__ is a built-in variable which evaluates to the name of the current module
# thus it can be used to check where the current script is being run on its own or being imported somwhere else

print(__name__) 

class MyNameIsSlimShady(object):

    def say_my_name(self): 
        # self represent the instance of the class, grant access to the attributes and methods of the class
        print("My name is")

def main_my_name_is_slim_shady():
    print("Standing Up!")

if __name__ == '__main__':
    main_my_name_is_slim_shady()

# main_my_name_is_slim_shady() function is invoked since the __name__ for the file is set to main for this module
# Output:
# Standing Up!
