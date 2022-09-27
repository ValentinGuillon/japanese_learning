#module_romaji_to_kana.py
#This module have a fonction to translate romaji input to hiragana or katakana

from module_characters_jap import *
import string

#add specials characters in the [all] list
for n in char['sp']:
    char['all'].append(n)
for n in char['sp+']:
    char['all'].append(n)

#kana_lang == 'hira' or 'kata', x is the romaji version of the kana to find
def find_kana(kana_lang, x):
    i = 0
    for y in char['all']:
        if(y.roma == x):
            if(kana_lang == "hira"):
                return(char['all'][i].hira)
            elif(kana_lang == "kata"):
                return(char['all'][i].kata)
        i += 1
    return 0



#this fonction made his way on the word letter by letter. When the end of a syllab is reached, the corresponding kana is added to a list ("to_hira"), until the final letter. Then return the completed list.
def romaji_to_hira(text):
    text = text.lower() #romaji text to transform into kana
    all = string.ascii_lowercase #all alphabetical letters
    vowels = "a" + "i" + "u" + "e" + "o"
    vowels_circumflex = "â" + "î" + "û" + "ê" + "ô"
    consonants = "k" + "g" + "s" + "z" + "t" + "c" + "h" + "d" + "j" + "n" + "h" + "f" + "b" + "p" + "m" + "y" + "r" + "w" + "n" + "v"

    to_hira = "" #consecutively stores kana, then finaly return it
    c = "" #kana that will be added to "to_hira"
    text = " " + text #will be removed at the end. It's for the case when the first and last letters are the sames consonant. Because on the program, it check i-1 on list, and for the first letter, it will check the last (and we don't wan't that)
    
    i = 0 #position on the word
    for x in text:
        j = 0 #position on the romaji/hira/kata syllabs list
        #the checked letter is a "n" (this part is for identify if it's a solo "n")

        if(x in consonants and text[i-1] == x):
            to_hira += tsuSmall.hira

        elif(x == "n"):
            #the "n" is the last letter on the word
            if(len(text[i:]) == 1):
                c = find_kana('hira', x)
                to_hira += c
            
            elif(text[i+1] == 'n'):
                pass
                #do nothing, because a double n, so it will be checked as a double letter (for the "small tsu")

            #the "n" IS NOT followed by a vowel
            elif(not text[i+1] in vowels and not text[i+1] in vowels_circumflex):
                c = find_kana('hira', x)
                to_hira += c

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
                c = find_kana('hira', x)
                to_hira += c
            
            #the vowel IS after a consonant
            elif(text[i-1] in consonants):
                #the vowel is after two same consonants
                if(text[i-2] == text[i-1]):
                    c = text[i-1] + x
                    c = find_kana('hira', c)
                    to_hira += c

                #the vowel is after two (different) consonants, but the first in not a "n"
                elif(text[i-2] in consonants and not text[i-2] == "n"):
                    c = text[i-2] + text[i-1] + x
                    c = find_kana('hira', c)
                    to_hira += c

                #the vowel is after only one consonant
                else:
                    c = text[i-1] + x
                    c = find_kana('hira', c)
                    to_hira += c

            #because th vowel is circumflex, we have to add a vowel kana
            #(don't forget the rule for the double vowel, with "e" and "o")
            if(x == "e"):
                x = "i"
            elif(x == "o"):
                x = "u"

            c = find_kana('hira', x)
            to_hira += c


        #the checked letter is a "vowel" (without circumflex)
        elif(x in vowels):
            #the vowel IS NOT after a consonant (so it's NOT a consonant-vowel syllab, just a single vowel)
            if(not text[i-1] in consonants and not text[i-1] in vowels_circumflex):
                if(text[i-1] == x):
                    if(x == "e"):
                        x = "i"
                    elif(x == "o"):
                        x = "u"

                c = find_kana('hira', x)
                to_hira += c

            #the vowel IS after a consonant   
            elif(text[i-1] in consonants):
                #the vowel is after two same consonants
                if(text[i-2] in consonants and text[i-2] == text[i-1]): 
                    c = text[i-1] + x
                    c = find_kana('hira', c)
                    to_hira += c
                    

                #the vowel is after two (different) consonants, but the first in not a "n"
                elif(text[i-2] in consonants and not text[i-2] == "n"): 
                    c = text[i-2] + text[i-1] + x
                    c = find_kana('hira', c)
                    to_hira += c

                #the vowel is after only one consonant
                else:
                    c = text[i-1] + x
                    c = find_kana('hira', c)
                    to_hira += c

        #if is space or not a letter (!&@...)            
        elif(not x in all): 
            to_hira += x

        else:
            #print("--------do nothing\n")
            pass

        i += 1

    
    to_hira = to_hira[1:] #on enlève l'espace du début
    return(to_hira)




