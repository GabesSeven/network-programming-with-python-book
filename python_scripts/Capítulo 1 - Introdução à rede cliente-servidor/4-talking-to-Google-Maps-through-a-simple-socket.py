#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gabriel Ferreira
# é necessário autenticação na API da Google para obter a chave
# http://g.co/dev/maps-no-account
# 4 - conversando com o Google Maps através de um soquete simples


import socket
from urllib.parse import quote_plus

request_text = """\
GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.1\r\n\
Host: maps.google.com:80\r\n\
User-Agent: search.py (Foundations of Python Network Programing)\r\n\
Connection: close\r\n\
\r\n\
"""

def geocode(address):
    sock = socket.socket()
    sock.connect(('maps.google.com', 80))
    request = request_text.format(quote_plus(address))
    sock.sendall(request.encode('ascii'))
    raw_reply = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more
    print(raw_reply.decode('utf-8'))


if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
