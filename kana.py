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
def function(combi_added, combiplus_added):
    print("\n\n\n\n\n\n\n\n")
    lang = input("What do you want to see ?\n Kana (k)\n Romaji (r)\n>")
    lang += input("Which kind of kana ?\n Hiragana (h)\n Katakana (k)\n Both (b)\n>")

    family = 'A'
    if(input("All characters ? (y/n)\n>") == 'n'):
        while (not family == 'a' and not family == 'v' and not family == 'k' and not family == 's' and not family == 't' and not family == 'n' and not family == 'h' and not family == 'm' and not family == 'r' and not family == 'w' and not family == 'c' and not family == 'C'):
            family = input("Choose the range :\n All (a)\n Vowels (v)\n K/G (k)\n S/Z (s)\n T/D (t)\n N (n)\n H/B/P (h)\n M (m)\n R (r)\n W/N (w)\n Combi (c)\n Combi+ (C)\n>")
    
    else:
        if(combi_added == 0):
            if(input("Add combi kana ? (y/n)\n>") == 'y'):
                combi_added = 1
                for n in char['romaji']['sp']:
                    char['romaji']['all'].append(n)
                for n in char['hira']['sp']:
                    char['hira']['all'].append(n)
                for n in char['kata']['sp']:
                    char['kata']['all'].append(n)
        if(combiplus_added == 0):
            if(input("Add combi+ kana ? (y/n)\n>") == 'y'):
                combi_added = 1
                combiplus_added = 1
                for n in char['romaji']['sp']:
                    char['romaji']['all'].append(n)
                for n in char['hira']['sp']:
                    char['hira']['all'].append(n)
                for n in char['kata']['sp']:
                    char['kata']['all'].append(n)
                for n in char['romaji']['sp+']:
                    char['romaji']['all'].append(n)
                for n in char['hira']['sp+']:
                    char['hira']['all'].append(n)
                for n in char['kata']['sp+']:
                    char['kata']['all'].append(n)

    if(family == 'c' and combi_added == 0):
        combi_added = 1
        for n in char['romaji']['sp']:
            char['romaji']['all'].append(n)
        for n in char['hira']['sp']:
            char['hira']['all'].append(n)
        for n in char['kata']['sp']:
            char['kata']['all'].append(n)
    if(family == 'C' and combiplus_added == 0):
        combi_added = 1
        combiplus_added = 1
        for n in char['romaji']['sp']:
            char['romaji']['all'].append(n)
        for n in char['hira']['sp']:
            char['hira']['all'].append(n)
        for n in char['kata']['sp']:
            char['kata']['all'].append(n)
        for n in char['romaji']['sp+']:
            char['romaji']['all'].append(n)
        for n in char['hira']['sp+']:
            char['hira']['all'].append(n)
        for n in char['kata']['sp+']:
            char['kata']['all'].append(n)




    nbr = int(input("How much ?\n>"))

    
    stop = ""
    while(not stop == "STOP"):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\"STOP\" to end\n\n\n\n\n")

        x = nbr
        romaji = ""
        kana = ""

        rand_kana = lang[1]
        if rand_kana == 'b':
            if (random.randint(0, 1) == 0):
                rand_kana = 'h'
            else:
                rand_kana = 'k'
    
        if (lang[0] == 'r'):
            if (rand_kana == 'h'):
                print("(Hiragana)")
            if (rand_kana == 'k'):
                print("(Katakana)")

        #printing of characters, then creation of the traducted characters
        while(x > 0):
            if (family == 'A' or 'a'):
                i = random.randint(0, len(char['hira']['all']) -1)
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
                if(rand_kana == 'h'):
                    print(char['hira']['all'][i], end = ' ')
                if(rand_kana == 'k'):
                    print(char['kata']['all'][i], end = ' ')
                romaji += char['romaji']['all'][i] + " "
            
            #romaji => kana
            if(lang[0] == 'r'):
                print(char['romaji']['all'][i], end = ' ')
                if(rand_kana == 'h'):
                    kana += char['hira']['all'][i] + " "
                if(rand_kana == 'k'):
                    kana += char['kata']['all'][i] + " "

                

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
            function(combi_added, combiplus_added)
            break
        restart = input(">")





def main():
    presentation()
    function(0, 0)

if __name__ == "__main__":
    main() 
