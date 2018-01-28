__author__ = 'Joaquin'

import random
import core.utils as Utils


class LettersUnigram:

    def __init__(self, masc, corpus):
        self.corpus = corpus
        self.masc = masc
        self.information = Utils.createLettersUnigramFromCorpus(masc, corpus)

    def predict(self, value, is_random = False):
        if (value in self.information):
            info = self.information[value]
            if(not is_random):
                return info[0][0]
            else:
                return Utils.getRandomValue(info)
        else:
            return random.choice(self.masc[value])


class WordUnigram:

    def __init__(self, masc, wordcorpus, lettercorpus):
        self.corpus = wordcorpus
        self.masc = masc
        self.letterUnigram = LettersUnigram(masc, lettercorpus)
        self.information = Utils.createWordsUnigramFromCorpus(masc, wordcorpus)

    def predict(self, value, random = False):
        if (value in self.information):
            info = self.information[value]
            if(not random):
                return info[0][0]
            else:
                return Utils.getRandomValue(info)
        else:
            result = ''
            for letter in value:
                result += self.letterUnigram.predict(letter, random)
            return result


# TESTS

unigramlee = LettersUnigram({1: ('a', 'b'), 2: ('c', 'd')}, {'a': 2, 'b': 3, 'c': 4, 'd': 5})
unigramWord = WordUnigram({1: ('a', 'b'), 2: ('c', 'd')}, {'abba': 2, 'aca': 3, 'daba': 4, 'caca': 5, 'dada': 6}, {'a': 2, 'b': 3, 'c': 4, 'd': 5})

print(unigramWord.predict('1111'))
print(unigramWord.predict('2121', True))
print(unigramlee.predict(1))
print(unigramlee.predict(1, True))