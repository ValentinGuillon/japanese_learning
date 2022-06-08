#kana_reconizing.py
#This program show a japanese charactere (romaji=>hiragana and romaji=>hiragana).

from module_characters_jap import *
import random

def function():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    lang = input("Hiragana => Romaji (hr)\nRomaji => Hiragana(rh)\nKatagana => Romaji (kr)\nRomaji => Katagana(rk)\nHira/Kata => Romaji (gr)\nRomaji => Hira/Kata (rg)\n>")
    while(not lang == "hr" and not lang == "rh" and not lang == "kr" and not lang == "rk" and not lang == "gr" and not lang == "rg"):
        lang = input(">")
    category = input("""
Which syllabs:
All (A)
Miss(M)
voyelles (v)
k, s, t,
n, h, m,
y, r, w,
sp
>""")
    while(not category == "A" and not category == "M" and not category == "v" and not category == "k" and not category == "s" and not category == "t" and not category == "n" and not category == "h" and not category == "m" and not category == "y" and not category == "r" and not category == "w" and not category == "sp"):
        category = input(">")


    stop = ""
    while(not stop == "STOP"):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\"STOP\" to end\n\n\n\n\n")
        i = 0
        i_hira = 0
        i_kata = 0
        hiragana = "[none]"
        katagana = "[none]"
        romaji = "[none]"
        romaji_hira = "[none]"
        romaji_kata = "[none]"
        
        #gererate characters based on category
        if(category == "A"):
            i = random.randint(0, len(char['hiragana']['all']) -1)
            hiragana = char['hiragana']['all'][i]
            katagana = char['katagana']['all'][i]
            romaji = char['romaji']['all'][i]

        elif(category == "M"):
            if(lang == "hr" or lang == "rh"):
                i = random.randint(0, len(char['hiragana']['miss']) -1)
                hiragana = char['hiragana']['miss'][i]
                katagana = "none"
                romaji = char['romaji']['hira_miss'][i]
            if(lang == "kr" or lang == "rk"):
                i = random.randint(0, len(char['katagana']['miss']) -1)
                hiragana = "none"
                katagana = char['katagana']['miss'][i]
                romaji = char['romaji']['kata_miss'][i]
            if(lang == "gr" or lang == "rg"):
                i_hira = random.randint(0, len(char['hiragana']['miss']) -1)
                i_kata = random.randint(0, len(char['katagana']['miss']) -1)
                hiragana = char['hiragana']['miss'][i_hira]
                katagana = char['katagana']['miss'][i_kata]
                romaji_hira = char['romaji']['hira_miss'][i_hira]
                romaji_kata = char['romaji']['kata_miss'][i_kata]

            
            
        elif(category == "v"):
            i = random.randint(0, len(char['hiragana']['vowel']) -1)
            hiragana = char['hiragana']['vowel'][i]
            katagana = char['katagana']['vowel'][i]
            romaji = char['romaji']['vowel'][i]
        
        elif(category == "k"):
            i = random.randint(0, len(char['hiragana']['k']) -1)
            hiragana = char['hiragana']['k'][i]
            katagana = char['katagana']['k'][i]
            romaji = char['romaji']['k'][i]
        
        elif(category == "s"):
            i = random.randint(0, len(char['hiragana']['s']) -1)
            hiragana = char['hiragana']['s'][i]
            katagana = char['katagana']['s'][i]
            romaji = char['romaji']['s'][i]
        
        elif(category == "t"):
            i = random.randint(0, len(char['hiragana']['t']) -1)
            hiragana = char['hiragana']['t'][i]
            katagana = char['katagana']['t'][i]
            romaji = char['romaji']['t'][i]
        
        elif(category == "n"):
            i = random.randint(0, len(char['hiragana']['n']) -1)
            hiragana = char['hiragana']['n'][i]
            katagana = char['katagana']['n'][i]
            romaji = char['romaji']['n'][i]
        
        elif(category == "h"):
            i = random.randint(0, len(char['hiragana']['h']) -1)
            hiragana = char['hiragana']['h'][i]
            katagana = char['katagana']['h'][i]
            romaji = char['romaji']['h'][i]
        
        elif(category == "m"):
            i = random.randint(0, len(char['hiragana']['m']) -1)
            hiragana = char['hiragana']['m'][i]
            katagana = char['katagana']['m'][i]
            romaji = char['romaji']['m'][i]
        
        elif(category == "y"):
            i = random.randint(0, len(char['hiragana']['y']) -1)
            hiragana = char['hiragana']['y'][i]
            katagana = char['katagana']['y'][i]
            romaji = char['romaji']['y'][i]
        
        elif(category == "r"):
            i = random.randint(0, len(char['hiragana']['r']) -1)
            hiragana = char['hiragana']['r'][i]
            katagana = char['katagana']['r'][i]
            romaji = char['romaji']['r'][i]
        
        elif(category == "w"):
            i = random.randint(0, len(char['hiragana']['w']) -1)
            hiragana = char['hiragana']['w'][i]
            katagana = char['katagana']['w'][i]
            romaji = char['romaji']['w'][i]
        elif(category == "sp"):
            i = random.randint(0, len(char['hiragana']['sp']) -1)
            hiragana = char['hiragana']['sp'][i]
            katagana = char['katagana']['sp'][i]
            romaji = char['romaji']['sp'][i]

        
        #print based on language
        if(lang == "hr"):
            stop = input(f"{hiragana}\n")
            if(not stop == "STOP"):
                stop = input(f"{romaji}\n")

        elif(lang == "kr"):
            stop = input(f"{katagana}\n")
            if(not stop == "STOP"):
                stop = input(f"{romaji}\n")
                
        elif(lang == "gr"):
            if(random.randint(0, 1)):
                stop = input(f"{hiragana}\n")
                if(not stop == "STOP"):
                    stop = input(f"{romaji}\n")
            else:
                stop = input(f"{katagana}\n")
                if(not stop == "STOP"):
                    stop = input(f"{romaji}\n")

        elif(lang == "rh"):
            if(romaji == "ji"):
                stop = input("ji\n")
                if(not stop == "STOP"):
                    stop = input(f"{char['hiragana']['all'][21]}\n")
            elif(romaji == "zu"):
                stop = input("zu\n")
                if(not stop == "STOP"):
                    stop = input(f"{char['hiragana']['all'][32]}\n")
            else:
                stop = input(f"{romaji}\n")
                if(not stop == "STOP"):
                    stop = input(f"{hiragana}\n")
                    
        elif(lang == "rk"):
            if(romaji == "ji"):
                stop = input("ji\n")
                if(not stop == "STOP"):
                    stop = input(f"{char['katagana']['all'][21]}\n")
            elif(romaji == "zu"):
                stop = input("zu\n")
                if(not stop == "STOP"):
                    stop = input(f"{char['katagana']['all'][32]}\n")
            else:    
                stop = input(f"{romaji}\n")
                if(not stop == "STOP"):
                    stop = input(f"{katagana}\n")
                    
        elif(lang == "rg"):
            if(romaji == "ji"):
                if(random.randint(0, 1)):
                    stop = input("ji (hira)\n")
                    if(not stop == "STOP"):
                        stop = input(f"{char['hiragana']['all'][21]}\n")
                else:
                    stop = input("ji (kata)\n")
                    if(not stop == "STOP"):
                        stop = input(f"{char['katagana']['all'][21]}\n")
            elif(romaji == "zu"):
                if(random.randint(0, 1)):
                    stop = input("zu (hira)\n")
                    if(not stop == "STOP"):
                        stop = input(f"{char['hiragana']['all'][32]}\n")
                else:
                    stop = input("zu (kata)\n")
                    if(not stop == "STOP"):
                        stop = input(f"{char['katagana']['all'][32]}\n")
            else:
                if(random.randint(0, 1)):
                    if(category == "M"):
                        stop = input(f"{romaji_hira} (hira)\n")
                    else:
                        stop = input(f"{romaji} (hira)\n")

                    if(not stop == "STOP"):
                        stop = input(f"{hiragana}\n")
                else:
                    if(category == "M"):
                        stop = input(f"{romaji_kata} (kata)\n")
                    else:
                        stop = input(f"{romaji} (kata)\n")
                        
                    if(not stop == "STOP"):
                        stop = input(f"{katagana}\n")
        
    
    
    restart = input("\n\nRestart ? (y/n)\n>")
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
