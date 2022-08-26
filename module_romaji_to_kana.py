#module_romaji_to_kana.py
#This module have a fonction to translate romaji input to hiragana or katagana

from module_characters_jap import *
import string


#kana_lang == 'hiragana' or 'katagana', x is the romaji version of the kana to find
def find_kana(kana_lang, x):
    j = 0
    for y in char['romaji']['all']:
        if(y == x):
            return(char[kana_lang]['all'][j])
        j += 1
    return 0

#this fonction made his way on the word letter by letter. When the end of a syllab is reached, the corresponding kana is added to a list ("to_hiragana"), until the final letter. Then return the completed list.
def romaji_to_hiragana(text):
    text = text.lower() #romaji text to transform into kana
    all = string.ascii_lowercase #all alphabetical letters
    vowels = "a" + "i" + "u" + "e" + "o"
    vowels_circumflex = "â" + "î" + "û" + "ê" + "ô"
    consonants = "k" + "g" + "s" + "z" + "t" + "c" + "h" + "d" + "j" + "n" + "h" + "f" + "b" + "p" + "m" + "y" + "r" + "w" + "n"

    to_hiragana = "" #consecutively stores kana, then finaly return it
    c = "" #kana that will be added to "to_hiragana"
    text = " " + text #will be removed at the end. It's for the case when the first and last letters are the sames consonant. Because on the program, it check i-1 on list, and for the first letter, it will check the last (and we don't wan't that)
    
    i = 0 #position on the word
    for x in text:
        j = 0 #position on the romaji/hira/kata syllabs list
        #the checked letter is a "n" (this part is for identify if it's a solo "n")
        if(x == "n"):
            #the "n" is the last letter on the word
            if(len(text[i:]) == 1):
                c = find_kana('hiragana', x)
                to_hiragana += c
            
            #the "n" IS NOT followed by a vowel
            elif(not text[i+1] in vowels and not text[i+1] in vowels_circumflex):
                c = find_kana('hiragana', x)
                to_hiragana += c

        #the checked letter is a "vowel" with an circumflex
        elif(x in vowels_circumflex): 
            #change the vowel circumflex to a simple vowel
            if(x == "â"):
                x = "a"
            elif(x == "î"):
                x = "i"
            elif(x == "û"):
                x = "u"
            elif(x == "ê"):
                x = "e"
            elif(x == "ô"):
                x = "o"

            #the vowel IS NOT after a consonant (so it's NOT a consonant-vowel syllab, just a single vowel)
            if(not text[i-1] in consonants):
                c = find_kana('hiragana', x)
                to_hiragana += c
            
            #the vowel IS after a consonant
            elif(text[i-1] in consonants):
                #the vowel is after two same consonants
                if(text[i-2] == text[i-1]):
                    c = text[i-1] + x
                    c = find_kana('hiragana', c)
                    to_hiragana += hira_small_tsu + c

                #the vowel is after two (different) consonants, but the first in not a "n"
                elif(text[i-2] in consonants and not text[i-2] == "n"):
                    c = text[i-2] + text[i-1] + x
                    c = find_kana('hiragana', c)
                    to_hiragana += c

                #the vowel is after only one consonant
                else:
                    c = text[i-1] + x
                    c = find_kana('hiragana', c)
                    to_hiragana += c

            #because th vowel is circumflex, we have to add a vowel kana
            #(don't forget the rule for the double vowel, with "e" and "o")
            if(x == "e"):
                x = "i"
            elif(x == "o"):
                x = "u"

            c = find_kana('hiragana', x)
            to_hiragana += c


        #the checked letter is a "vowel" (without circumflex)
        elif(x in vowels): 
            #the vowel IS NOT after a consonant (so it's NOT a consonant-vowel syllab, just a single vowel)
            if(not text[i-1] in consonants):
                c = find_kana('hiragana', x)
                to_hiragana += c

            #the vowel IS after a consonant   
            elif(text[i-1] in consonants):
                #the vowel is after two same consonants
                if(text[i-2] in consonants and text[i-2] == text[i-1]): 
                    c = text[i-1] + x
                    c = find_kana('hiragana', c)
                    to_hiragana += hira_small_tsu + c

                #the vowel is after two (different) consonants, but the first in not a "n"
                elif(text[i-2] in consonants and not text[i-2] == "n"): 
                    c = text[i-2] + text[i-1] + x
                    c = find_kana('hiragana', c)
                    to_hiragana += c

                #the vowel is after only one consonant
                else:
                    c = text[i-1] + x
                    c = find_kana('hiragana', c)
                    to_hiragana += c
                    #print(c)

        #if is space or not a letter (!&@...)            
        elif(not x in all): 
            to_hiragana += x
            #print(x)
        i += 1
    
    to_hiragana = to_hiragana[1:] #on enlève l'espace du début
    return(to_hiragana)




