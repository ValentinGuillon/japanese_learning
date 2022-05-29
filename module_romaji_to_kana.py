#module_romaji_to_kana.py
#This module have a fonction to traducts romaji input to hiragana or katagana

from module_characters_jap import *
import string

def romaji_to_hiragana(text):
    text = text.lower()
    all = string.ascii_lowercase
    vowels = "a" + "e" + "i" + "o" + "u"
    vowels_circumflex = "â" + "ê" + "î" + "ô" + "û"
    consonnes = "b" + "c" + "d" + "f" + "g" + "h" + "j" + "k" + "l" + "m" + "n" + "p" + "q" + "r" + "s" + "t" + "v" + "w" + "x" + "y" + "z"

    to_hiragana = ""
    c = "" 
    text = " " + text #c'est pour les cas où la première lettre et la dernière sont deux mêmes consonnes. Parceque dans la suite, le prog fait des vérif' sur le i-1, et si c'est la première lettre, ça va regarder la dernière lettre.
    i = 0
    for x in text:
        j = 0
        #if is "n"
        if(x == "n"): 
            #if is "n" on the last character
            if(len(text[i:]) == 1):
                j = 0
                for y in char['romaji']['all']:
                    if(y == x):
                        c = char['hiragana']['all'][j]
                        break
                    j += 1
                    
                to_hiragana += c
                #print(c)
            
            #if is "n + not vowel"
            elif(not text[i+1] in vowels and not text[i+1] in vowels_circumflex):
                j = 0
                for y in char['romaji']['all']:
                    if(y == x):
                        c = char['hiragana']['all'][j]
                        break
                    j += 1
                    
                to_hiragana += c
                #print(c)

        #if is "vowel_circumflex"
        elif(x in vowels_circumflex): 
            if(x == "â"):
                x = "a"
            elif(x == "ê"):
                x = "e"
            elif(x == "î"):
                x = "i"
            elif(x == "ô"):
                x = "o"
            elif(x == "û"):
                x = "u"

            #if is "vowel_circumflex" solo
            if(not text[i-1] in consonnes):
                j = 0
                for y in char['romaji']['all']:
                    if(y == x):
                        c = char['hiragana']['all'][j]
                        break
                    j += 1
                to_hiragana += c
                #print(c)
            
            #if is "cons + vowel_circumflex"
            elif(text[i-1] in consonnes):
                #if is "cons + cons + vowel_circumflex" and consonnes are same
                if(text[i-2] == text[i-1]):
                    c = text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    to_hiragana += hira_small_tsu + c
                    #print(c)

                #if is "cons1 + cons2 + vowel_circumflex" and cons1 is not "n"
                elif(text[i-2] in consonnes and not text[i-2] == "n"):
                    c = text[i-2] + text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    to_hiragana += c
                    #print(c)

                else:
                    c = text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    to_hiragana += c
                    #print(c)

            j = 0
            for y in char['romaji']['all']:
                if(y == x):
                    c = char['hiragana']['all'][j]
                    break
                j += 1
            to_hiragana += c


        #if is "vowel"
        elif(x in vowels): 
            #if is not "cons + vowel"
            if(not text[i-1] in consonnes):
                j = 0
                for y in char['romaji']['all']:
                    if(y == x):
                        c = char['hiragana']['all'][j]
                        break
                    j += 1
                to_hiragana += c
                #print(c)

            #if is "cons + vowel"    
            elif(text[i-1] in consonnes):
                #if is "cons + cons + vowel" and consonnes are same
                if(text[i-2] in consonnes and text[i-2] == text[i-1]): 
                    c = text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    
                    to_hiragana += hira_small_tsu + c
                    #print(c)

                #if is "cons + cons + vowel" and cons1 is not "n"
                elif(text[i-2] in consonnes and not text[i-2] == "n"): 
                    c = text[i-2] + text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    
                    to_hiragana += c
                    #print(c)
                else:
                    c = text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    to_hiragana += c
                    #print(c)

        #if is space or not a letter (!&@...)            
        elif(not x in all): 
            to_hiragana += x
            #print(x)
        i += 1
    
    to_hiragana = to_hiragana[1:] #et mtn on enlève l'espace du début
    return(to_hiragana)





