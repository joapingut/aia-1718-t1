# -*- coding: utf-8 -*-
__author__ = 'Joaquin, Luis'

import operator, random
import core.utils as Utils

'''
Clase que define el comportamiento de un bigram.
Recibe varios parametros en su constructor:
    masc: la cofificación de los cracteres en su representación númerica.
    corpus: la información obtenida del texto del corpus que se va a usar en este bigram.
    unigram: la clase que define el unigram al que se va a recurrir en caso de no poder predecir la palabra
    uniLetter: booleano que inidica si el unigram al que se va a llamar hace la prediccion por caracteres.
'''
class Bigram:

    '''
    Constructor que inicia el bigram
    '''
    def __init__(self, masc, corpus, unigram, uniLetter=False):
        self.corpus = corpus
        self.masc = masc
        self.information = createBigramFromCorpus(masc, corpus)
        self.unigram = unigram
        self.is_unigram_letter = uniLetter

    '''
    Metodo que precide una palabra dada su representacion en forma numerica.
    Al ser un bigram requiere que se le pase la palabra que previamente le sigue en lenguaje natural y el valor a predecir
    en forma numerica.
    is_random es un parametro que activa la predicción con el uso de la ruleta. Si se deja a False se elige siempre la que
    mas veces a salido en el corpus.
    '''
    def predict(self, previous, value, is_random=False):
        if (previous in self.information):
            relations = self.information[previous]
            if(value in relations):
                info = relations[value]
                if(not is_random):
                    return info[0][0]
                else:
                    return Utils.getRandomValue(info)
        return self.unigram.predict(value, is_random)


'''
Dada la información de la codificación de los caracteres y la información sacada del texto del corpus
obtiene un nuevo diccionaio con la relacion entre un elemento y los otros que le siguen.

entrada: {'asd':{papa:8, 'caca':7}} -> significa que a 'asd' le siguen los elementos 'papa' 8 veces y 'caca' 7 veces

salida: {'asd':{4458:[('papa', 8/15), ('caca',7/15)]}} -> significa que a 'asd' le siguen los elementos codificados como 4458
que son 'papa' que aparece 8 de las 15 veces que asd tiene algo delante y 'caca' que aparece 7 de las 15.

Dentro de cada valor del diccionario con la traduccion numerica los elementos estan ordenados de mayor numero de veces de
aparicion a menor.
'''
def createBigramFromCorpus(masc, corpus):
    result = {}
    for corpus_key in corpus:
        values = corpus[corpus_key]
        relations = {}
        tam = len(values)
        for rel_key in values:
            translation = Utils.translateWord(masc, rel_key)
            value = values[rel_key] / tam
            if translation in relations:
                aux = relations[translation]
                aux.append((rel_key, value))
                aux = sorted(aux, key=operator.itemgetter(1), reverse=True)
                relations[translation] = aux
            else:
                relations[translation] = [(rel_key, value),]
        result[corpus_key] = relations
    return result

