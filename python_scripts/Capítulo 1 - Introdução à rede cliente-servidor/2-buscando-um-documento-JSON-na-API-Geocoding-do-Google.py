#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gabriel Ferreira
# é necessário autenticação na API da Google para obter a chave
# http://g.co/dev/maps-no-account
# 2 - buscando um documento JSON na API Geocoding do Google


import requests

def geocode(address):
    parameters = {'sensor': 'false', 'address': address}
    base = 'https://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    answer = response.json()
    print(answer)
    # print(answer['results'][0]['geometry']['location'])



if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
