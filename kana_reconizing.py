#kana_reconizing.py
#This program show a japanese charactere (romaji=>hiragana and romaji=>hiragana).

from modules.module_characters_jap import *
import random

def function():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    choose = input("Hiragana => Romaji (h)\nRomaji => Hiragana(r)\n>")
    while(not choose == "h" and not choose == "r"):
        choose = input(">")
    choice = input("""
Which syllabs:
All (A)
voyelles (v)
k, s, t,
n, h, m,
y, r, w,
sp
>""")
    while(not choice == "A" and not choice == "v" and not choice == "k" and not choice == "s" and not choice == "t" and not choice == "n" and not choice == "h" and not choice == "m" and not choice == "y" and not choice == "r" and not choice == "w" and not choice == "sp"):
        choice = input(">")


    replay = ""
    while(replay == ""):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        i = 0        
        hiragana = "[none]"
        romaji = "[none]"
        
        if(choice == "A"):
            i = random.randint(0, len(char['hiragana']['all']) -1)
            hiragana = char['hiragana']['all'][i]
            romaji = char['romaji']['all'][i]
            
        elif(choice == "v"):
            i = random.randint(0, len(char['hiragana']['vowel']) -1)
            hiragana = char['hiragana']['vowel'][i]
            romaji = char['romaji']['vowel'][i]
        
        elif(choice == "k"):
            i = random.randint(0, len(char['hiragana']['k']) -1)
            hiragana = char['hiragana']['k'][i]
            romaji = char['romaji']['k'][i]
        
        elif(choice == "s"):
            i = random.randint(0, len(char['hiragana']['s']) -1)
            hiragana = char['hiragana']['s'][i]
            romaji = char['romaji']['s'][i]
        
        elif(choice == "t"):
            i = random.randint(0, len(char['hiragana']['t']) -1)
            hiragana = char['hiragana']['t'][i]
            romaji = char['romaji']['t'][i]
        
        elif(choice == "n"):
            i = random.randint(0, len(char['hiragana']['n']) -1)
            hiragana = char['hiragana']['n'][i]
            romaji = char['romaji']['n'][i]
        
        elif(choice == "h"):
            i = random.randint(0, len(char['hiragana']['h']) -1)
            hiragana = char['hiragana']['h'][i]
            romaji = char['romaji']['h'][i]
        
        elif(choice == "m"):
            i = random.randint(0, len(char['hiragana']['m']) -1)
            hiragana = char['hiragana']['m'][i]
            romaji = char['romaji']['m'][i]
        
        elif(choice == "y"):
            i = random.randint(0, len(char['hiragana']['y']) -1)
            hiragana = char['hiragana']['y'][i]
            romaji = char['romaji']['y'][i]
        
        elif(choice == "r"):
            i = random.randint(0, len(char['hiragana']['r']) -1)
            hiragana = char['hiragana']['r'][i]
            romaji = char['romaji']['r'][i]
        
        elif(choice == "w"):
            i = random.randint(0, len(char['hiragana']['w']) -1)
            hiragana = char['hiragana']['w'][i]
            romaji = char['romaji']['w'][i]
        elif(choice == "sp"):
            i = random.randint(0, len(char['hiragana']['sp']) -1)
            hiragana = char['hiragana']['sp'][i]
            romaji = char['romaji']['sp'][i]

        
        if(choose == "h"):
            input(f"{hiragana}\n")
            input(f"{romaji}\n")             
                    
        elif(choose == "r"):
            if(romaji == "ji"):
                input("ji\n")
                input(f"{char['hiragana']['all'][21]}\n")
            elif(romaji == "zu"):
                input("zu\n")
                input(f"{char['hiragana']['all'][32]}\n")
            else:    
                input(f"{romaji}\n")
                input(f"{hiragana}\n")
        
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
       a kana symbol
            then
         in romaji
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
