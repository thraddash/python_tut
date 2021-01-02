#!/usr/bin/env python

# Set operation
set_a = {1, 2, 3, 4, 5, 1}
set_b = {6, 5, 4, 7, 8, 8}
print("Set A: ", set_a)
print("Set B: ", set_b)

print("#items in set_a but not in set_b")
print("A-B ", set_a - set_b) 
print("#items in set_a or set_b or both")
print("A|B ", set_a | set_b)
print("#common items in set_a and set_b")
print("A&B", set_a & set_b) 
print("#items in set_b but not in set_a")
print("B-A ", set_b - set_a)
print("#items in set_a or set_b but no both")
print("A^B ", set_a ^ set_b)
