#!/usr/bin/env python
# -*- coding: utf-8 -*-

from py2neo import Graph, Node, Relationship
import json


class Repository(object):
    def __init__(self):
        self._graph = Graph('bolt://localhost:7687', auth=('neo4j', "admin"))

    def save_people(self, people):
        people = json.loads(people)
        tx = self._graph.begin()
        node = Node("Pessoa", Nome=people['nome'], DataDeNascimento=people['data_nascimento'], Email=people['email'],
                      Cidade=people['cidade'], Estado=people['estado'], Cargo=people['cargo'])
        tx.create(node)
        tx.commit()

    def save_company(self, company):
        company = json.loads(company)
        tx = self._graph.begin()
        node = Node("Empresa", Nome=company['nome'], Cidade=company['cidade'], Estado=company['estado'], Area=company['area'])
        tx.create(node)
        tx.commit()

    def set_people_and_company_relationship(self, people, company):
        people = json.loads(people)
        people_node = Node("Pessoa", Nome=people['nome'], DataDeNascimento=people['data_nascimento'], Email=people['email'],
                      Cidade=people['cidade'], Estado=people['estado'], Cargo=people['cargo'])
        people_node.__primarylabel__ = "Pessoa"
        people_node.__primarykey__ = "Nome"
        company = json.loads(company)
        company_node = Node("Empresa", Nome=company['nome'], Cidade=company['cidade'], Estado=company['estado'], Area=company['area'])
        company_node.__primarylabel__ = "Empresa"
        company_node.__primarykey__ = "Nome"
        relationship = Relationship.type("TRABALHA")
        self._graph.merge(relationship(people_node, company_node))

# repo = Repository()

# people_sample = """
# {
#         "nome": "Jorge Anthony Marcelo Viana",
#         "data_nascimento": "10/10/1983",
#         "email": "jjorgeanthonymarceloviana@eanac.com.br",
#         "cidade": "Olinda",
#         "estado": "PE",
#         "cargo": "Administrativo"
#     }
#     """
# company_sample = """
# {
#         "nome": "Cláudio e Arthur Joalheria Ltda",
#         "cidade": "Itu",
#         "estado": "SP",
#         "area": "Exatas"
#     }
#     """

# repo.save_people(people_sample)
# repo.save_company(company_sample)
# repo.set_people_and_company_relationship(people_sample, company_sample)