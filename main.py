# -*- coding: utf-8 -*-
__author__ = 'Joaquin, Luis'

import core.utils as Utils
import corpus.corpus as Corpus
import predictor.unigram as Unigram
import predictor.bigram as Bigram


print('Hello, loading predictor')

masc = Utils.readLettersMasc('ressources/letters.txt')
allowed_chars = Utils.extractAllowedChars(masc)
letters_corpus = Corpus.getCaracteresUnigram(Utils.flatListOfStrings(Utils.readFileToString('ressources/texto1.txt')), allowed_chars)
word_corpus = Corpus.getPalabrasUnigram(Utils.flatListOfStrings(Utils.readFileToString('ressources/texto1.txt')))

relation_letters_corpus = Corpus.getCaracteresBigram(Utils.flatListOfStrings(Utils.readFileToString('ressources/texto1.txt')), allowed_chars)
relation_words_corpus = Corpus.getPalabrasBigram(Utils.flatListOfStrings(Utils.readFileToString('ressources/texto1.txt')))

unigram_letter = Unigram.LettersUnigram(masc, letters_corpus)
bigram_letter = Bigram.Bigram(masc, relation_letters_corpus, unigram_letter)
unigram_word = Unigram.WordUnigram(masc, word_corpus, bigram_letter, True)
bigram_word = Bigram.Bigram(masc, relation_words_corpus, unigram_word)

print('System loaded')

while(True):
    text = input('Please, write a phrase: ')
    if text == '-!':
        print("Goodbye")
        break;
    text = text.lower()
    translate = Utils.translatePhrase(masc, text)
    print('Traducción: ', translate)
    words = translate.split(' ')
    result = ''
    random_result = ''
    previous = ''
    for word in words:
        predicted = bigram_word.predict(previous, word)
        random_predicted = bigram_word.predict(previous, word, True)
        result += predicted  + ' '
        random_result += random_predicted  + ' '
        previous = word
    print("Here is the result: " + result)
    print("Here is the random result: " + random_result)
    print()