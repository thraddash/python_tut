#!/usr/bin/env python

import sys
a = 'my-string'
sys.getrefcount(a)
b = [a] # make a list with a as an element
c = {'key': a} # create a dictionary with a as one of teh value
out=sys.getrefcount(a)

# ref 1 variable creation
# ref 2 pass variable a to sys.getrefcount() function

# import gc
# gc.get_threshod()

# import gc 
# gc.get_count()
class MyClass(object):
    pass
a = MyClass()
a.obj = a
del a
