#This program show japanese characteres (hiragana->romaji) based on an int parameter.

from module_characters_jap_vcom import *
import random

def function():
    choose = input("kana or romaji?\n>")
    nbr = int(input("How much?\n>"))

    
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
    
    restart = ""
    while(restart == ""):
        restart = input("Restart ? (y/n)\n>")
        if(restart == "y"):
            function()





def main():
    input("""
    	
=============================
        This program
          give you
        kana symbols
          base on
        your number
=============================
When there is no choices
press Enter
""")
    
    function()

if __name__ == "__main__":
    main() 
