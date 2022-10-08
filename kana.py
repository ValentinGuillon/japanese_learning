#kana.py
#This program show japanese characters (hira/kata->romaji) based on an int parameter.

from module_characters_jap import *
import random


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
Press Enter to proceed
when nothing is asked.
...
""")
    input("""This symbol ">",
means an answer is expected.
=============================
""")

#ask first langage (jap or romaji), then program loop (possibility of restart the fonction during the loop)
def main(combiAdded, combiplusAdded):
    print("\n\n\n\n\n\n\n\n")
    lang = input("What do you want to see ?\n Kana (k)\n Romaji (r)\n>")
    lang += input("Which kind of kana ?\n Hiragana (h)\n Katakana (k)\n Both (b)\n>")

    family = 'A'
    if(input("Choose a kana category ? (y/n)\n>") == 'y'):
        while (not family == 'a' and not family == 'v' and not family == 'k' and not family == 's' and not family == 't' and not family == 'n' and not family == 'h' and not family == 'm' and not family == 'r' and not family == 'w' and not family == 'c' and not family == 'C'):
            family = input("Choose the range :\n All (a)\n Vowels (v)\n K/G (k)\n S/Z (s)\n T/D (t)\n N (n)\n H/B/P (h)\n M (m)\n R (r)\n W/N (w)\n Combi (c)\n Combi+ (C)\n>")
    
    else:
        if(combiAdded == 0):
            if(input("Add combi kana ? (y/n)\n>") == 'y'):
                combiAdded = 1
                for n in char['sp']:
                    char['all'].append(n)
        if(combiplusAdded == 0):
            if(input("Add combi+ kana ? (y/n)\n>") == 'y'):
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




    nbr = int(input("How much ?\n>"))

    
    stop = ""
    while(not stop == "STOP"):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\"STOP\" to end\n\n\n\n\n")

        x = nbr
        romaji = ""
        kana = ""

        randKana = lang[1]
        if randKana == 'b':
            if (random.randint(0, 1) == 0):
                randKana = 'h'
            else:
                randKana = 'k'
    
        if (lang[0] == 'r'):
            if (randKana == 'h'):
                print("(Hiragana)")
            if (randKana == 'k'):
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
                if(randKana == 'h'):
                    print(char['all'][i].hira, end = ' ')
                if(randKana == 'k'):
                    print(char['all'][i].kata, end = ' ')
                romaji += char['all'][i].roma + " "
            
            #romaji => kana
            if(lang[0] == 'r'):
                print(char['all'][i].roma, end = ' ')
                if(randKana == 'h'):
                    kana += char['all'][i].hira + " "
                if(randKana == 'k'):
                    kana += char['all'][i].kata + " "

                

            x -= 1

        stop = input("\n")

        #affichage de la réponse
        if((lang[0] == 'k') and not stop == "STOP"):
            stop = input(f"{romaji}\n")
        elif((lang[0] == 'r') and not stop == "STOP"):
            stop = input(f"{kana}\n")

    
    restart = input("\n\nRestart ? (y/n)\n>")
    while(restart == "" or not restart == "n"):
        if(restart == "y"):
            main(combiAdded, combiplusAdded)
            break
        restart = input(">")



if __name__ == "__main__":
    presentation()
    main(0, 0)
