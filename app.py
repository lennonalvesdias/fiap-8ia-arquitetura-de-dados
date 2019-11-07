#!/usr/bin/env python
# -*- coding: utf-8 -*-

import modules.helper as helper
import modules.people as people
import modules.company as company
import modules.university as university


def main():
    try:
        print('running application')
        print('generate peoples')
        peoples = people.generate_peoples(5, 5)
        print('saving peoples')
        helper.save_txt('data/peoples.txt', peoples)
        print('generate companies')
        companies = company.generate_companies(6)
        print('saving companies')
        helper.save_txt('data/companies.txt', companies)
        print('generate universities')
        universities = university.generate_universities(4)
        print('saving universities')
        helper.save_txt('data/universities.txt', universities)
    except Exception as ex:
        print("{0.__name__}: {1}".format(type(ex), ex))


if __name__ == "__main__":
    main()
