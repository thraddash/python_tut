#!/usr/bin/env python

numbers_list = [1, 2, 3, 4, 5]
numbers_list[:] = (value for value in numbers_list if value != 2)
print(numbers_list)
