# -*- coding: utf-8 -*-
__author__ = 'Joaquin, Luis'


import operator, random, math


'''
Función para traducir una frase de lenguaje natural separada por espacios al código númerico codificado
en el párametro masc.

Ej: si masc = {'1':[a,b]} y phrase = 'aabbaa bbba' resultado = 111111 1111
'''
def translatePhrase(masc, phrase):
    words =phrase.split(' ')
    translations = []
    for word in words:
        translations.append(translateWord(masc, word))
    return ' '.join(translations)


'''
Función para traducir una palabra de lenguaje natural al código númerico codificado
en el párametro masc.

Ej: si masc = {'1':[a,b]} y phrase = 'aabbaa' resultado = 111111
'''
def translateWord(masc, word):
    result = ''
    for letter in word:
        for masc_key in masc:
            if letter in masc.get(masc_key):
                result += str(masc_key)
    return result

'''
Dada una lista de valores asociados a un peso, elige de forma aleatoria uno de esa lista.

Ej: list = [('a',1)('b',2)] resultado = 'b'
'''
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


'''
Dada la ruta al archivo con la codificacion de los caracteres esta funcion devuelve un diccionario de listas
con esa codificación.

Ej path = 'c:/test/codigo.txt' resultado = {'1':('a','b','c'), '2':('d','e','f')}
'''
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

'''
Dado el mismo formato que devuelve el metodo readLettersMasc, devuelve una lista con los caracteres que se admiten.

EJ: masc = {'1':('a','b','c'), '2':('d','e','f')} resultado = [a,b,c,d,e,f]
'''
def extractAllowedChars(masc):
    return flatListOfList(list(masc.values()))

'''
Dada una lista de listas de elementos devuelve otra lista con todos los elementos de todas las listas.

EJ: things = [(a,b),(a,d)] resultado = [a,b,a,d]
'''
def flatListOfList(things):
    return [item for sublist in things for item in sublist]

'''
Dada una lista de strings devuelve otro string con los elementos de la lista separados por espacios

EJ: things = ['aaa', 'bbbb'] resultado = 'aaa bbbb'
'''
def flatListOfStrings(things):
    return ''.join(things)

'''
Dada la ruta de un archivo devuelve un string con el contenido de dicho archivo.

EJ; path = 'c:/test/texto.txt' resultado = 'texto 222'
'''
def readFileToString(path):
    file = open(path, 'r', encoding='utf8')
    return file.readlines()

'''
Devuelve una lista con los caracteres considerados signos de puntuación.
'''
def listOfPuntuationsMarks():
    return ["(",")","¡","!","¿","?",":",";","@","#",",","."," ","...", "_", "-", "[", "]", "\""]

'''
Dada dos cadenas comprueba la cercania entre ellas y devuelve el porcentaje de igualdad.
'''
def checkApproximation(original, comparation):
    longi = len(original)
    i = 0
    for index in range(0, longi):
        if original[index] == comparation[index]:
            i += 1
    return str((i/longi) * 100) + " %"

'''
Comprueba si una cadena s es un numero.
'''
def checkNum(s):
    try:
        int(s)
        return True
    except ValueError:
        return False