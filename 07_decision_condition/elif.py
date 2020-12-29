#!/usr/bin/env python

num = input("Please enter a number: ")
num = int(num)
if num % 50 == 0:
  print("Half Century")
elif num == 100:
  print("Century")
elif num > 100: 
  print("Century +")
else:
  print("Unknown number")
