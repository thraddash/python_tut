#!/usr/bin/env python

a="""
############################################################
## Dictionary expression {key:value}
num_dict_sq = {v: v * v for v in range(1, 11) if v%2 != 0}
print(num_dict_sq)
"""
print(a)

num_dict_sq = {v: v * v for v in range(1, 11) if v%2 != 0}
print(num_dict_sq)
