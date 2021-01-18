#!/usr/bin/env python

a="""
#######################################################################
## Set expression
# Note: only unique value will be added to the set, no duplicate numbers

num_dict_sq = {v * v for v in range(1, 11) if v%2 != 0}
print(num_dict_sq)
"""
print(a)

num_dict_sq = {v * v for v in range(1, 11) if v%2 != 0}
print(num_dict_sq)
