# -*- coding: utf-8 -*-
__author__ = 'Joaquin, Luis'

import core.utils as Utils
import core.initializer as Init

Init.RESSOURCES_PATH = 'ressources/'

Init.initializer(False)

masc = Init.masc
unigram_letter = Init.unigram_letter
bigram_letter = Init.bigram_letter
unigram_word = Init.unigram_word
bigram_word = Init.bigram_word

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