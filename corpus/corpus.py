# -*- coding: utf-8 -*-
__author__ = 'Joaquin, Luis'

import re, os
import core.utils as Utils

def getCaracteresUnigram(s, allowed, corpus={}):
    dict = corpus
    s = s.lower()
    for x in s:
        if x in dict.keys():
            dict[x] += 1
        elif x in allowed:
            dict[x] = 1
    return dict

def getPalabrasUnigram(s, corpus={}):
    dict = corpus
    s = s.lower()
    s = re.sub(r'[0-9]+','',s)
    string = re.findall(r'\w+',s)
    for x in string:
        if x in dict.keys():
            dict[x] += 1
        else:
            dict[x] = 1
    return dict

def getCaracteresBigram(s, allowed, corpus={}):
    dict = corpus
    punctmarks = Utils.listOfPuntuationsMarks()
    s = s.lower()
    lastChar = ""
    for x in s:
        if lastChar == "" and x in allowed:
            lastChar = x
        elif x in dict.keys():
            if lastChar in dict[x].keys():
                i = dict[x][lastChar]+1
                dict[x].update({lastChar:i})
            else:
                dict[x].update({lastChar:1})
            lastChar = x
        elif x in punctmarks:
            lastChar = ""
        elif x in allowed:
            dict[x] = {lastChar:1}
            lastChar = x
    return dict


def getPalabrasBigram(s, corpus={}):
    dict = corpus
    punctmarks = Utils.listOfPuntuationsMarks()
    s = s.lower()
    string = re.findall(r"[A-záéíóúñ]+|[1-9]+|[\.)(?¿!¡:;@#,]+", s, re.DOTALL | re.IGNORECASE)
    lastWord = ""
    for x in string:
        if lastWord == "" and x not in punctmarks:
            lastWord = x
        elif x in dict.keys():
            if lastWord in dict[x].keys():
                i = dict[x][lastWord]+1
                dict[x].update({lastWord:i})
            else:
                dict[x].update({lastWord:1})
            lastWord = x
        elif any(o in x for o in punctmarks) or Utils.checkNum(x):
            lastWord = ""
        else:
            dict[x] = {lastWord:1}
            lastWord = x
    return dict

def trainCorpus(name, allowed, corpus):
    result = corpus
    for file in os.listdir('../ressources'):
        if file.startswith('texto'):
            s = Utils.flatListOfStrings(Utils.readFileToString('../ressources/' + file))
            if name == 'lettersUnigram':
                result = getCaracteresUnigram(s, allowed, result)
            elif name == 'lettersBigram':
                result = getCaracteresBigram(s, allowed, result)
            elif name == 'wordsUnigram':
                result = getPalabrasUnigram(s, result)
            elif name == 'wordsBigram':
                result = getPalabrasBigram(s, result)
    return result