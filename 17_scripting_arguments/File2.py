#!/usr/bin/env python

# __name__ is a built-in variable which evaluates to the name of the current module
# thus it can be used to check where the current script is being run on its own or being imported somwhere else
import File1

print("File2 ___name__ == %s" %__name__) 

if __name__ == "__main__":
    print("File2 is being run directly")
else:
    print("File2 is being imported")
