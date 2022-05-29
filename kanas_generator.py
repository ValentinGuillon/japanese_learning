#kanas_generator.py
#This program show japanese characteres (hiragana->romaji) based on an int parameter.

from module_characters_jap import *
import random

def function():
    lang = input("Hiragana => Romaji (hr)\nRomaji => Hiragana (rh)\nKatagana => Romaji (kr)\nRomaji => Katagana (rk)\n>")
    while(not lang == "hr" and not lang == "rh" and not lang == "kr" and not lang == "rk"):
        lang = input(">")
    nbr = int(input("How many?\n>"))

    
    replay = ""
    while(replay == ""):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        x = nbr
        romaji = ""
        kana = ""
    
        #affichage de la suite à deviner, et création de la réponse
        while(x > 0):
            i = random.randint(0, len(char['romaji']['all']) - 1)
            if(lang == "hr"):
                print(char['hiragana']['all'][i], end = ' ')
                romaji += char['romaji']['all'][i] + " "

            elif(lang == "kr"):
                print(char['katagana']['all'][i], end = ' ')
                romaji += char['romaji']['all'][i] + " "
            
            elif(lang == "rh"):
                print(char['romaji']['all'][i], end = ' ')
                kana += char['hiragana']['all'][i] + " "
            
            elif(lang == "rk"):
                print(char['romaji']['all'][i], end = ' ')
                kana += char['katagana']['all'][i] + " "

            x -= 1

        input("\n")

        #affichage de la réponse
        if(lang == "hr" or lang == "kr"):
            input(f"{romaji}\n")
        elif(lang == "rh" or lang == "rk"):
            input(f"{kana}\n")

        replay = input("Again ? (Enter or n)\n>")
    
    restart = input("Restart ? (y/n)\n>")
    while(restart == "" or not restart == "n"):
        if(restart == "y"):
            function()
            break
        restart = input(">")





def main():
    input("""
    	
=============================
        This program
          give you
        kana symbols
          base on
        your number
=============================
Press Enter to proceed
when nothing is asked.
...
""")
    input("""This symbol ">",
means an answer is expected.
=============================
""")
    
    function()

if __name__ == "__main__":
    main() 
