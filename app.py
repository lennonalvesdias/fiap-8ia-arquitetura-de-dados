#!C:\\Users\\lenno\\Anaconda3\\python.exe
# -*- coding: utf-8 -*-

import modules.helper as helper
import modules.people as people

BASE_DATA_FILES = 'C:\\Users\\lenno\\OneDrive\\Projects\\arquitetura\\data\\'

def main():
    try:
        mens = helper.read_txt(f'{BASE_DATA_FILES}\\mens.txt')
        womens = helper.read_txt('C:\\Users\\lenno\\OneDrive\\Projects\\arquitetura\\data\\womens.txt')
        peoples = people.generate_peoples(mens + womens)
        helper.save_txt(f'{BASE_DATA_FILES}\\peoples.txt', peoples)
    except Exception as ex:
        print("{0.__name__}: {1}".format(type(ex), ex))

if __name__ == "__main__":
    main()