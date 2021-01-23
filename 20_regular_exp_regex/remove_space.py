#!/usr/bin/env python

# strip unwanted middle space

import re

text = "hello    world"
print("Original: " + text)
txtre = re.compile(r'\s+')
text = txtre.sub(' ', text)
print(text)
