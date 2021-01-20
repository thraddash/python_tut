#!/usr/bin/env python

## read list of lines

with open("names.txt") as fobj:
    lines = fobj.readlines()

print(lines)
print("########### strip() ###############")
with open("names.txt", "r") as fobj:
    for line in fobj:
        line = line.strip()
        print(line)

print("########### replace() ###############")
with open("names.txt", "r") as fobj:
    for line in fobj:
        line = line.replace("\r", "").replace("\n", "")
        print(line)

print("########### rstrip() ###############")
with open("names.txt", "r") as fobj:
    for line in fobj:
        line = line.rstrip()
        print(line)
