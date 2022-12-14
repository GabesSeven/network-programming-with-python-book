#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gabriel Ferreira
# 1 - usando getaddrinfo() para criar e conectar um soquete

# Encontra o serviço www de um host arbitrário usando getaddrinfo()

import argparse, socket, sys

def connect_to(hostname_or_ip):
    try:
        infolist = socket.getaddrinfo(
            hostname_or_ip, 'www', 0, socket.SOCK_STREAM, 0,
            socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME,
            )
    except socket.gaierror as e:
        print('Name service failure:', e.args[1])
        sys.exit(1)

    # de acordo com a recomendação padrão, testa o primeiro
    info = infolist[0]
    socket_args = info[0:3]
    address = info[4]
    s = socket.socket(*socket_args)
    try:
        s.connect(address)
    except socket.error as e:
        print('Network failure:', e.args[1])
    else:
        print('Success: host', info[3], 'is listening on port 80')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Try to connect to port 80')
    parser.add_argument('hostname', help='hostname that you want to contact')
    connect_to(parser.parse_args().hostname)
