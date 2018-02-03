# -*- coding: utf-8 -*-
__author__ = 'Joaquin, Luis'

import re, os
import core.utils as Utils

'''
Metodo que recupera del texto s toda la informacion para generar un corpus para el unigram de letras,
    s: es el texto
    allowed: es una lista con los caracteres permitidos
    corpus: diccionario en blanco u otro diccionario que ya posea informacion si se desea agregar otro corpus a la misma

    resultado = {a:2, b:3, c:4, d:5}
'''
def getCaracteresUnigram(s, allowed, corpus={}):
    dict = corpus
    s = s.lower()
    for x in s:
        if x in dict.keys():
            dict[x] += 1
        elif x in allowed:
            dict[x] = 1
    return dict

'''
Metodo que recupera del texto s toda la informacion para generar un corpus para el unigram de palabras,
    s: es el texto
    corpus: diccionario en blanco u otro diccionario que ya posea informacion si se desea agregar otro corpus a la misma

    resultado = {aaa:2, bas:3, caca:4, daba:5}
'''
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

'''
Metodo que recupera del texto s toda la informacion para generar un corpus para el bigram de letras,
    s: es el texto
    allowed: es una lista con los caracteres permitidos
    corpus: diccionario en blanco u otro diccionario que ya posea informacion si se desea agregar otro corpus a la misma

    resultado = {'a':{'p':8, 'c':7}}
'''
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

'''
Metodo que recupera del texto s toda la informacion para generar un corpus para el bigram de palabras,
    s: es el texto
    corpus: diccionario en blanco u otro diccionario que ya posea informacion si se desea agregar otro corpus a la misma

    resultado = {'asd':{papa:8, 'caca':7}}
'''
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

'''
Metodo para agregar a un corpus toda la informacion de los textos contenidos en la carpeta ressources que empiecen
por texto.
    name: nombre del corpus a entrenar, lettersUnigram, lettersBigram, wordsUnigram, wordsBigram
    allowed: lista de caractres permitidos, si se ba a entrar un n-gram de palabras se puede ignorar y pasar cualquier valor
    corpus: el corpus que se quiere entrenar o un diccionario vacio si no hay datos.

resultado: el corpus con la nueva informacion.
'''
def trainCorpus(name, allowed, corpus, path='../ressources/'):
    result = corpus
    for file in os.listdir(path):
        if file.startswith('texto'):
            s = Utils.flatListOfStrings(Utils.readFileToString(path + file))
            if name == 'lettersUnigram':
                result = getCaracteresUnigram(s, allowed, result)
            elif name == 'lettersBigram':
                result = getCaracteresBigram(s, allowed, result)
            elif name == 'wordsUnigram':
                result = getPalabrasUnigram(s, result)
            elif name == 'wordsBigram':
                result = getPalabrasBigram(s, result)
    return result