def romaji_to_katagana(text):
    text = text.lower()
    all = string.ascii_lowercase
    vowels = "a" + "e" + "i" + "o" + "u"
    vowels_circumflex = "â" + "ê" + "î" + "ô" + "û"
    consonnes = "b" + "c" + "d" + "f" + "g" + "h" + "j" + "k" + "l" + "m" + "n" + "p" + "q" + "r" + "s" + "t" + "v" + "w" + "x" + "y" + "z"

    to_katagana = ""
    c = "" 
    text = " " + text #c'est pour les cas où la première lettre et la dernière sont deux mêmes consonnes. Parceque dans la suite, le prog fait des vérif' sur le i-1, et si c'est la première lettre, ça va regarder la dernière lettre.
    i = 0
    for x in text:
        j = 0
        #if is "n"
        if(x == "n"): 
            #if is "n" on the last character
            if(len(text[i:]) == 1):
                j = 0
                for y in char['romaji']['all']:
                    if(y == x):
                        c = char['katagana']['all'][j]
                        break
                    j += 1
                    
                to_katagana += c
                #print(c)
            
            #if is "n + not vowel"
            elif(not text[i+1] in vowels and not text[i+1] in vowels_circumflex):
                j = 0
                for y in char['romaji']['all']:
                    if(y == x):
                        c = char['katagana']['all'][j]
                        break
                    j += 1
                    
                to_katagana += c
                #print(c)

        #if is "vowel_circumflex"
        elif(x in vowels_circumflex): 
            if(x == "â"):
                x = "a"
            elif(x == "ê"):
                x = "e"
            elif(x == "î"):
                x = "i"
            elif(x == "ô"):
                x = "o"
            elif(x == "û"):
                x = "u"

            #if is "vowel_circumflex" solo
            if(not text[i-1] in consonnes):
                j = 0
                for y in char['romaji']['all']:
                    if(y == x):
                        c = char['katagana']['all'][j]
                        break
                    j += 1
                to_katagana += c
                #print(c)
            
            #if is "cons + vowel_circumflex"
            elif(text[i-1] in consonnes):
                #if is "cons + cons + vowel_circumflex" and consonnes are same
                if(text[i-2] == text[i-1]):
                    c = text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['katagana']['all'][j]
                            break
                        j += 1
                    to_katagana += kata_small_tsu + c
                    #print(c)

                #if is "cons1 + cons2 + vowel_circumflex" and cons1 is not "n"
                elif(text[i-2] in consonnes and not text[i-2] == "n"):
                    c = text[i-2] + text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['katagana']['all'][j]
                            break
                        j += 1
                    to_katagana += c
                    #print(c)

                else:
                    c = text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['katagana']['all'][j]
                            break
                        j += 1
                    to_katagana += c
                    #print(c)

            j = 0
            for y in char['romaji']['all']:
                if(y == x):
                    c = char['katagana']['all'][j]
                    break
                j += 1
            to_katagana += c


        #if is "vowel"
        elif(x in vowels): 
            #if is not "cons + vowel"
            if(not text[i-1] in consonnes):
                j = 0
                for y in char['romaji']['all']:
                    if(y == x):
                        c = char['katagana']['all'][j]
                        break
                    j += 1
                to_katagana += c
                #print(c)

            #if is "cons + vowel"    
            elif(text[i-1] in consonnes):
                #if is "cons + cons + vowel" and consonnes are same
                if(text[i-2] in consonnes and text[i-2] == text[i-1]): 
                    c = text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['katagana']['all'][j]
                            break
                        j += 1
                    
                    to_katagana += kata_small_tsu + c
                    #print(c)

                #if is "cons + cons + vowel" and cons1 is not "n"
                elif(text[i-2] in consonnes and not text[i-2] == "n"): 
                    c = text[i-2] + text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['katagana']['all'][j]
                            break
                        j += 1
                    
                    to_katagana += c
                    #print(c)
                else:
                    c = text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['katagana']['all'][j]
                            break
                        j += 1
                    to_katagana += c
                    #print(c)

        #if is space or not a letter (!&@...)            
        elif(not x in all): 
            to_katagana += x
            #print(x)
        i += 1
    
    to_katagana = to_katagana[1:] #et mtn on enlève l'espace du début
    return(to_katagana)