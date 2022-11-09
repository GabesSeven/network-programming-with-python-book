#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gabriel Ferreira
# 1 - acessando páginas web com urllib e request
# deve-se ligar o XAMPP, antes de fazer uma solicitação localhost

import requests

from urllib.request import urlopen
import urllib.error



# biblioteca requests:
#  - dá suporte a respostas HTTP compactadas (gzip, deflate)
#  - determina decodificação ASCII automaticamente

r_requets = requests.get('http://localhost:80/headers')
print(r_requets.text)

print('\n\n*********************************\n\n')

r_urllib = urlopen('http://localhost:80/headers')
print(r_urllib.read().decode('ascii'))
