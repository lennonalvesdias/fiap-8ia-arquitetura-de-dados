#!/usr/bin/env python
# -*- coding: utf-8 -*-

import modules.helper as helper
import modules.api as api
import modules.repository as repository

STATES = [1, 2, 3]  # 1 sp # 2 rj # 3 pr
STATES_WEIGHTS = [40, 20, 20]


def save_universities(universities):
    repo = repository.Repository()
    for university in universities:
        repo.save_university(university)


def translate_state(state):
    if state == 3:
        return 'PR', 'Curitiba'
    elif state == 2:
        return 'RJ', 'Rio de Janeiro'
    else:
        return 'SP', 'São Paulo'


def get_univesity_state(universtity, state):
    state_and_city = translate_state(state)
    universtity['estado'] = state_and_city[0]
    universtity['cidade'] = state_and_city[1]
    return {
        'nome': universtity['name'],
        'estado': state_and_city[0],
        'cidade': state_and_city[1]
    }


def get_universities_state(university_list, state_list):
    return [get_univesity_state(universtity, state) for universtity, state in zip(university_list, state_list)]


def get_state_list(universities):
    return helper.random_weights(STATES, STATES_WEIGHTS, len(universities))


def generate_universities(amount):
    universities = api.get_universities()[:amount]
    state_list = get_state_list(universities)
    universities = get_universities_state(universities, state_list)
    return universities
