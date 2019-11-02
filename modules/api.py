#!C:\\Users\\lenno\\Anaconda3\\python.exe
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.4devs.com.br/ferramentas_online.php'

def get_peoples(gender, quantity):
    params = {'acao': 'gerar_pessoa', 'sexo': gender, 'txt_qtde': quantity}
    return requests.post(BASE_URL, data=params).json()

def get_company(state, age):
    params = {'acao': 'gerar_empresa', 'pontuacao': 'N', 'estado': state, 'idade': age}
    companie = requests.post(BASE_URL, data=params).text
    soup = BeautifulSoup(companie)
    return {
        'nome': soup.find(id='nome').get('value'),
        'cidade': soup.find(id='cidade').get('value'),
        'estado': soup.find(id='estado').get('value')
    }

def get_companies(state, age, quantity):
    i = 0
    companies = []
    while i <= quantity:
        companies += [get_company(state, age)]
        i += 1
    return companies