#!/usr/bin/env python

a="""
###########################
## Case sensitive search
###########################
text = "movie New MOVIE release mOVIe"

find movie, capture all upper case and lower case
print list

sub mOVIe with bad, ignore case on mOVIe
OUTPUT: bad New bad release bad
"""
print(a)

import re

text = "movie New MOVIE release mOVIe"
list = re.findall('movie', text, flags=re.IGNORECASE)
print(list)

text = re.sub('mOVIe', 'bad', text, flags=re.IGNORECASE)
print(text)
