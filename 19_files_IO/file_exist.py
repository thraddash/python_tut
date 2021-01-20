#!/usr/bin/env python
a="""
############################
# File existence check

import os
if os.path.exists('spanish.txt'):
###########################
"""
print(a)

import os

if os.path.exists('spanish.txt'):
    print("Yes, file exist")

b="""
############################################
Temporary File module w+ = reading & write 
Temporary File auto destroy when program is closed
############################################
from tempfile import TemporaryFile

with TemporaryFile('w+') as fobj:
    fobj.write("Hello World\\n")

    fobj.seek(0) # seek to the the beggining
    data = fobj.read()
    print(data)
############################################
"""
print(b)
from tempfile import TemporaryFile

with TemporaryFile('w+') as fobj:
    fobj.write("Hello World \n")
    fobj.seek(0) # go to the beggining of the file
    data = fobj.read()
    print(data)
