#kana.py
#This program show japanese characters (hira/kata->romaji) based on an int parameter.

import random
from module_characters_jap import *


def presentation():
    input("""
=============================
        This program
          show you
          multiple
            kana
     (in jap or romaji)
          then the
         translation
=============================
...""")
    input("Press Enter to proceed\nwhen nothing is asked.\n...")
    input("This symbol \">\",\nmeans an answer is expected.\n=============================\n""")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

#print current category and languages
def printOptions(category, lang):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("=========== Kana category ===")
    if (category in ['A', 'a']):
        print(" All")
    if (category == 'v'):
        print(" Vowals")
    if (category == 'k'):
        print(" K/G")
    if (category == 's'):
        print(" S/Z")
    if (category == 't'):
        print(" T/D")
    if (category == 'n'):
        print(" N")
    if (category == 'h'):
        print(" H/B/P")
    if (category == 'm'):
        print(" M")
    if (category == 'r'):
        print(" R")
    if (category == 'w'):
        print(" W/N")
    if (category == 'c'):
        print(" Combi")
    if (category == 'C'):
        print(" Combi+")

    print("========== Printing order ===")
    for n in lang[0]:
        if n == 'r':
            print(" Romaji => Kana")
        if n == 'k':
            print(" Kana => Romaji")

    print("==================== Kana ===")
    for n in lang[1]:
        if n == 'h':
            print(" Hiragana")
        if n == 'k':
            print(" Katakana")
        if n == 'b' :
            print(" Random kana")
    print("=============================")




#ask language (jap or romaji) first, then program loop (possibility of restart the fonction during the loop)
def main(combiAdded, combiplusAdded):
    print("\n\n\n\n\n\n\n\n")
    lang = ""
    userInput = ""

    #choose printing order
    print("= Choose what to see first ==\n Kana (k)\n Romaji (r)\n=============================")
    while(not userInput == "k" and not userInput == "r"):
        userInput = input(">")
    
    lang += userInput
    userInput = ""

    #choose kana type
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("============= Choose kana ===\n Hiragana (h)\n Katakana (k)\n Both (b)\n=============================")
    while(not userInput == "h" and not userInput == "k" and not userInput == "b"):
        userInput = input(">")
    
    lang += userInput

    kanaFamily = ['a', 'v', 'k', 's', 't', 'n', 'h', 'm', 'r', 'w', 'c', 'C']


    family = ""
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if(input("Choose a kana category ? (y/n)\n>") == 'y'):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("==== Choose kana category ===\n All (a)\n Vowels (v)\n K/G (k)\n S/Z (s)\n T/D (t)\n N (n)\n H/B/P (h)\n M (m)\n R (r)\n W/N (w)\n Combi (c) (kya, byu...)\n Combi+ (C) (va, kwo...)\n=============================")
        while (not family in kanaFamily):
            family = input(">")
    
    else:
        family = 'A'
        if(combiAdded == 0):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            if(input("    Add combi kana ? (y/n)\n>") == 'y'):
                combiAdded = 1
                for n in char['sp']:
                    char['all'].append(n)
        if(combiplusAdded == 0):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            if(input("    Add combi+ kana ? (y/n)\n>") == 'y'):
                combiAdded = 1
                combiplusAdded = 1
                for n in char['sp']:
                    char['all'].append(n)
                for n in char['sp+']:
                    char['all'].append(n)

    if(family == 'c' and combiAdded == 0):
        combiAdded = 1
        for n in char['sp']:
            char['all'].append(n)
    if(family == 'C' and combiplusAdded == 0):
        combiAdded = 1
        combiplusAdded = 1
        for n in char['sp']:
            char['all'].append(n)
        for n in char['sp+']:
            char['all'].append(n)



    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    nbr = int(input("    How much kana ?\n>"))

    
    stop = ""
    while(not stop == "STOP"):
        printOptions(family, lang)
        print("\"STOP\" to end\n\n")

        x = nbr
        romaji = ""
        kana = ""
        saveLang = lang

        if lang[1] == 'b':
            if (random.randint(0, 1)):
                lang  = lang[0] + 'h'
            else:
                lang  = lang[0] + 'k'
    
        if (lang[0] == 'r'):
            if (lang[1] == 'h'):
                print("(Hiragana)")
            if (lang[1] == 'k'):
                print("(Katakana)")

        #printing of characters, then creation of the traducted characters
        while(x > 0):
            if (family == 'A' or 'a'):
                i = random.randint(0, len(char['all']) -1)
            if (family == 'v'):
                i = random.randint(0, 4)
            if (family == 'k'):
                i = random.randint(5, 14)
            if (family == 's'):
                i = random.randint(15, 24)
            if (family == 't'):
                i = random.randint(25, 34)
            if (family == 'n'):
                i = random.randint(35, 39)
            if (family == 'h'):
                i = random.randint(40, 54)
            if (family == 'm'):
                i = random.randint(55, 59)
            if (family == 'r'):
                i = random.randint(63, 67)
            if (family == 'w'):
                i = random.randint(68, 70)
            if (family == 'c'):
                i = random.randint(71, 97)
            if (family == 'C'):
                i = random.randint(98, 130)
            
            
            
            #kana => romaji
            if(lang[0] == 'k'):
                if(lang[1] == 'h'):
                    print(char['all'][i].hira, end = ' ')
                if(lang[1] == 'k'):
                    print(char['all'][i].kata, end = ' ')
                romaji += char['all'][i].roma + " "
            
            #romaji => kana
            if(lang[0] == 'r'):
                print(char['all'][i].roma, end = ' ')
                if(lang[1] == 'h'):
                    kana += char['all'][i].hira + " "
                if(lang[1] == 'k'):
                    kana += char['all'][i].kata + " "

            
            x -= 1

        
        

        stop = input("\n")

        #affichage de la réponse
        if((lang[0] == 'k') and not stop == "STOP"):
            stop = input(f"{romaji}\n")
        elif((lang[0] == 'r') and not stop == "STOP"):
            stop = input(f"{kana}\n")


        #reset language
        lang = saveLang
    
    restart = ""
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRestart ? (y/n)")
    while(restart == "" or not restart == "n"):
        if(restart == "y"):
            main(combiAdded, combiplusAdded)
            break
        restart = input(">")



if __name__ == "__main__":
    presentation()
    main(0, 0)
