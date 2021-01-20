#!/usr/bin/env python
# Serialize python object ot a byte stream

import pickle

dict_data = {'name':'Mike', 'country':'USA'}

with open('serialize', 'wb') as fobj:
    pickle.dump(dict_data, fobj)

with open('serialize', 'rb') as fobj:
    dict_data = pickle.load(fobj)
    print(dict_data)
