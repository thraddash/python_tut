#!/usr/bin/env python

# calling my_name_is_slim_shady.py from a file what_is_my_name.py 
# Output: my_name_is_slim_shady
# Output: class name MyNameIsSlimShady

# what_is_my_name.py
print("What's my name?")
import my_name_is_slim_shady

# Outputs: 
# What's my name?
# my_name_is_slim_shady

# Calling the my_name_is_slim_shady.py from a file what_is_my_name.py 
# Outputs: my_name_is_slim_shady and class name MyNameIsSlimShady
print()
ss = my_name_is_slim_shady.MyNameIsSlimShady()
ss.say_my_name()
print(ss.__class__.__name__)

# Outputs: 
# My name is:
# MyNameIsSlimShady

# the __name__ variable module that is being executed is set to __main__
# it is use to check if a module is invoked directly or called from a different file

def main_what_is_my_name():
    print("Not Standing Up")

if __name__ == '__main__':
    main_what_is_my_name()

# Output:
# Not Standing Up
