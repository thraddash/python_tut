#!/usr/bin/env python

import numpy as np
print("####### 1, 2, 3 #########")
x = np.array([1, 2, 3])
print(x.dtype)
print("######## 1.1, 2.1, 3.1 ########")
x = np.array([1.1, 2.1, 3.1])
print(x.dtype)
print("######### a, b, c #########")
x = np.array(["a", "b", "c"])
print(x.dtype)
print("########## True False ########")
x = np.array([True, False])
print(x.dtype)
