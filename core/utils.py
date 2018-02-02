# -*- coding: utf-8 -*-
__author__ = 'Joaquin, Luis'


import operator, random, math

def translatePhrase(masc, phrase):
    words =phrase.split(' ')
    translations = []
    for word in words:
        translations.append(translateWord(masc, word))
    return ' '.join(translations)

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
    ran = random.randint(0,int(math.floor(max)))
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

def extractAllowedChars(masc):
    return flatListOfList(list(masc.values()))

def flatListOfList(things):
    return [item for sublist in things for item in sublist]

def flatListOfStrings(things):
    return ''.join(things)

def readFileToString(path):
    file = open(path, 'r', encoding='utf8')
    return file.readlines()

def listOfPuntuationsMarks():
    return ["(",")","¡","!","¿","?",":",";","@","#",",","."," ","...", "_", "-", "[", "]", "\""]

def checkApproximation(original, comparation):
    longi = len(original)
    i = 0
    for index in range(0, longi):
        if original[index] == comparation[index]:
            i += 1
    return str((i/longi) * 100) + " %"


def checkNum(s):
    try:
        int(s)
        return True
    except ValueError:
        return False