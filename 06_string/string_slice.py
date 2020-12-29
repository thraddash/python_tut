#!/usr/bin/env python

print("#String slice, use range operator")
name = 'name = "Taylor Swift"'
print(name)
print(name[0: 6], "name[0:6] #include char until 5")
print(name[:6], "name[:6]  #automatically use zero as the start of the index")
print(name[7:], "name[7:] # starts from index 7 until end of sequence")
print(name[7:-1], "name[7:-1] #starts from index 7 until end of sequence, subtract last character in the sequence")
