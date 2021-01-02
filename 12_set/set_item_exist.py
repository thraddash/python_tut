#!/usr/bin/env python

# Check item exist or not
set_country = {'europe', 'central america', 'usa'}
country = 'usa'

if country in set_country:
    print(country.title(), 'exists ')

if country not in set_country:
    print(country.title(), 'exists ')
