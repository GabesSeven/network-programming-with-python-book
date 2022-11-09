#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Gabriel Ferreira
# 3 - negociação de conteúdo

import requests



# biblioteca requests e urllib:
#  - permite que você insira qualquer cabeçalho Accept na solicitação que quiser
#  - são suporte a padrões para criação de cliente que usará seus cabeçalho favoritos
#  - constrói como parte de sua session

s = requests.Session()
print(s.headers)

print('\n\n')

s.headers.update({'Accept-Language': 'en-US,en;q=0.8'})
print(s.headers)
