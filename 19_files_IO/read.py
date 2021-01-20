#!/usr/bin/env python 
#----------------------
# Files
#---------------------

# Reading full contents of a text file
# with , auto close file

try:
    with open('data.txt') as fobj:
        contents = fobj.read()
        print(contents)
except Exception as e:
    print("File Erorr: ", e)
