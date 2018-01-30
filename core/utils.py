# -*- coding: utf-8 -*-
__author__ = 'Joaquin'


import operator, random


def translateWord(masc, word):
    result = ''
    for letter in word:
        for masc_key in masc:
            if letter in masc.get(masc_key):
                result += str(masc_key)
    return result

def getRandomValue(list):
    max = 0;
    for tup in list:
        max += tup[1]
    ran = random.randint(1,max)
    now = 0
    value = None
    for tup in list:
        now += tup[1]
        if ran > now:
            continue
        else:
            value = tup[0]
            break
    return value


def readLettersMasc(path):
    file = open(path, 'r', encoding='utf8')
    masc = {}
    for line in file:
        parts = line.split(':')
        key = parts[0]
        values = []
        val_part = parts[1].split(',')
        for val in val_part:
            values.append(val.strip())
        masc[key] = values
    return masc
