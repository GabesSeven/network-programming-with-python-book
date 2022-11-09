#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gabriel Ferreira
# 4 - conexão, sua reutilização e o httplib

import requests
import http.client

# biblioteca urllib e httplib:
#  - urllib não fornece reutilização, só pode ser realizado duas solicitações no mesmo soquete com a biblioteca padrão httplib

h = http.client.HTTPConnection('localhost:8000')
h.request('GET', '/ip')
r = h.getresponse()
print(r.status)

h.request('GET', '/user-agent')
r = h.getresponse()
print(r.status)
