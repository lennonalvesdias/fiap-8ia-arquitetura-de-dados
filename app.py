#!C:\\Users\\lenno\\Anaconda3\\python.exe
# -*- coding: utf-8 -*-

import modules.helper as helper
import modules.people as people

def main():
    try:
        peoples = people.generate_peoples(30, 20)
        helper.save_txt('data/peoples.txt', peoples)
    except Exception as ex:
        print("{0.__name__}: {1}".format(type(ex), ex))

if __name__ == "__main__":
    main()