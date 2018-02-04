# -*- coding: utf-8 -*-
__author__ = 'Joaquin, Luis'

import core.initializer as Init
from tkinter import *
from tkinter import ttk


Init.RESSOURCES_PATH = 'ressources/'

Init.initializer(False)

print('Running Main')

class Interface():
    def __init__(self):
        
        self.raiz = Tk()
        self.raiz.geometry('500x450')
        
        self.raiz.resizable(width=False,height=False)
        self.raiz.title('Predictor')
        
        self.etiq1 = ttk.Label(self.raiz, text="Please, write a phrase:")
        self.etiq2 = ttk.Label(self.raiz, text="Input phrase:")
        self.etiq3 = ttk.Label(self.raiz, text="Here is the result:")
        self.etiq4 = ttk.Label(self.raiz, text="Here is the random result:")
       
        self.tinfo = Text(self.raiz, width=60, height=5)
        self.tinfo2 = Text(self.raiz, width=60, height=5)
        self.tinfores = Text(self.raiz, width=60, height=5)
        self.tinforandomres = Text(self.raiz, width=60, height=5)
        
        
        self.etiq1.pack(side=TOP)
        self.tinfo.pack(side=TOP)
        self.etiq2.pack(side=TOP)
        self.tinfo2.pack(side=TOP)
        self.etiq3.pack(side=TOP)
        self.tinfores.pack(side=TOP)
        self.etiq4.pack(side=TOP)
        self.tinforandomres.pack(side=TOP)
        
        self.bbw = ttk.Button(self.raiz, text='Bigram words', command=self.bigramWords)
        self.bbl = ttk.Button(self.raiz, text='Bigram letters', command=self.bigramLetters)
        self.buw = ttk.Button(self.raiz, text='Unigram words', command=self.unigramWords)
        self.bul = ttk.Button(self.raiz, text='Unigram letters', command=self.unigramLetters)
        
        self.bbw.pack(side=LEFT)
        self.bbl.pack(side=LEFT)
        self.buw.pack(side=LEFT)
        self.bul.pack(side=LEFT)
        
        self.bexit = ttk.Button(self.raiz, text='Exit', command=self.raiz.destroy)
        self.bexit.pack(side=RIGHT)
        
        self.tinfo2.config(state=DISABLED)
        self.tinfores.config(state=DISABLED)
        self.tinforandomres.config(state=DISABLED)
        
        self.bbw.focus_set()
        self.raiz.mainloop()
    
    def bigramWords(self):
        self.tinfo2.config(state=NORMAL)
        self.tinfores.config(state=NORMAL)
        self.tinforandomres.config(state=NORMAL)
        
        self.tinfo2.delete("1.0", END)
        self.tinfores.delete("1.0", END)
        self.tinforandomres.delete("1.0", END)
        
        texto = self.tinfo.get("1.0",'end-1c')
        
        res = Init.predictWordBigram(texto, True, False, accuracy=True)
        randomres = Init.predictWordBigram(texto, True, True, accuracy=True)
        
        self.tinfo2.insert("1.0", texto)
        self.tinfores.insert("1.0",res)
        self.tinforandomres.insert("1.0",randomres)
        
        self.tinfo2.config(state=DISABLED)
        self.tinfores.config(state=DISABLED)
        self.tinforandomres.config(state=DISABLED)
        
    def bigramLetters(self):
        self.tinfo2.config(state=NORMAL)
        self.tinfores.config(state=NORMAL)
        self.tinforandomres.config(state=NORMAL)
        
        self.tinfo2.delete("1.0", END)
        self.tinfores.delete("1.0", END)
        self.tinforandomres.delete("1.0", END)
        
        texto = self.tinfo.get("1.0",'end-1c')
        
        res = Init.predictLetterBigram(texto, True, False, accuracy=True)
        randomres = Init.predictLetterBigram(texto, True, True, accuracy=True)

        self.tinfo2.insert("1.0", texto)
        self.tinfores.insert("1.0",res)
        self.tinforandomres.insert("1.0",randomres)
        
        self.tinfo2.config(state=DISABLED)
        self.tinfores.config(state=DISABLED)
        self.tinforandomres.config(state=DISABLED)
    
    def unigramWords(self):
        self.tinfo2.config(state=NORMAL)
        self.tinfores.config(state=NORMAL)
        self.tinforandomres.config(state=NORMAL)
        
        self.tinfo2.delete("1.0", END)
        self.tinfores.delete("1.0", END)
        self.tinforandomres.delete("1.0", END)
        
        texto = self.tinfo.get("1.0",'end-1c')
        
        res = Init.predictWordUnigram(texto, True, False, accuracy=True)
        randomres = Init.predictWordUnigram(texto, True, True, accuracy=True)
        
        self.tinfo2.insert("1.0", texto)
        self.tinfores.insert("1.0",res)
        self.tinforandomres.insert("1.0",randomres)
        
        self.tinfo2.config(state=DISABLED)
        self.tinfores.config(state=DISABLED)
        self.tinforandomres.config(state=DISABLED)
        
    def unigramLetters(self):
        self.tinfo2.config(state=NORMAL)
        self.tinfores.config(state=NORMAL)
        self.tinforandomres.config(state=NORMAL)
        
        self.tinfo2.delete("1.0", END)
        self.tinfores.delete("1.0", END)
        self.tinforandomres.delete("1.0", END)
        
        texto = self.tinfo.get("1.0",'end-1c')
        
        res = Init.predictLetterUnigram(texto, True, False, accuracy=True)
        randomres = Init.predictLetterUnigram(texto, True, True, accuracy=True)
        
        self.tinfo2.insert("1.0", texto)
        self.tinfores.insert("1.0",res)
        self.tinforandomres.insert("1.0",randomres)
        
        self.tinfo2.config(state=DISABLED)
        self.tinfores.config(state=DISABLED)
        self.tinforandomres.config(state=DISABLED)

def main():
    app = Interface()
    return 0

if __name__ == '__main__':
    main()
    