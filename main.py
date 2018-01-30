# -*- coding: utf-8 -*-
__author__ = 'Joaquin'

import core.utils as Utils
import predictor.unigram as Unigram
import predictor.bigram as Bigram


print('Hello, loading predictor')

masc = Utils.readLettersMasc('ressources/letters.txt')
letters_corpus = {'a': 103, 'b': 87, 'c': 46, 'd': 99, 'e':120,'f':88,'g':76,'h':57,'i':76,'j':88,'k':12,'l':98,'m':67,'n':54,'ñ':36,'o':78,'p':55,'q':45,'r':98,'s':78,'t':54,'u':56,'v':10,'w':1,'x':2,'y':7,'z':5,'á':1,'é':1,'í':1,'ó':1,'ú':1}
word_corpus = {'abba': 2, 'aca': 3, 'daba': 4, 'caca': 5, 'dada': 6}

relation_letters_corpus = {'a':{'s':8, 'e':7}}
relation_words_corpus = {'de':{'mayor':8, 'casa':3}}

unigram_letter = Unigram.LettersUnigram(masc, letters_corpus)
bigram_letter = Bigram.Bigram(masc, relation_letters_corpus, unigram_letter)
unigram_word = Unigram.WordUnigram(masc, word_corpus, bigram_letter, True)
bigram_word = Bigram.Bigram(masc, relation_words_corpus, unigram_word)

print('System loaded')

while(True):
    text = input('Please, write a phrase: ')
    words = text.split(' ')
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
