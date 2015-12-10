#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *

def translate(word):
    word = list(word)
    for index, char in enumerate(word):
        if (index+1)<len(word): #checks if it is the last char
        			#might remove this for since I am using the same else condition 2 times
        			#I could also add the same condition on all the ifs below, but that would also be kinda bad, and I'm too lazy to fix it now
            if (char == 's') and (word[index+1]=='h'):#checking for russian letters that would use more than one latin letter
                if((index+3)<len(word) and word[index+2]=='c' and word[index+3]=='h'):
                    word[index] = u"щ"
                    del word[index+1], word[index+1], word[index+1]
                else:
                    word[index] = u"ш"
                    del word[index+1]
            elif (char == u"Y"):
                if(word[index+1]==u"A"):
                    word[index] = u"Я"
                    del word[index+1]
                elif(word[index+1]==u"U"):
                    word[index] = u"Ю"
                    del word[index+1]
            elif (char == u"y"):
                if(word[index+1]==u"a"):
                    word[index] = u"я"
                    del word[index+1]
                elif(word[index+1]==u"u"):
                    word[index] = u"ю"
                    del word[index+1]
            elif (char == 'T') and (word[index+1]=='S'):
                word[index] = u"Ц"
                del word[index+1]
            elif (char == 't') and (word[index+1]=='s'):
                word[index] = u"ц"
                del word[index+1]
            elif (char == 'C') and (word[index+1]=='H'):
                word[index] = u"Ч"
                del word[index+1]
            elif (char == 'c') and (word[index+1]=='h'):
                word[index] = u"ч"
                del word[index+1]
            elif (char == 'Z') and (word[index+1]=='H'):
                word[index] = u"Ж"
                del word[index+1]
            elif (char == 'z') and (word[index+1]=='h'):
                word[index] = u"ж"
                del word[index+1]
            else:#simple letters
                if char in lower_case_letters.keys():
                    word[index] = lower_case_letters[char]
                elif char in capital_letters.keys():
                    word[index] = capital_letters[char]
        else:#same thing for the last char
            if char in lower_case_letters.keys():
                word[index] = lower_case_letters[char]
            elif char in capital_letters.keys():
                word[index] = capital_letters[char]
    return "".join(word)#joins the list of chars so we can have the word


def onKeyPress(event):#Deletes the current text and writes the new translated one
	old = e.get()
	e.delete(0, END)
	e.insert(0,translate(old))

capital_letters = {
    u'A': u'А',
    u'B': u'Б',
    u'V': u'В',
    u'G': u'Г',
    u'D': u'Д',
    u'E': u'Е',
    u'Ë': u'Ё',
    u'ZH': u'Ж',
    u'Z': u'З',
    u'I': u'И',
    u'J': u'Й',
    u'K': u'К',
    u'L': u'Л',
    u'M': u'М',
    u'N': u'Н',
    u'O': u'О',
    u'P': u'П',
    u'R': u'Р',
    u'S': u'С',
    u'T': u'Т',
    u'U': u'У',
    u'F': u'Ф',
    u'H': u'Х',
    u'TS': u'Ц',
    u'CH': u'Ч',
    u'SH': u'Ш',
    u'SHCH': u'Щ',
    u'Y': u'Ы',        
    u'È': u'Э',
    u'YU': u'Ю',
    u'YA': u'Я' 
}

lower_case_letters = {
    u'a': u'а',
    u'b': u'б',
    u'v': u'в',
    u'g': u'г',
    u'd': u'д',
    u'e': u'е',
    u'ë': u'ё',
    u'zh': u'ж',
    u'z': u'з',
    u'i': u'и',
    u'j': u'й',
    u'k': u'к',
    u'l': u'л',
    u'm': u'м',
    u'n': u'н',
    u'o': u'о',
    u'p': u'п',
    u'r': u'р',
    u's': u'с',
    u't': u'т',
    u'u': u'у',
    u'f': u'ф',
    u'h': u'х',
    u'ts': u'ц',
    u'ch': u'ч',
    u'sh': u'ш',
    u'shch': u'щ',
    u'\"': u'ъ',
    u'y': u'ы',
    u'\'': u'ь',
    u'è': u'э',
    u'yu': u'ю',
    u'ya': u'я' 
}
    
master = Tk()

e = Entry(master)
e.pack()
e.bind("<space>", onKeyPress)#translate text everytime space is pressed
e.focus_set()                #gets keyboard focus

mainloop()


