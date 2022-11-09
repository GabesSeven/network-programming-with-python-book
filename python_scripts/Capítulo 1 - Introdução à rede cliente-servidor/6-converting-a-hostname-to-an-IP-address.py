#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gabriel Ferreira
# 7 - convertendo um nome de host em um endereço IP

import socket

if __name__ == '__main__':
    hostname = 'www.python.org'
    addr = socket.gethostbyname(hostname)
    print('O endereço IP de {} é {}'.format(hostname, addr))
