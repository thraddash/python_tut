#!/usr/bin/env python

#Iteration Tuple

tp = 1, 2, 'bill', 4.4, False
for t in tp:
    print(t)

#Compare
t1 = 1, 2, 3
t2 = 1, 2, 3
if t1 == t2:
    print("t1 and t2 values are equal\n")

print("#Immutable")
print("t1 = 1, 2, 3")
print("t1[0]=2\n")

print("# Unpacking Multiple assignment")
t1 = 5, 7, 11
x, y, z = t1
print(x, y, z, sep = ' | ')

print("# Underscore _ unuse")
t1 = 5, 7, 11
x, y, _ = t1
print(x, y, sep = ' | ')

