#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gabriel Ferreira
# 2 - consulta DNS simples realizando sua própria recursão

# Consulta DNS básica

import argparse, dns.resolver

def lookup(name):
    for qtype in 'A', 'AAAA', 'CNAME', 'MX', 'NS':
        answer = dns.resolver.query(name, qtype, raise_on_no_answer=False)
        if answer.rrset is not None:
            print(answer.rrset)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resolve a name using DNS')
    parser.add_argument('name', help='hostname that you want to look up in DNS')
    lookup(parser.parse_args().name)
