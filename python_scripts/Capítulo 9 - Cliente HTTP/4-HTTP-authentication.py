#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gabriel Ferreira
# 4 - autenticação HTTP

import requests



# biblioteca requests:
#  - dá suporte a autenticação básica através do parâmetro de palavra-chave

# r = requests.get('http://example.com/api', auth=('brandon', 'atigdngnatwwal'))
# r = requests.get('http://www.google.com', auth=('brandon', 'atigdngnatwwal'))
# print(r.headers)

s = requests.Session()
s.auth = 'brandon', 'atigdngnatwwal'
print(s.get('http://httpbin.org/basic-auth/brandon/atigdngnatwwal'))
