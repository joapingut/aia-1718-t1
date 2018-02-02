# -*- coding: utf-8 -*-
__author__ = 'Joaquin, Luis'

import pickle, os

CORPUS_NAMES_PATH = {'lettersUnigram':'lettersUnigram.pkl', 'lettersBigram':'lettersBigram.pkl', 'wordsUnigram':'wordsUnigram.pkl', 'wordsBigram':'wordsBigram.pkl'}

RESSOURCES_PATH = '../ressources/'

def getCorpusPath(name):
    global RESSOURCES_PATH, CORPUS_NAMES_PATH
    return RESSOURCES_PATH + CORPUS_NAMES_PATH[name]

def existCorpus(name):
    if name not in CORPUS_NAMES_PATH:
        return False
    return os.path.isfile(RESSOURCES_PATH + CORPUS_NAMES_PATH[name])

def saveCorpus(name, corpus):
    f = open(getCorpusPath(name),"wb")
    pickle.dump(corpus,f)
    f.close()

def loadCorpus(name):
    corpus = {}
    if not existCorpus(name):
        return corpus
    f = open(getCorpusPath(name),"rb")
    corpus = pickle.load(f)
    f.close()
    return corpus