#this fonction made his way on the word letter by letter. When the end of a syllab is reached, the corresponding kana is added to a list ("to_katagana"), until the final letter. Then return the completed list.
def romaji_to_katagana(text):
    text = text.lower() #romaji text to transform into kana
    all = string.ascii_lowercase #all alphabetical letters
    vowels = "a" + "i" + "u" + "e" + "o"
    vowels_circumflex = "â" + "î" + "û" + "ê" + "ô"
    consonants = "k" + "g" + "s" + "z" + "t" + "c" + "h" + "d" + "j" + "n" + "h" + "f" + "b" + "p" + "m" + "y" + "r" + "w" + "n"

    to_katagana = "" #consecutively stores kana, then finaly return it
    c = "" #kana that will be added to "to_katagana"
    text = " " + text #will be removed at the end. It's for the case when the first and last letters are the sames consonant. Because on the program, it check i-1 on list, and for the first letter, it will check the last (and we don't wan't that)
    
    i = 0 #position on the word
    for x in text:
        j = 0 #position on the romaji/hira/kata syllabs list
        #the checked letter is a "n" (this part is for identify if it's a solo "n")
        if(x == "n"):
            #the "n" is the last letter on the word
            if(len(text[i:]) == 1):
                c = find_kana('katagana', x)
                to_katagana += c
            
            #the "n" IS NOT followed by a vowel
            elif(not text[i+1] in vowels and not text[i+1] in vowels_circumflex):
                c = find_kana('katagana', x)
                to_katagana += c

        #the checked letter is a "vowel" with an circumflex
        elif(x in vowels_circumflex): 
            #change the vowel circumflex to a simple vowel
            if(x == "â"):
                x = "a"
            elif(x == "î"):
                x = "i"
            elif(x == "û"):
                x = "u"
            elif(x == "ê"):
                x = "e"
            elif(x == "ô"):
                x = "o"

            #the vowel IS NOT after a consonant (so it's NOT a consonant-vowel syllab, just a single vowel)
            if(not text[i-1] in consonants):
                c = find_kana('katagana', x)
                to_katagana += c
            
            #the vowel IS after a consonant
            elif(text[i-1] in consonants):
                #the vowel is after two same consonants
                if(text[i-2] == text[i-1]):
                    c = text[i-1] + x
                    c = find_kana('katagana', c)
                    to_katagana += kata_small_tsu + c

                #the vowel is after two (different) consonants, but the first in not a "n"
                elif(text[i-2] in consonants and not text[i-2] == "n"):
                    c = text[i-2] + text[i-1] + x
                    c = find_kana('katagana', c)
                    to_katagana += c

                #the vowel is after only one consonant
                else:
                    c = text[i-1] + x
                    c = find_kana('katagana', c)
                    to_katagana += c

            #because th vowel is circumflex, we have to add a vowel kana
            to_katagana += kata_long_vowel


        #the checked letter is a "vowel" (without circumflex)
        elif(x in vowels): 
            #the vowel IS NOT after a consonant (so it's NOT a consonant-vowel syllab, just a single vowel)
            if(not text[i-1] in consonants):
                c = find_kana('katagana', x)
                to_katagana += c

            #the vowel IS after a consonant   
            elif(text[i-1] in consonants):
                #the vowel is after two same consonants
                if(text[i-2] in consonants and text[i-2] == text[i-1]): 
                    c = text[i-1] + x
                    c = find_kana('katagana', c)
                    to_katagana += kata_small_tsu + c

                #the vowel is after two (different) consonants, but the first in not a "n"
                elif(text[i-2] in consonants and not text[i-2] == "n"): 
                    c = text[i-2] + text[i-1] + x
                    c = find_kana('katagana', c)
                    to_katagana += c

                #the vowel is after only one consonant
                else:
                    c = text[i-1] + x
                    c = find_kana('katagana', c)
                    to_katagana += c
                    #print(c)

        #if is space or not a letter (!&@...)            
        elif(not x in all): 
            to_katagana += x
            #print(x)
        i += 1
    
    to_katagana = to_katagana[1:] #on enlève l'espace du début
    return(to_katagana)