#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gabriel Ferreira
# 5 - conversando com o Google Maps através de um soquete simples


if __name__ == '__main__':
    # Conversão de bytes do ambiente externo em caracteres Unicode
    input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
    input_characters = input_bytes.decode('utf-16')
    print(repr(input_characters))

    # Conversão de caracteres em bytes antes de seu envio
    output_characters = 'We copy you down, Eagle.\n'
    output_bytes = output_characters.encode('utf-8')
    # print(output_characters.encode('utf-16'))
    with open('eagle.txt', 'wb') as f:
        f.write(output_bytes)
