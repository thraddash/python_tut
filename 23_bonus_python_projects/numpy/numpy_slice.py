#!/usr/bin/env python
# [start_index:end_index]
# end index will not be included

import numpy as np


print("##### a, b, c, d, e ########")
arr = ["a", "b", "c", "d", "e"]
print("#### [1:3] b, c #########")
print(arr[1:3]) # b , c 
print("#### [0:4] a, b, c, d #########")
print(arr[0:4]) # a , b, c , d
print("#### [2:] c , d, e #########")
print(arr[2:])
print("#### [:2] a, b #########")
print(arr[:2])
print("#### [-4:-1] b, c, d  #########")
print(arr[-4:-1])

