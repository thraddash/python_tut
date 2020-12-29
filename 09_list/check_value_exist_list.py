#!/usr/bin/env python
numbers = [3, 1, 2, 3, 4, 3, 2]
print(numbers)
if 2 in numbers:
    print("2 is in number")

if 20 not in numbers:
    print("20 does not exist")

count=0
while count < len(numbers):
    print("index: " + str(count),"value: " + str(numbers[count]))
    count +=1

count=0
while count < len(numbers):
    if numbers[count] == 3:
      print("found 3")
    count +=1
