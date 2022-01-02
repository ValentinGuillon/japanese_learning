#choose_random_1_999.py
import random
from module_romaji_to_kana import *

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
        choice = input("Number => Hiragana (nh)\nNumber => Romaji (nr)\nHiragana => Number (h)\nRomaji => Number (r)\n>")
        while(not choice == "nh" and not choice == "nr" and not choice == "h" and not choice == "r"):
            choice = input(">")

    elif(mod == "g"):
        choice = input("Number => Romaji (nr)\nRomaji => Number (r)\n>")
        while(not choice == "nr" and not choice == "r"):
            choice = input(">")


    correct = 0
    wrong = 0
    streak = 0
    current_streak = 0
    replay = ""
    while(replay == "" or not replay == "n") :
        nbr = random.randint(1, 999)
        romaji = nbr_to_romaji(nbr)
        hiragana = romaji_to_hiragana(romaji)
        
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        if(mod == "v"):
            if(choice == "nh"):
                input(f"{nbr}\n")
                input(f"{hiragana}\n")
            elif(choice == "nr"):
                input(f"{nbr}\n")
                input(f"{romaji}\n")
            elif(choice == "h"):
                input(f"{hiragana}\n")
                input(f"{nbr}\n")
            elif(choice == "r"):
                input(f"{romaji}\n")
                input(f"{nbr}\n")

            replay = input("Again ? (Enter or n)\n>")
        

        elif(mod == "g"):
            if(choice == "nr"):
                guess = input(f""""STOP" to end the game\n===============
Correct:{correct}\nWrong:{wrong}\nBest streak:{streak}\nStreak:{current_streak}\n===============\n\n\n\n
In romaji ?\n\n{nbr}\n>""")
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

            elif(choice == "r"):
                guess = input(f""""STOP" to end the game\n===============
Correct:{correct}\nWrong:{wrong}\nBest streak:{streak}\nStreak:{current_streak}\n===============\n\n\n\n
Which number is ?\n\n{romaji}\n>""")
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

    
    restart = input("Restart and change mod ? (y/n)\n>")
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

    function_mod()
    
if __name__ == "__main__":
    main() 
