#!C:\\Users\\lenno\\Anaconda3\\python.exe
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

URL_4DEVS = 'https://www.4devs.com.br/ferramentas_online.php'
URL_HIPOLABS = 'http://universities.hipolabs.com/search'

def get_peoples(gender, quantity):
    params = {'acao': 'gerar_pessoa', 'sexo': gender, 'txt_qtde': quantity}
    result = requests.post(URL_4DEVS, data=params)
    result.encoding = 'utf-8'
    return result.json()

def get_company(state, age):
    params = {'acao': 'gerar_empresa', 'pontuacao': 'N', 'estado': state, 'idade': age}
    companie = requests.post(URL_4DEVS, data=params).text
    soup = BeautifulSoup(companie, features="lxml")
    return {
        'nome': soup.find(id='nome').get('value'),
        'cidade': soup.find(id='cidade').get('value'),
        'estado': soup.find(id='estado').get('value')
    }

def get_companies(state, age, amount):
    i = 0
    companies = []
    while i <= amount:
        companies += [get_company(state, age)]
        i += 1
    return companies

def get_universities():
    params = {'country': 'Brazil'}
    result = requests.get(URL_HIPOLABS, params=params)
    result.encoding = 'utf-8'
    return result.json()