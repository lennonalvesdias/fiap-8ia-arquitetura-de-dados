#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

BASE_URL = 'https://www.4devs.com.br/ferramentas_online.php'

def get_peoples(gender, quantity):
    params = {'acao': 'gerar_pessoa', 'sexo': gender, 'txt_qtde': quantity}
    return requests.post(BASE_URL, data=params).json()

def get_companies(state, age):
    params = {'acao': 'gerar_empresa', 'pontuacao': 'N', 'estado': state, 'idade': age}
    return requests.post(BASE_URL, data=params).text