#!/usr/bin/env python

# Multiple exceptions
print("# tuple exception")
try: 
    disk_file = open('filename')
except(FileNotFoundError, PermissionError): # using tuple
    print("Can not open the file")

print()
print("# single line exception")
try:
    disk_file=open('filename')
except FileNotFoundError:
    print("File doesn't exist")
except PermissionError:
    print("Permission denied to open the file")
