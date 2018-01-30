# -*- coding: utf-8 -*-
__author__ = 'Joaquin'


import core.utils as Utils
import predictor.unigram as Unigram
import predictor.bigram as Bigram

# TESTS

masc = {'1':( 'a', 'b', 'c'),
'2': ('d', 'e', 'f'),
'3': ('g', 'h', 'i'),
'4': ('j', 'k', 'l'),
'5': ('m', 'n', 'o'),
'6': ('p', 'q', 'r', 's'),
'7': ('t', 'u', 'v'),
'8': ('w', 'x', 'y', 'z')}

unigramlee = Unigram.LettersUnigram(masc, {'a': 2, 'b': 3, 'c': 4, 'd': 5})

bigramlee = Bigram.Bigram(masc, {'a':{'s':8, 'e':7}}, unigramlee)

unigramWord = Unigram.WordUnigram(masc, {'abba': 2, 'aca': 3, 'daba': 4, 'caca': 5, 'dada': 6}, bigramlee, True)

bigramWord = Bigram.Bigram(masc, {'de':{'mayor':8, 'casa':3}}, unigramWord)


print(bigramWord.predict('de', '4587'))
print(bigramWord.predict('de', '4587', True))

# END TEST

# TESTS

#createPredictorUnigramFromCorpus({1: ('a', 'b'), 2: ('c', 'd')}, {'a': 2, 'b': 3, 'c': 4, 'd': 5})

#getRandomValue([('b',3) ,('a',2)])

#print(translateWord({1: ('a', 'b'), 2: ('c', 'd')}, 'acdabbcbda'))

#print(createWordsUnigramFromCorpus({1: ('a', 'b'), 2: ('c', 'd')}, {'abba': 2, 'aca': 3, 'daba': 4, 'caca': 5, 'dada': 6}))

#print(readLettersMasc('../ressources/letters.txt'))