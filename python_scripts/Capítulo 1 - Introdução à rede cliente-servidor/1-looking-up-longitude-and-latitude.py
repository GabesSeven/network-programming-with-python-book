#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gabriel Ferreira
# é necessário autenticação na API da Google para obter a chave
# http://g.co/dev/maps-no-account
# 1 - procurando a longitude e latitude

# from pygeocoder import Geocoder
import requests
import geocoder

if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH'

    # address = 'Rua Véu das Noivas'
    # print(Geocoder.geocode(address)[0].coordinates)

    # g = geocoder.google(address)
    # print(g.latlng)
