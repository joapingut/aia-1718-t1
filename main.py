__author__ = 'Joaquin'

import core.utils as Utils
import predictor.unigram as Unigram


print('Hello, loading predictor')

masc = Utils.readLettersMasc('ressources/letters.txt')
letters_corpus = {'a': 103, 'b': 87, 'c': 46, 'd': 99, 'e':120,'f':88,'g':76,'h':57,'i':76,'j':88,'k':12,'l':98,'m':67,'n':54,'ñ':36,'o':78,'p':55,'q':45,'r':98,'s':78,'t':54,'u':56,'v':10,'w':1,'x':2,'y':7,'z':5,'á':1,'é':1,'í':1,'ó':1,'ú':1}
word_corpus = {'abba': 2, 'aca': 3, 'daba': 4, 'caca': 5, 'dada': 6}

unigram_prd = Unigram.WordUnigram(masc, word_corpus, letters_corpus)

print('System loaded')

while(True):
    text = input('Please, write a phrase: ')
    words = text.split(' ')
    result = ''
    random_result = ''
    for word in words:
        result += unigram_prd.predict(word) + ' '
        random_result += unigram_prd.predict(word, True) + ' '
    print("Here is the result: " + result)
    print("Here is the random result: " + random_result)
    print()
