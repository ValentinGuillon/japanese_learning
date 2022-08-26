#choose_random_1_999.py
import random
from module_romaji_to_kana import *


def presentation():
    input("""
=============================
        This program
     gives you a number
     between 1 and 999
        in japanese
=============================
Press Enter to proceed
when nothing is asked.
...
""")
    input("""This symbol ">",
means an answer is expected.
=============================
""")

def function_mod():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") 
    mod = input("""Choose the program mod :
Guess mod (g) | View mod (v)
  You have    |   Guess in
  to write    |   your mind
  the word    |   No input
  to guess    |   require
>""")
    while(not mod == "g" and not mod == "v"):
        mod = input(">")
    function(mod)


def function(mod):    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    if(mod == "v"):
        lang = input("Number => Romaji (nr)\nRomaji => Number (rn)\nNumber => Hiragana (nh)\nHiragana => Number (hn)\nNumber => katakana (nk)\nkatakana => Number (kn)\n>")
        while(not lang == "nh" and not lang == "nr" and not lang == "hn" and not lang == "rn" and not lang == "nk" and not lang == "kn"):
            lang = input(">")

    elif(mod == "g"):
        lang = input("Number => Romaji (n)\nRomaji => Number (r)\nHiragana => Number (h)\nkatakana => Number (k)\n>")
        while(not lang == "n" and not lang == "r" and not lang == "h" and not lang == "k"):
            lang = input(">")


    correct = 0
    wrong = 0
    streak = 0
    current_streak = 0
    stop = ""
    while(not stop == "STOP") :
        nbr = random.randint(1, 999)
        romaji = nbr_to_romaji(nbr)
        hira = romaji_to_hira(romaji)
        kata = romaji_to_kata(romaji)
        
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\"STOP\" to end\n\n\n\n\n")

        if(mod == "v"):
            if(lang == "nr"):
                stop = input(f"{nbr}\n")
                if(not stop == "STOP"):
                    stop = input(f"{romaji}\n")
            elif(lang == "rn"):
                stop = input(f"{romaji}\n")
                if(not stop == "STOP"):
                    stop = input(f"{nbr}\n")
            elif(lang == "nh"):
                stop = input(f"{nbr}\n")
                if(not stop == "STOP"):
                    stop = input(f"{hira}\n")
            elif(lang == "hn"):
                stop = input(f"{hira}\n")
                if(not stop == "STOP"):
                    stop = input(f"{nbr}\n")
            elif(lang == "nk"):
                stop = input(f"{nbr}\n")
                if(not stop == "STOP"):
                    stop = input(f"{kata}\n")
            elif(lang == "kn"):
                stop = input(f"{kata}\n")
                if(not stop == "STOP"):
                    stop = input(f"{nbr}\n")

        

        elif(mod == "g"):
            if(lang == "n"):
                guess = input(f"""\n===============
    Correct:{correct}\n      Wrong:{wrong}\nBest streak:{streak}\n     Streak:{current_streak}\n===============\n\n\n\n
In romaji ?\n\n {nbr}\n>""")
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str.lower(romaji)):
                    input(f"""Oupsi. C'était "{romaji}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                elif(str.lower(guess) == romaji):
                    correct += 1
                    current_streak += 1

            elif(lang == "r"):
                guess = input(f"""\n===============
    Correct:{correct}\n      Wrong:{wrong}\nBest streak:{streak}\n     Streak:{current_streak}\n===============\n\n\n\n
Which number is ?\n\n {romaji}\n>""")
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str(nbr)):
                    input(f"""Oupsi. C'était "{nbr}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                elif(guess == str(nbr)):
                    correct += 1
                    current_streak += 1

            elif(lang == "h"):
                guess = input(f"""\n===============
    Correct:{correct}\n      Wrong:{wrong}\nBest streak:{streak}\n     Streak:{current_streak}\n===============\n\n\n\n
Which number is ?\n\n {hira}\n>""")
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str(nbr)):
                    input(f"""Oupsi. C'était "{nbr}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                elif(guess == str(nbr)):
                    correct += 1
                    current_streak += 1

            elif(lang == "k"):
                guess = input(f"""\n===============
    Correct:{correct}\n      Wrong:{wrong}\nBest streak:{streak}\n     Streak:{current_streak}\n===============\n\n\n\n
Which number is ?\n\n {kata}\n>""")
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str(nbr)):
                    input(f"""Oupsi. C'était "{nbr}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                elif(guess == str(nbr)):
                    correct += 1
                    current_streak += 1

    
    restart = input("\n\nRestart and change mod ? (y/n)\n>")
    while(restart == "" or not restart == "n"):
        if(restart == "y"):
            function_mod()
            break
        restart = input(">")



def nbr_to_romaji(x):
    romaji = ""
    _1 = "ichi" 
    _2 = "ni"
    _3 = "san" 
    _4 = "yon" 
    _5 = "go" 
    _6 = "roku" 
    _7 = "nana" 
    _8 = "hachi" 
    _9 = "kyuu"
    _10 = "juu"
    _100 = "hyaku"
    
    #transform nbr to romaji
    #centaines
    if(x>=900):
        romaji += _9 + _100 + " " 
        x -= 900
    elif(x>=800):
        romaji += "happyaku " 
        x -= 800
    elif(x>=700):
        romaji += _7 + _100 + " "
        x -= 700
    elif(x>=600):
        romaji += "roppyaku "
        x -= 600
    elif(x>=500):
        romaji += _5 + _100 + " "
        x -= 500    
    elif(x>=400):
        romaji += _4 + _100 + " "
        x -= 400
    elif(x>=300):
        romaji += "sanbyaku "
        x -= 300
    elif(x>=200):
        romaji += _2 + _100 + " "
        x -= 200
    elif(x>=100):
        romaji += _100 + " "
        x -= 100
        
    #dizaines
    if(x>=90):
        romaji += _9 + _10 + " " 
        x -= 90
    elif(x>=80):
        romaji += _8 + _10 + " " 
        x -= 80
    elif(x>=70):
        romaji += _7 + _10 + " "
        x -= 70
    elif(x>=60):
        romaji += _6 + _10 + " "
        x -= 60
    elif(x>=50):
        romaji += _5 + _10 + " "
        x -= 50    
    elif(x>=40):
        romaji += _4 + _10 + " "
        x -= 40
    elif(x>=30):
        romaji += _3 + _10 + " "
        x -= 30
    elif(x>=20):
        romaji += _2 + _10 + " "
        x -= 20
    elif(x>=10):
        romaji += _10 + " "
        x -= 10
            
    #unité
    if(x==9):
        romaji += _9
    elif(x==8):
        romaji += _8
    elif(x==7):
        romaji += _7
    elif(x==6):
        romaji += _6
    elif(x==5):
        romaji += _5    
    elif(x==4):
        romaji += _4
    elif(x==3):
        romaji += _3
    elif(x==2):
        romaji += _2
    elif(x==1):
        romaji += _1

    length = len(romaji)
    if(romaji[length - 1] == " "):
        romaji = romaji[0:length - 1]
            
    return(romaji)





def main():
    presentation()
    function_mod()
    
if __name__ == "__main__":
    main() 
