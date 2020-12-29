#!/usr/bin/env python

print("# Matching text a the start and at the end")
filename = 'xbigdata.txt'
print(filename.endswith('.txt'))
print(filename.startswith('bi'))

print('')
print("# Find word in sentence")
sentence = "A quick brown fox jumps over the lazy dog"
print(sentence.find('fox')) # index 14
print(sentence.find('foxs')) #-1 the value not found

print('')
print("# Replace text")
sentence = sentence.replace('fox', 'tiger')
print(sentence)

print('')
print("# Print separator x,y,z, sep = '| ' ")
x = 'The'
y = 'Red'
z = 'Balloon'
print(x + '| ' + y + '| ' + z)
print(x,y,z, sep='| ')
