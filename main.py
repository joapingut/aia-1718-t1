# -*- coding: utf-8 -*-
__author__ = 'Joaquin, Luis'

import core.initializer as Init

Init.RESSOURCES_PATH = 'ressources/'

Init.initializer(False)

print('Running Main')

while(True):
    text = input('Please, write a phrase: ')
    if text == '-!':
        print("Goodbye")
        break;
    print("Here is the result: ")
    Init.predictWordBigram(text, True, False, accuracy=True)
    print("Here is the random result: ")
    Init.predictWordBigram(text, True, True, accuracy=True)
    print()
