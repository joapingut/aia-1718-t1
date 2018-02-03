# -*- coding: utf-8 -*-
__author__ = 'Joaquin, Luis'


'''
Archivo .py para probar el sistema de predicción. Antes de nada hay que ejecutar el método initializer para cagar
los predictores. Si el parametro train se pasa como True se cogeran todos los archivos de la carpeta ressources
que empiecen por texto y el archivo default como corpus para generar la información. Si el parametro es False se
recuperará la información almacenada en los archivos pkl o si no existen se hara lo dicho anteriormete.

Cuando ya se haya ejeutado el metodo se pueden invocar los otros metodos que empiezan por predict para probar los
distintos tipos de n-gram.
'''

import core.utils as Utils
import corpus.corpus as Corpus
import predictor.unigram as Unigram
import predictor.bigram as Bigram
import corpus.persistence as Persistence


RESSOURCES_PATH = '../ressources/'

masc = None

unigram_letter = None
bigram_letter = None
unigram_word = None
bigram_word = None


'''
Metodo que inicia los predictores para que se puedan probar.
'''
def initializer(train=False):
    Persistence.RESSOURCES_PATH = RESSOURCES_PATH
    print('Hello, loading predictor')
    global masc,unigram_letter, bigram_letter, unigram_word, bigram_word
    masc = Utils.readLettersMasc(RESSOURCES_PATH + 'letters.txt')
    allowed_chars = Utils.extractAllowedChars(masc)

    changes = False

    letters_corpus = {}
    if not train:
        letters_corpus = Persistence.loadCorpus("lettersUnigram")
    if len(letters_corpus) == 0:
        letters_corpus = Corpus.getCaracteresUnigram(Utils.flatListOfStrings(Utils.readFileToString(RESSOURCES_PATH +'default.txt')), allowed_chars)
        changes = True

    word_corpus = {}
    if not train:
        word_corpus = Persistence.loadCorpus("wordsUnigram")
    if len(word_corpus) == 0:
        word_corpus = Corpus.getPalabrasUnigram(Utils.flatListOfStrings(Utils.readFileToString(RESSOURCES_PATH + 'default.txt')))
        changes = True

    relation_letters_corpus = {}
    if not train:
        relation_letters_corpus = Persistence.loadCorpus("lettersBigram")
    if len(relation_letters_corpus) == 0:
        relation_letters_corpus = Corpus.getCaracteresBigram(Utils.flatListOfStrings(Utils.readFileToString(RESSOURCES_PATH + 'default.txt')), allowed_chars)
        changes = True

    relation_words_corpus = {}
    if not train:
        relation_words_corpus = Persistence.loadCorpus("wordsBigram")
    if len(relation_words_corpus) == 0:
        relation_words_corpus = Corpus.getPalabrasBigram(Utils.flatListOfStrings(Utils.readFileToString(RESSOURCES_PATH + 'default.txt')))
        changes = True

    if train:
        changes = True
        letters_corpus = Corpus.trainCorpus("lettersUnigram", allowed_chars, letters_corpus, RESSOURCES_PATH)
        word_corpus = Corpus.trainCorpus("wordsUnigram", allowed_chars, word_corpus, RESSOURCES_PATH)
        relation_letters_corpus = Corpus.trainCorpus("lettersBigram", allowed_chars, relation_letters_corpus, RESSOURCES_PATH)
        relation_words_corpus = Corpus.trainCorpus("wordsBigram", allowed_chars, relation_words_corpus, RESSOURCES_PATH)

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


'''
Metodo para predecir utilizando el unigram de letras.
    text: es la entrada
    translate: indica si la entrada esta en formato numerico o lenguaje natural. False numerico, True natural.
    random: indica si se quiere utilizar el metodo de la ruleta en las predicciones.
    accuracy: parametro para indicar si se quiere ver el grado de cercania entre la prediccion y la frase original, solo si la entrada esta en lenguaje natural.
'''
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

'''
Metodo para predecir utilizando el unigram de palabras.
    text: es la entrada
    translate: indica si la entrada esta en formato numerico o lenguaje natural. False numerico, True natural.
    random: indica si se quiere utilizar el metodo de la ruleta en las predicciones.
    accuracy: parametro para indicar si se quiere ver el grado de cercania entre la prediccion y la frase original, solo si la entrada esta en lenguaje natural.
'''
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

'''
Metodo para predecir utilizando el bigram de letras.
    text: es la entrada
    translate: indica si la entrada esta en formato numerico o lenguaje natural. False numerico, True natural.
    random: indica si se quiere utilizar el metodo de la ruleta en las predicciones.
    accuracy: parametro para indicar si se quiere ver el grado de cercania entre la prediccion y la frase original, solo si la entrada esta en lenguaje natural.
'''
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


'''
Metodo para predecir utilizando el bigram de palabras.
    text: es la entrada
    translate: indica si la entrada esta en formato numerico o lenguaje natural. False numerico, True natural.
    random: indica si se quiere utilizar el metodo de la ruleta en las predicciones.
    accuracy: parametro para indicar si se quiere ver el grado de cercania entre la prediccion y la frase original, solo si la entrada esta en lenguaje natural.
'''
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

'''
Ejemplos de uso
'''
def test():
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
