#!/usr/bin/env python

# import specific module in a package
print("# include __init__.py in mspack folder to indicate that it is a package directory")
print()
from mspack import msmath
from mspack import msstring
#from mspack import *

print("# from mspack import msmath")
print("# from mspack import mstring")
print("argument 10 + 2")
print(msmath.sum(10, 2))
print("argument 10 - 2")
print(msmath.subtract(10, 2))
print("argument 2 * 2")
print(msmath.multiplication(2, 2))
print()
print("forloop Hello world")
msstring.print_characters("Hello World!")
print()
print("# import all module from package")
print("# from mspack import *")
print("# update __init__.py with Python magic methods or dunder methods __all__, all module list")
print("Dunder - Double Underscores")
print('# __all__ = ["msmath", "msstring"]')
 
