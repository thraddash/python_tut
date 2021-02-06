#!/usr/bin/env python
'''
pip install requests
pip install lxml
'''

import requests
from bs4 import BeautifulSoup
url = 'https://abcnews.go.com/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("List of all the h1, h2, h3 :")
for heading in soup.find_all(["h1", "h2", "h3"]):
     print(heading.name + ' ' + heading.text.strip())
