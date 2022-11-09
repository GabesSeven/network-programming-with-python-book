#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gabriel Ferreira
# 2 - seguindo redirecionamento para usual em código de erro 3xx

import requests

from urllib.request import urlopen
import urllib.error

# biblioteca httplib:
# - não realiza redirecionamento automaticamente
# - é necessário detectar o código de erro 3XX de redirecionamento

# biblioteca urllib:
# - realiza redirecionamento automaticamente
r_urllib = urlopen('http://httpbin.org/status/301')
print(r_urllib.status, r_urllib.url)

print('\n\n*********************************\n\n')

# biblioteca requests:
# - realiza redirecionamento automaticamente
# - apresenta histórico de redirecionamentos que levaram até a última localização de endereço URL
# - permite desativar o redirecionamento
r_requests = requests.get('http://httpbin.org/status/301')
print(r_requests)
print(r_requests.history)

print('\n\n*********************************\n\n')

r_requests = requests.get('http://httpbin.org/status/301', allow_redirects=False)
r_requests.raise_for_status()
print(r_requests)

print('\n\n*********************************\n\n')


# dois dos redirecionamentos mais comuns envolve se o início do nome do host é usado no contato com o servidor
print(requests.get('http://google.com').url)
print(requests.get('http://www.twitter.com').url)

print('\n\n*********************************\n\n')

# método urlopen() lança um exceção quando há códigos de erro, evitando que o programa acidentalmente processe uma página de erro
# na biblioteca urllib, a resposta do método urlopen() se transforma em exceção e objeto
try:
    urlopen('http://localhost:80/status/500')
except urllib.error.HTTPError as e:
    print(e.status, repr(e.headers['Content-Type']))


print('\n\n*********************************\n\n')

# na biblioteca requests, códigos de erro resulta em objetos, sendo papel do chamador verificar através de status de resposta
# ou usandoo método raise_for_status()
print(requests.get('http://localhost:80/status/500').status_code)
print(requests.get('http://localhost:80/status/500').raise_for_status())
