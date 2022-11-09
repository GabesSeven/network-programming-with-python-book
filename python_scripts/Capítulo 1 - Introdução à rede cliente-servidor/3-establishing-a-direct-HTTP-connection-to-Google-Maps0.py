#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gabriel Ferreira
# é necessário autenticação na API da Google para obter a chave
# http://g.co/dev/maps-no-account
# 3 - estabelecendo uma conexão HTTP direta com o Google Maps


import http.client
import json
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'

def geocode(address):
    path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
    connection = http.client.HTTPConnection('maps.google.com')
    connection.request('GET', path)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply)
    # print(reply['results']['0']['geometry']['location'])


if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
