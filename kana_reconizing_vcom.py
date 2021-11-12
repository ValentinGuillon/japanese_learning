#This program show a japanese charactere (romaji->hiragana and vs).

from module_characters_jap_vcom import *
import random

def function():
    choose = input("hiragana or romaji ? (h/r)\n>")
    choice = input("""
which syllabs:
All (Enter)
voyelles (v)
k, s, t,
n, h, m,
y, r, w
>""")


    replay = ""
    while(replay == ""):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        i = 0        
        hiragana = "[none]"
        romaji = "[none]"
        
        if(choice == ""):
            i = random.randint(0, 70)
            hiragana = char['hiragana']['all'][i]
            romaji = char['romaji']['all'][i]
            
        elif(choice == "v"):
            i = random.randint(0, 4)
            hiragana = char['hiragana']['vowel'][i]
            romaji = char['romaji']['vowel'][i]
        
        elif(choice == "k"):
            i = random.randint(0, 9)
            hiragana = char['hiragana']['k'][i]
            romaji = char['romaji']['k'][i]
        
        elif(choice == "s"):
            i = random.randint(0, 9)
            hiragana = char['hiragana']['s'][i]
            romaji = char['romaji']['s'][i]
        
        elif(choice == "t"):
            i = random.randint(0, 9)
            hiragana = char['hiragana']['t'][i]
            romaji = char['romaji']['t'][i]
        
        elif(choice == "n"):
            i = random.randint(0, 4)
            hiragana = char['hiragana']['n'][i]
            romaji = char['romaji']['n'][i]
        
        elif(choice == "h"):
            i = random.randint(0, 14)
            hiragana = char['hiragana']['h'][i]
            romaji = char['romaji']['h'][i]
        
        elif(choice == "m"):
            i = random.randint(0, 4)
            hiragana = char['hiragana']['m'][i]
            romaji = char['romaji']['m'][i]
        
        elif(choice == "y"):
            i = random.randint(0, 2)
            hiragana = char['hiragana']['y'][i]
            romaji = char['romaji']['y'][i]
        
        elif(choice == "r"):
            i = random.randint(0, 4)
            hiragana = char['hiragana']['r'][i]
            romaji = char['romaji']['r'][i]
        
        elif(choice == "w"):
            i = random.randint(0, 1)
            hiragana = char['hiragana']['w'][i]
            romaji = char['romaji']['w'][i]

        
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
       a kana symbol
            then
         in romaji
=============================
When there is no choices
press Enter
""")
    
    function()

if __name__ == "__main__":
    main() 
