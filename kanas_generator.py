#This program show japanese characteres (hiragana->romaji) based on an int parameter.

from module_characters_jap_vcom import *
import random

def function():
    choose = input("Kana => Romaji (k)\nRomaji => Kana (r)\n>")
    nbr = int(input("How many?\n>"))

    
    replay = ""
    while(replay == ""):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        x = nbr
        romaji = ""
        kana = ""
    
        while(x > 0):
            i = random.randint(0, 70)
            if(choose == "k"):
                print(char['hiragana']['all'][i], end = ' ')
                romaji += char['romaji']['all'][i] + " "

            elif(choose == "r"):
                print(char['romaji']['all'][i], end = ' ')
                kana += char['hiragana']['all'][i] + " "

            x -= 1

        input("\n")
        if(choose == "k"):
            input(f"{romaji}\n")
        elif(choose == "r"):
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
Press Enter to proceed when nothing is asked.
...
""")
    input("""This symbol ">", means an answer is expected.
=============================
""")
    
    function()

if __name__ == "__main__":
    main() 
