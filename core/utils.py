__author__ = 'Joaquin'


import operator, random

'''

Crea un predictor unigram a partir del corpus y la mascara dada.

El formato que devuelve es el siguiente:

masc = {1:(a,b), 2:(c,d)}
corpus = {a:2, b:3, c:4, d:5}

return {1:((b:3), (a:2)), 2:((d:5),(c:4))}

Notese que devuelve un diccionario en el que las claves son las mismas de la mascara y los valores son una lista de tuplas
en la que el primer elemento de esa tupla es un elemento del corpus y el segundo es las veces que aparece el mismo.

Dentro de cada lista de tuplas estas están ordenadas de mayor a menor, es decir, si el elemento b tiene mas incidencias
que el elemento a, b saldra primero.

'''
def createLettersUnigramFromCorpus(masc, corpus):
    sorted_corpus = sorted(corpus.items(), key=operator.itemgetter(1), reverse=True)
    result = {}
    for corpus_pair in sorted_corpus:
        for masc_key in masc:
            masc_value = masc.get(masc_key)
            corpus_key = corpus_pair[0]
            corpus_value = corpus_pair[1]
            if(corpus_key in masc_value):
                if(masc_key in result):
                    value = result.get(masc_key)
                    value.append(corpus_pair)
                    result[masc_key] = value
                else:
                    result[masc_key] = [corpus_pair,]
    return result

def createWordsUnigramFromCorpus(masc, corpus):
    sorted_corpus = sorted(corpus.items(), key=operator.itemgetter(1), reverse=True)
    result = {}
    for corpus_pair in sorted_corpus:
        word = corpus_pair[0]
        translation = translateWord(masc, word)
        if translation in result:
            info = result.get(translation)
            info.append(corpus_pair)
            result[translation] = info
        else:
            info = [corpus_pair,]
            result[translation] = info
    return result


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

# TESTS

#createPredictorUnigramFromCorpus({1: ('a', 'b'), 2: ('c', 'd')}, {'a': 2, 'b': 3, 'c': 4, 'd': 5})

#getRandomValue([('b',3) ,('a',2)])

#print(translateWord({1: ('a', 'b'), 2: ('c', 'd')}, 'acdabbcbda'))

#print(createWordsUnigramFromCorpus({1: ('a', 'b'), 2: ('c', 'd')}, {'abba': 2, 'aca': 3, 'daba': 4, 'caca': 5, 'dada': 6}))

#print(readLettersMasc('../ressources/letters.txt'))