#this fonction made his way on the word letter by letter. When the end of a syllab is reached, the corresponding kana is added to a list ("to_kata"), until the final letter. Then return the completed list.
def romaji_to_kata(text):
    text = text.lower() #romaji text to transform into kana
    all = string.ascii_lowercase #all alphabetical letters
    vowels = "a" + "i" + "u" + "e" + "o"
    vowels_circumflex = "â" + "î" + "û" + "ê" + "ô"
    consonants = "k" + "g" + "s" + "z" + "t" + "c" + "h" + "d" + "j" + "n" + "h" + "f" + "b" + "p" + "m" + "y" + "r" + "w" + "n" + "v"

    to_kata = "" #consecutively stores kana, then finaly return it
    c = "" #kana that will be added to "to_kata"
    text = " " + text #will be removed at the end. It's for the case when the first and last letters are the sames consonant. Because on the program, it check i-1 on list, and for the first letter, it will check the last (and we don't wan't that)
    
    i = 0 #position on the word
    for x in text:
        j = 0 #position on the romaji/hira/kata syllabs list
        #the checked letter is a "n" (this part is for identify if it's a solo "n")

        if(x in consonants and text[i-1] == x):
            to_kata += tsuSmall.kata


        elif(x == "n"):
            #the "n" is the last letter on the word
            if(len(text[i:]) == 1):
                c = find_kana('kata', x)
                to_kata += c

            elif(text[i+1] == 'n'):
                pass
                #do nothing, because a double n, so it will be checked as a double letter (for the "small tsu")
            
            #the "n" IS NOT followed by a vowel
            elif(not text[i+1] in vowels and not text[i+1] in vowels_circumflex):
                c = find_kana('kata', x)
                to_kata += c

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
                c = find_kana('kata', x)
                to_kata += c
            
            #the vowel IS after a consonant
            elif(text[i-1] in consonants):
                #the vowel is after two same consonants
                if(text[i-2] == text[i-1]):
                    c = text[i-1] + x
                    c = find_kana('kata', c)
                    to_kata += c

                #the vowel is after two (different) consonants, but the first in not a "n"
                elif(text[i-2] in consonants and not text[i-2] == "n"):
                    c = text[i-2] + text[i-1] + x
                    c = find_kana('kata', c)
                    to_kata += c

                #the vowel is after only one consonant
                else:
                    c = text[i-1] + x
                    c = find_kana('kata', c)
                    to_kata += c

            #because th vowel is circumflex, we have to add a vowel kana
            to_kata += longVowel.kata


        #the checked letter is a "vowel" (without circumflex)
        elif(x in vowels):
            #the vowel IS NOT after a consonant (so it's NOT a consonant-vowel syllab, just a single vowel)
            if(not text[i-1] in consonants):
                if(text[i-1] in vowels and x == text[i-1]):
                    to_kata += longVowel.kata
                elif(text[i-1] in vowels):
                    if(text[i-1] == 'e' and x == "i"):
                        to_kata += longVowel.kata
                    elif(text[i-1] == 'o' and x == "u"):
                        to_kata += longVowel.kata
                    else:
                        c = find_kana('kata', x)
                        to_kata += c

                else:
                    c = find_kana('kata', x)
                    to_kata += c

            #the vowel IS after a consonant   
            elif(text[i-1] in consonants):
                #the vowel is after two same consonants
                if(text[i-2] in consonants and text[i-2] == text[i-1]): 
                    c = text[i-1] + x
                    c = find_kana('kata', c)
                    to_kata += c

                #the vowel is after two (different) consonants, but the first in not a "n"
                elif(text[i-2] in consonants and not text[i-2] == "n"): 
                    c = text[i-2] + text[i-1] + x
                    c = find_kana('kata', c)
                    to_kata += c

                #the vowel is after only one consonant
                else:
                    c = text[i-1] + x
                    c = find_kana('kata', c)
                    to_kata += c
                    #print(c)

        #if is space or not a letter (!&@...)            
        elif(not x in all): 
            to_kata += x
            #print(x)
        i += 1
    
    to_kata = to_kata[1:] #on enlève l'espace du début
    return(to_kata)


'''
#il faut prendre en compte les kana spéciaux pour cette partie, et là, flemme
def kana_to_romaji(text):
    romaji = "" #'text' change into romaji
    c = "" #kana
    i = 0 #position on 'text'
    j = 0 #position on the romaji/hira/kata syllabs list
    founded = 0 #bool to tell if the kana was find or not
    double_consonant = 0 #there will be a consonnat to double

    while (not len(text[i:]) == 0) :
        j = 0
        founded = 0

        for x in char['hira']['all']:
            if(x == text[i]):
                c = char[romaji]['all'][j]
                founded = 1
                break
            j += 1
        
        if(founded == 0):
            for x in char['kata']['all']:
                if(x == text[i]):
                    c = char[romaji]['all'][j]
                    founded = 1
                    break
                j += 1
        
        if(founded == 0):


        
        i += 1
'''