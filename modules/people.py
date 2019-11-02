#!/usr/bin/env python
# -*- coding: utf-8 -*-

import modules.helper as helper
import modules.api as api

POSITIONS = [1, 2, 3] # 1 administrativo # 2 gerencial # 3 diretoria
POSITION_WEIGHTS = [60, 30, 20]

def translate_position(position):
    if position == 3:
        return 'Diretoria'
    elif position == 2:
        return 'Gerencial'
    else:
        return 'Administrativo'

def people_to_mini(people, position):
    return {
        'nome': people['nome'],
        'data_nascimento': people['data_nasc'],
        'email': people['email'],
        'cidade': people['cidade'],
        'estado': people['estado'],
        'cargo': translate_position(position)
    }

def peoples_to_mini(people_list, position_list):
    return [people_to_mini(people, position) for people, position in zip(people_list, position_list)]

def get_positions_list(peoples):
    return helper.random_weights(POSITIONS, POSITION_WEIGHTS, len(peoples))

def generate_peoples(amount_of_mens, amount_of_women):
    mens = api.get_peoples('H', amount_of_mens)
    women = api.get_peoples('M', amount_of_women)
    peoples = mens + women
    return peoples_to_mini(peoples, get_positions_list(peoples))