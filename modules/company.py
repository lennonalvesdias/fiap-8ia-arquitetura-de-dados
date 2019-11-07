#!/usr/bin/env python
# -*- coding: utf-8 -*-

import modules.helper as helper
import modules.api as api
import modules.repository as repository

OCCUPATIONS = [1, 2, 3]  # 1 exatas # 2 humanas # 3 biologicas
OCCUPATIONS_WEIGHTS = [60, 20, 20]


def save_companies(companies):
    repo = repository.Repository()
    for company in companies:
        repo.save_company(company)


def translate_occupation(ocuppation):
    if ocuppation == 3:
        return 'Biológicas'
    elif ocuppation == 2:
        return 'Humanas'
    else:
        return 'Exatas'


def get_company_ocupation(company, occupation):
    company['area'] = translate_occupation(occupation)
    return company


def get_companies_ocupation(company_list, occupation_list):
    return [get_company_ocupation(company, occupation) for company, occupation in zip(company_list, occupation_list)]


def get_occupation_list(companies):
    return helper.random_weights(OCCUPATIONS, OCCUPATIONS_WEIGHTS, len(companies))


def get_full_companies(state, age, amount):
    companies = api.get_companies(state, age, amount)
    companies = get_companies_ocupation(
        companies, get_occupation_list(companies))
    return companies


def generate_companies(amount):
    sp = get_full_companies('SP', 5, round(amount * 0.3))
    rj = get_full_companies('RJ', 5, round(amount * 0.3))
    mg = get_full_companies('MG', 5, round(amount * 0.2))
    pr = get_full_companies('PR', 5, round(amount * 0.2))
    companies = sp + rj + mg + pr
    save_companies(companies)
    return companies
