#!/usr/bin/env python

# Traditional Read
# close file

try: 
    fobj = open('data.txt')
except Exception as e:
    print("File Error: ", e)
else:
    contents = fobj.read()
    print(contents)
finally:
    fobj.close()
