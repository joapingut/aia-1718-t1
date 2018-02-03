# -*- coding: utf-8 -*-
__author__ = 'Joaquin, Luis'

import random, operator
import core.utils as Utils


class LettersUnigram:

    def __init__(self, masc, corpus):
        self.corpus = corpus
        self.masc = masc
        self.information = createLettersUnigramFromCorpus(masc, corpus)

    def predict(self, value, is_random = False):
        if (value in self.information):
            info = self.information[value]
            if(not is_random):
                return info[0][0]
            else:
                return Utils.getRandomValue(info)
        else:
            return random.choice(self.masc[value])


class WordUnigram:

    def __init__(self, masc, wordcorpus, lettersGram, isLetterBi=False):
        self.corpus = wordcorpus
        self.masc = masc
        self.lettersGram = lettersGram
        self.isLetterBi = isLetterBi
        self.information = createWordsUnigramFromCorpus(masc, wordcorpus)

    def predict(self, value, random = False):
        if (value in self.information):
            info = self.information[value]
            if(not random):
                return info[0][0]
            else:
                return Utils.getRandomValue(info)
        else:
            result = ''
            previous = ''
            for letter in value:
                elected = None
                if self.isLetterBi:
                    elected = self.lettersGram.predict(previous, letter, random)
                else:
                    elected = self.lettersGram.predict(letter, random)
                result += elected
                previous = elected
            return result


'''
Crea un predictor unigram a partir del corpus y la mascara dada.

El formato que devuelve es el siguiente:

masc = {1:(a,b), 2:(c,d)}
corpus = {a:2, b:3, c:4, d:5}

return {1:((b:3/5), (a:2/5)), 2:((d:5/9),(c:4/9))}

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

'''
Crea un predictor unigram a partir del corpus y la mascara dada.

El formato que devuelve es el siguiente:

masc = {1:(a,b), 2:(c,d)}
corpus = {abba:2, baba:3, caca:4, dada:5}

return {1111:[(baba:3), (abba:2)], 2121:[(dada:5),(caca:4)]}

Notese que devuelve un diccionario en el que las claves son la traduccion que corresponde a los valores y el valor son una lista de tuplas
en la que el primer elemento de esa tupla es un elemento del corpus y el segundo es las veces que aparece el mismo asociados a dicha
traducción numerica.

Dentro de cada lista de tuplas estas están ordenadas de mayor a menor, es decir, si el elemento b tiene mas incidencias
que el elemento a, b saldra primero.
'''
def createWordsUnigramFromCorpus(masc, corpus):
    sorted_corpus = sorted(corpus.items(), key=operator.itemgetter(1), reverse=True)
    result = {}
    for corpus_pair in sorted_corpus:
        word = corpus_pair[0]
        translation = Utils.translateWord(masc, word)
        if translation in result:
            info = result.get(translation)
            info.append(corpus_pair)
            result[translation] = info
        else:
            info = [corpus_pair,]
            result[translation] = info
    return result