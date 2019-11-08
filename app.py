#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

import modules.helper as helper
import modules.people as people
import modules.company as company
import modules.university as university
import modules.repository as repository

def create_peoples_companies_relationships(peoples, companies, relationships):
    print('create peoples and companies relationships')
    repo = repository.Repository()
    [repo.set_people_and_company_relationship(people, companies[relationship]) for people, relationship in zip(peoples, relationships)]

def create_peoples_university_relationships(peoples, universities, relationships):
    print('create peoples and universities relationships')
    repo = repository.Repository()
    [repo.set_people_and_university_relationship(people, universities[relationship]) for people, relationship in zip(peoples, relationships)]

def generate_database():
    print('clear database')
    repository.Repository().clear()
    print('generate peoples')
    peoples = people.generate_peoples(5, 5)
    print('saving peoples')
    helper.save_txt('data/peoples.txt', peoples)
    print('generate companies')
    companies = company.generate_companies(3)
    print('saving companies')
    helper.save_txt('data/companies.txt', companies)
    print('generate universities')
    universities = university.generate_universities(4)
    print('saving universities')
    helper.save_txt('data/universities.txt', universities)
    return peoples, companies, universities


def main():
    try:
        print('running application')
        peoples, companies, universities = generate_database()
        create_peoples_companies_relationships(peoples, companies, helper.random_weights(np.arange(0, len(companies)), None, len(peoples)))
        create_peoples_university_relationships(peoples, universities, helper.random_weights(np.arange(0, len(universities)), None, len(peoples)))
    except Exception as ex:
        print("{0.__name__}: {1}".format(type(ex), ex))


if __name__ == "__main__":
    main()
