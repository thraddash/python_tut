#!/usr/bin/env python

#-----------------------
# __name__ == '__main__
#-----------------------

def square(num):
    return num * 2

# __name__ is assigned to the module/file that it is associated with
# it can also be asigned to module, classes, functions, methods, descriptors, genrator instances
# __name__ variable for the module that is being executed is set to __main__ for the script
# it is used to check if the modue is invoked directly or called from a different file

# when you run main.py alone, square() function is invoked sine the __name__ 
# for the file is sets to __main__ for this module

if __name__ == '__main__': 

    print(square(2))
