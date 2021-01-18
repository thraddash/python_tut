#!/usr/bin/env python
a="""
#################################################################################################
# An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted. 
# The only difference between dict() and OrderedDict() is that:
#
# OrderedDict preserves the order in which the keys are inserted. 
# A regular dict doesn’t track the insertion order, and iterating it gives the 
# values in an arbitrary order. By contrast, the order the items are inserted is 
# remembered by OrderedDict 
"""
print(a)

from collections import OrderedDict

print("This is a Dict:\n") 
d = {} 
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key, value in d.items(): 
    print(key, value) 
  
print("\nThis is an Ordered Dict:\n") 
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
  
for key, value in od.items(): 
    print(key, value) 
print()
b="""
####################################################################################
# Key value Change: If the value of a certain key is changed, 
# the position of the key remains unchanged in OrderedDict.
"""
from collections import OrderedDict 
  
print("Before:\n") 
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items(): 
    print(key, value) 
  
print("\nAfter:\n") 
od['c'] = 5
for key, value in od.items(): 
    print(key, value) 

c="""
#######################################################################################
# Deletion and Re-Inserting: Deleting and re-inserting the same key will push 
# it to the back as OrderedDict however maintains the order of insertion.
#
"""
print(c)
print()
from collections import OrderedDict 
  
print("Before deleting:\n") 
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
  
for key, value in od.items(): 
    print(key, value) 
  
print("\nAfter deleting:\n") 
od.pop('c') 
for key, value in od.items(): 
    print(key, value) 
  
print("\nAfter re-inserting:\n") 
od['c'] = 3
for key, value in od.items(): 
    print(key, value)
