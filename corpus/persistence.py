# -*- coding: utf-8 -*-
__author__ = 'Joaquin, Luis'

import pickle, os

CORPUS_NAMES_PATH = {'lettersUnigram':'lettersUnigram.pkl', 'lettersBigram':'lettersBigram.pkl', 'wordsUnigram':'wordsUnigram.pkl', 'wordsBigram':'wordsBigram.pkl'}

RESSOURCES_PATH = '../ressources/'

'''
Dado el nombre de un corpus, devuelve la ruta donde se guarda su pkl.
'''
def getCorpusPath(name):
    global RESSOURCES_PATH, CORPUS_NAMES_PATH
    return RESSOURCES_PATH + CORPUS_NAMES_PATH[name]

'''
Dado el nombre de un corpus, comprueba si existe un archivo pkl asociado al mismo.
'''
def existCorpus(name):
    if name not in CORPUS_NAMES_PATH:
        return False
    return os.path.isfile(RESSOURCES_PATH + CORPUS_NAMES_PATH[name])

'''
Dado la informacion estadistica de corpus contenida en un diccionario, almacena dicha informacion en un archivo asosciado
segun el nombre pasado como parametro.
'''
def saveCorpus(name, corpus):
    f = open(getCorpusPath(name),"wb")
    pickle.dump(corpus,f)
    f.close()

'''
Dado el nombre de un corpus devuelve la informacion asociada en el pkl previament almacenado o un diccionario vacio
si no hay archivo.
'''
def loadCorpus(name):
    corpus = {}
    if not existCorpus(name):
        return corpus
    f = open(getCorpusPath(name),"rb")
    corpus = pickle.load(f)
    f.close()
    return corpus
