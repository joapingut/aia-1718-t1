# -*- coding: utf-8 -*-
__author__ = 'Joaquin'

import operator, random
import core.utils as Utils


class Bigram:

    def __init__(self, masc, corpus, unigram, uniLetter=False):
        self.corpus = corpus
        self.masc = masc
        self.information = createBigramFromCorpus(masc, corpus)
        self.unigram = unigram
        self.is_unigram_letter = uniLetter

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
        entrada: {'asd':{papa:8, 'caca':7}}
        salida: {'asd':{4458:[('papa', 8), ('caca',7)]}}    '''
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

