# -*- coding: utf-8 -*-
__author__ = 'Joaquin, Luis'

import core.utils as Utils
import corpus.corpus as Corpus
import predictor.unigram as Unigram
import predictor.bigram as Bigram
import corpus.persistence as Persistence


masc = None

unigram_letter = None
bigram_letter = None
unigram_word = None
bigram_word = None

def initializer(train=False):
    print('Hello, loading predictor')
    global masc,unigram_letter, bigram_letter, unigram_word, bigram_word
    masc = Utils.readLettersMasc('../ressources/letters.txt')
    allowed_chars = Utils.extractAllowedChars(masc)

    changes = False

    letters_corpus = {}
    if not train:
        letters_corpus = Persistence.loadCorpus("lettersUnigram")
    if len(letters_corpus) == 0:
        letters_corpus = Corpus.getCaracteresUnigram(Utils.flatListOfStrings(Utils.readFileToString('../ressources/default.txt')), allowed_chars)
        changes = True

    word_corpus = {}
    if not train:
        word_corpus = Persistence.loadCorpus("wordsUnigram")
    if len(word_corpus) == 0:
        word_corpus = Corpus.getPalabrasUnigram(Utils.flatListOfStrings(Utils.readFileToString('../ressources/default.txt')))
        changes = True

    relation_letters_corpus = {}
    if not train:
        relation_letters_corpus = Persistence.loadCorpus("lettersBigram")
    if len(relation_letters_corpus) == 0:
        relation_letters_corpus = Corpus.getCaracteresBigram(Utils.flatListOfStrings(Utils.readFileToString('../ressources/default.txt')), allowed_chars)
        changes = True

    relation_words_corpus = {}
    if not train:
        relation_words_corpus = Persistence.loadCorpus("wordsBigram")
    if len(relation_words_corpus) == 0:
        relation_words_corpus = Corpus.getPalabrasBigram(Utils.flatListOfStrings(Utils.readFileToString('../ressources/default.txt')))
        changes = True

    if train:
        changes = True
        letters_corpus = Corpus.trainCorpus("lettersUnigram", allowed_chars, letters_corpus)
        word_corpus = Corpus.trainCorpus("wordsUnigram", allowed_chars, word_corpus)
        relation_letters_corpus = Corpus.trainCorpus("lettersBigram", allowed_chars, relation_letters_corpus)
        relation_words_corpus = Corpus.trainCorpus("wordsBigram", allowed_chars, relation_words_corpus)

    if changes:
        Persistence.saveCorpus("lettersUnigram", letters_corpus)
        Persistence.saveCorpus("wordsUnigram", word_corpus,)
        Persistence.saveCorpus("lettersBigram", relation_letters_corpus)
        Persistence.saveCorpus("wordsBigram", relation_words_corpus)

    unigram_letter = Unigram.LettersUnigram(masc, letters_corpus)
    bigram_letter = Bigram.Bigram(masc, relation_letters_corpus, unigram_letter)
    unigram_word = Unigram.WordUnigram(masc, word_corpus, bigram_letter, True)
    bigram_word = Bigram.Bigram(masc, relation_words_corpus, unigram_word)

    print('System loaded')


def predictLetterUnigram(text, translate=False, random=False, accuracy=False):
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
        predicted = ' '.join(result)
    print("Prediction: ", predicted)
    if translate and accuracy:
        print("Accuracy: ", Utils.checkApproximation(text.lower(), predicted))

def predictWordUnigram(text, translate=False, random=False, accuracy=False):
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
        predicted = ' '.join(result)
    print("Prediction: ", predicted)
    if translate and accuracy:
        print("Accuracy: ", Utils.checkApproximation(text.lower(), predicted))

def predictLetterBigram(text, translate=False, random=False, accuracy=False):
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
    predicted = ' '.join(result)
    print("Prediction: ", predicted)
    if translate and accuracy:
        print("Accuracy: ", Utils.checkApproximation(text.lower(), predicted))


def predictWordBigram(text, translate=False, random=False, accuracy=False):
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
    predicted = ' '.join(result)
    print("Prediction: ", predicted)
    if translate and accuracy:
        print("Accuracy: ", Utils.checkApproximation(text.lower(), predicted))


initializer(True)
print('Examples of use')
predictLetterUnigram("Esto es un ejemplo", True, accuracy=True)
predictLetterBigram("Esto es un ejemplo", True, accuracy=True)
predictWordUnigram("Esto es un ejemplo", True, accuracy=True)
predictWordBigram("Esto es un ejemplo", True, accuracy=True)
print("Random choices enabled")
predictLetterUnigram("Esto es un ejemplo", True, True, True)
predictLetterBigram("Esto es un ejemplo", True, True, True)
predictWordUnigram("Esto es un ejemplo", True, True, True)
predictWordBigram("Esto es un ejemplo", True, True, True)
