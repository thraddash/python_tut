#!/usr/bin/env python

list_of_number = [1, 2, 'Math', 4, 5]
sum = 0
for num in list_of_number:
    if type(num) == int:
      sum += num
print(f"Sum is: {sum}")
