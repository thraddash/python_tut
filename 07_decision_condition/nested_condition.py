#!/usr/bin/env python

# nested condition
x = input("Please enter a number: ")
x = int(x)
if x < 2:
  print("less than 2")
else:
  if x == 3:
    print("x is 3")
  else:
    if x == 5:
      print("x is 5")
    else:
      if x >=2:
        print("greater than 2 or equal to 2")

