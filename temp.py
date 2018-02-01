# -*- coding: utf-8 -*-

import pickle
import random
import re

def unigramLetras(s):
    
    dict = {'Python' : '.py', 'C' : '.cpp'}
    f = open("unigramletras.pkl","wb")
    pickle.dump(dict,f)
    f.close()
    
def abrirPickle(s):
    f = pickle.load(open("unigramletras.pkl","rb"))
    print(f)
    
def getCaracteresUnigram(s, allowed):
    dict = {}
    #allowed = {'a','á','b','c','d','e','é','f','g','h','i','í','j','k','l','m','n','ñ','o','ó','p','q','r','s','t','u','ú','v','w','x','y','z'}
    s = s.lower()
    for x in s:
        if x in dict.keys():
            dict[x] += 1
        elif x in allowed:
            dict[x] = 1
    return dict

def getPalabrasUnigram(s):
    dict = {}
    s = s.lower()
    s = re.sub(r'[0-9]+','',s)
    string = re.findall(r'\w+',s)
    for x in string:
        if x in dict.keys():
            dict[x] += 1
        else:
            dict[x] = 1
    return dict

def getCaracteresBigram(s, allowed):
    dict = {}
    punctmarks = ["(",")","¡","!","¿","?",":",";","@","#",",","."," "]
    #allowed = {'a','á','b','c','d','e','é','f','g','h','i','í','j','k','l','m','n','ñ','o','ó','p','q','r','s','t','u','ú','v','w','x','y','z'}
    s = s.lower()
    lastChar = ""
    for x in s:
        if lastChar == "" and x in allowed:
            lastChar = x
        elif x in dict.keys():
            if lastChar in dict[x].keys():
                i = dict[x][lastChar]+1
                dict[x].update({lastChar:i})
            else:
                dict[x].update({lastChar:1})
            lastChar = x
        elif x in punctmarks:
            lastChar = ""
        elif x in allowed:
            dict[x] = {lastChar:1}
            lastChar = x
    return dict

def checkNum(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
        
def getPalabrasBigram(s):
    dict = {}
    punctmarks = ["(",")","¡","!","¿","?",":",";","@","#",",","."," ","..."]
    s = s.lower()
    string = re.findall(r"[A-záéíóú]+|[1-9]+|[\.)(?¿!¡:;@#,]+", s, re.DOTALL | re.IGNORECASE)
    lastWord = ""
    for x in string:
        if lastWord == "" and x not in punctmarks:
            lastWord = x
        elif x in dict.keys():
            if lastWord in dict[x].keys():
                i = dict[x][lastWord]+1
                dict[x].update({lastWord:i})
            else:
                dict[x].update({lastWord:1})
            lastWord = x
        elif any(o in x for o in punctmarks) or checkNum(x):
            lastWord = ""
        #elif not checkNum(x) and not any(o in x for o in punctmarks):
        else:
            dict[x] = {lastWord:1}
            lastWord = x
    return dict

def checkApproximation(s,r):
    i = 0
    res = 0
    for x in s:
        if s[i]==r[i]:
            res += 1
        i += 1
    res = (res/len(s))*100
    return str(res)+" %"

def guardarUnigramPalabras(s):
    dict = getPalabrasUnigram(s)
    result = {}
    optionsRev = {'a':1,'á':1,'b':1,'c':1,'d':2,'e':2,'é':2,'f':2,'g':3,'h':3,'i':3,'í':3,'j':4,'k':4,'l':4,'m':5,'n':5,'ñ':5,'o':5,'ó':5,'p':6,'q':6,'r':6,'s':6,'t':7,'u':7,'ú':7,'v':7,'w':8,'x':8,'y':8,'z':8}
    for x in dict:
        string = ""
        for y in x:
            if y in optionsRev.keys():
                string += str(optionsRev[y])
        if string in result.keys():
            if x in result[string].keys():
                i = result[string][x]
                result[string].update({x:i})
            else:
                result[string].update({x:dict[x]})
        else:
            result[string]={x:dict[x]}
    return result

def guardarUnigramLetras(s):
    dict = getCaracteresUnigram(s)
    result = {1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{}}
    options = {1:{'a','á','b','c'},2:{'d','e','é','f'},3:{'g','h','i','í'},4:{'j','k','l'},5:{'m','n','ñ','o','ó'},6:{'p','q','r','s'},7:{'t','u','ú','v'},8:{'w','x','y','z'}}
    for x in dict.keys():
        for y in options.keys():
            if x in options[y] and x in result[y].keys():
                i = result[y][x]+dict[x]
                result[y].update({x:i})
            elif x in options[y] and not x in result[y].keys():
                result[y].update({x:dict[x]})
    
    return result

def pruebaLetras(s,e):
    dict = guardarUnigramLetras(e)
    result = ""
    for x in s:
        if x == (' ' or ',' or '.' or ';'):
            result = result+x
        else:
            max = sum([dict[int(x)][c] for c in dict[int(x)]])
            print(max)
            print(dict)
            pick = random.uniform(0,max)
            print(pick)
            current = 0
            for y in dict[int(x)]:
                current += dict[int(x)][y]
                if current > pick:
                    result = result+y
                    break
    return result

def pruebaPalabras(s,e):
    dict = guardarUnigramPalabras(e)
    result = ""
    s = s.split(" ")
    for x in s:
        if x in dict.keys():
            max = sum([dict[x][c] for c in dict[x]])
            pick = random.uniform(0,max)
            current = 0
            for y in dict[x]:
                current += dict[x][y]
                if current > pick:
                    result = result+y
                    break
            result += " "
        else:
            result += pruebaLetras(x,e)+" "
    return result