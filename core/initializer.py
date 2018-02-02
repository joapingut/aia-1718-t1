# -*- coding: utf-8 -*-
__author__ = 'Joaquin, Luis'

import core.utils as Utils
import corpus.corpus as Corpus
import predictor.unigram as Unigram
import predictor.bigram as Bigram


masc = None

unigram_letter = None
bigram_letter = None
unigram_word = None
bigram_word = None

def initializer():
    print('Hello, loading predictor')
    global masc,unigram_letter, bigram_letter, unigram_word, bigram_word
    masc = Utils.readLettersMasc('../ressources/letters.txt')
    allowed_chars = Utils.extractAllowedChars(masc)
    letters_corpus = Corpus.getCaracteresUnigram(Utils.flatListOfStrings(Utils.readFileToString('../ressources/texto1.txt')), allowed_chars)
    word_corpus = Corpus.getPalabrasUnigram(Utils.flatListOfStrings(Utils.readFileToString('../ressources/texto1.txt')))

    relation_letters_corpus = Corpus.getCaracteresBigram(Utils.flatListOfStrings(Utils.readFileToString('../ressources/texto1.txt')), allowed_chars)
    relation_words_corpus = Corpus.getPalabrasBigram(Utils.flatListOfStrings(Utils.readFileToString('../ressources/texto1.txt')))

    unigram_letter = Unigram.LettersUnigram(masc, letters_corpus)
    bigram_letter = Bigram.Bigram(masc, relation_letters_corpus, unigram_letter)
    unigram_word = Unigram.WordUnigram(masc, word_corpus, bigram_letter, True)
    bigram_word = Bigram.Bigram(masc, relation_words_corpus, unigram_word)

    print('System loaded')


def predictLetterUnigram(text, translate=False, random=False):
    print('Using Letters unigram')
    global masc,unigram_letter, bigram_letter, unigram_word, bigram_word
    string = None
    if translate:
        string = Utils.translatePhrase(masc, text.lower())
    else:
        string = text.lower()
    print("Phrase: ", string)
    words = string.split(' ')
    result = []
    for word in words:
        aux = ''
        for letter in word:
            aux += unigram_letter.predict(letter, random)
        result.append(aux)
    print("Prediction: ", ' '.join(result))

def predictWordUnigram(text, translate=False, random=False):
    print('Using words unigram')
    global masc,unigram_letter, bigram_letter, unigram_word, bigram_word
    string = None
    if translate:
        string = Utils.translatePhrase(masc, text.lower())
    else:
        string = text.lower()
    print("Phrase: ", string)
    words = string.split(' ')
    result = []
    for word in words:
        result.append(unigram_word.predict(word, random))
    print("Prediction: ", ' '.join(result))

def predictLetterBigram(text, translate=False, random=False):
    print('Using Letters bigram')
    global masc,unigram_letter, bigram_letter, unigram_word, bigram_word
    string = None
    if translate:
        string = Utils.translatePhrase(masc, text.lower())
    else:
        string = text.lower()
    print("Phrase: ", string)
    words = string.split(' ')
    result = []
    for word in words:
        aux = ''
        last = ''
        for letter in word:
            aux += bigram_letter.predict(last, letter, random)
            last = letter
        result.append(aux)
    print("Prediction: ", ' '.join(result))


def predictWordBigram(text, translate=False, random=False):
    print('Using words bigram')
    global masc,unigram_letter, bigram_letter, unigram_word, bigram_word
    string = None
    if translate:
        string = Utils.translatePhrase(masc, text.lower())
    else:
        string = text.lower()
    print("Phrase: ", string)
    words = string.split(' ')
    result = []
    last = ''
    for word in words:
        result.append(bigram_word.predict(last, word, random))
        last = word
    print("Prediction: ", ' '.join(result))


initializer()
print('Examples of use')
predictLetterUnigram("Esto es un ejemplo", True)
predictLetterBigram("Esto es un ejemplo", True)
predictWordBigram("Esto es un ejemplo", True)
predictWordBigram("Esto es un ejemplo", True)
print("Random choices enabled")
predictLetterUnigram("Esto es un ejemplo", True, True)
predictLetterBigram("Esto es un ejemplo", True, True)
predictWordBigram("Esto es un ejemplo", True, True)
predictWordBigram("Esto es un ejemplo", True, True)
