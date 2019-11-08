#!/usr/bin/env python
# -*- coding: utf-8 -*-

from py2neo import Graph, Node, Relationship
import json


class Repository(object):
    def __init__(self):
        self._graph = Graph('bolt://neo4jdb:7687', auth=('neo4j', "admin"))

    def clear(self):
        self._graph.delete_all()

    def save_people(self, people):
        if isinstance(people, str): people = json.loads(people)
        tx = self._graph.begin()
        node = Node("Pessoa", Nome=people['nome'], DataDeNascimento=people['data_nascimento'], Email=people['email'],
                      Cidade=people['cidade'], Estado=people['estado'], Cargo=people['cargo'])
        tx.create(node)
        tx.commit()

    def save_company(self, company):
        if isinstance(company, str): company = json.loads(company)
        tx = self._graph.begin()
        node = Node("Empresa", Nome=company['nome'], Cidade=company['cidade'], Estado=company['estado'], Area=company['area'])
        tx.create(node)
        tx.commit()

    def save_university(self, university):
        if isinstance(university, str): university = json.loads(university)
        tx = self._graph.begin()
        node = Node("Empresa", Nome=company['nome'], Cidade=company['cidade'], Estado=company['estado'], Area=company['area'])
        tx.create(node)
        tx.commit()

    def set_people_and_company_relationship(self, people, company):
        if isinstance(people, str): people = json.loads(people)
        people_node = Node("Pessoa", Nome=people['nome'], DataDeNascimento=people['data_nascimento'], Email=people['email'],
                      Cidade=people['cidade'], Estado=people['estado'], Cargo=people['cargo'])
        people_node.__primarylabel__ = "Pessoa"
        people_node.__primarykey__ = "Nome"
        if isinstance(company, str): company = json.loads(company)
        company_node = Node("Empresa", Nome=company['nome'], Cidade=company['cidade'], Estado=company['estado'], Area=company['area'])
        company_node.__primarylabel__ = "Empresa"
        company_node.__primarykey__ = "Nome"
        relationship = Relationship.type("TRABALHA")
        self._graph.merge(relationship(people_node, company_node))

    def set_people_and_university_relationship(self, people, university):
        if isinstance(people, str): people = json.loads(people)
        people_node = Node("Pessoa", Nome=people['nome'], DataDeNascimento=people['data_nascimento'], Email=people['email'],
                      Cidade=people['cidade'], Estado=people['estado'], Cargo=people['cargo'])
        people_node.__primarylabel__ = "Pessoa"
        people_node.__primarykey__ = "Nome"
        if isinstance(university, str): university = json.loads(university)
        university_node = Node("Universidade", Nome=university['nome'], Cidade=university['cidade'], Estado=university['estado'])
        university_node.__primarylabel__ = "Universidade"
        university_node.__primarykey__ = "Nome"
        relationship = Relationship.type("ESTUDA")
        self._graph.merge(relationship(people_node, university_node))