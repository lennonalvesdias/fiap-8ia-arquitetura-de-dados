#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from random import choices

def random_weights(values, weights, quantity):
    return choices(values, weights, k=quantity)

def read_txt(file_path):
    with open(file_path, 'r', encoding="utf8") as txt_file:
        return json.load(txt_file)

def save_txt(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as outfile:
        json.dump(content, outfile, indent=4, ensure_ascii=False)