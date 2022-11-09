#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gabriel Ferreira
# 2 - servidor e cliente UDP em máquinas diferentes

# client e servidor UDP para comunicação de rede

import argparse, random, socket, sys

MAX_BYTES = 65535

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print('Listening at {}'.format(sock.getsockname()))

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        if random.random() < .5:
            print('Pretending to drop packet from {}'.format(address))
            continue
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))
        message = 'Your data was {} bytes long'.format(len(data))
        sock.sendto(message.ecode('ascii'), address)

def client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = sys.argv[2]
    sock.connect((hostname, port))
    print('CLient socket name is {}'.format(sock.getsockname()))

    delay = .1
    text = 'This is another message'
    data = text.encode('ascii')
    while True:
        sock.send(data)
        print('Waiting up to {} seconds for a reply'.format(delay))
        sock.settimeout(delay)
        try:
            data = sock.recv(MAX_BYTES)
        except socket.timeout:
            # espera ainda mais pela próxima solicitação
            delay *= 2
            if delay > 2.0:
                raise RuntimeError('I think the server is down')
            else:
                # terminamos e não podemos interromper o loop
                break
    print('The server at {} says {!r}'.format(data.decode('ascii')))


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally,'' pretending packets are opften dropped')
    parser.add_argument('role', choices=choices, help='which role to take')
    parser.add_argument('host', help='interface the server listens at;''host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
