#numbers.py
import random
import module_romaji_to_kana


#receive a int, and return it as a romaji str
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

    if(romaji[len(romaji) - 1] == " "):
        romaji = romaji[0:len(romaji) - 1]
            
    return(romaji)





def presentation():
    input("""
=============================
        This program
     gives you a number
     between 1 and 999
        in japanese
=============================
...""")
    input("Press Enter to proceed\nwhen nothing is asked.\n...")
    input("This symbol \">\",\nmeans an answer is expected.\n=============================\n""")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

#print current category and languages
def printOptions(mod, lang):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("===================== Mod ===")
    
    if mod == "g":
        print(" Game")
        print("=============== Languages ===")
        if lang == 'n':
            print(" Number\n Romaji")
        if lang == 'r':
            print(" Romaji\n Number")
        if lang == 'h':
            print(" Hiragana\n Number")
        if lang == 'k':
            print(" Katakana\n Number")
        if lang == 'b':
            print(" Random kana\n Number")


    elif mod == "v":
        print(" View")
        print("=============== Languages ===")
        for n in lang:
            if n == 'n':
                print(" Number")
            if n == 'r':
                print(" Romaji")
            if n == 'h':
                print(" Hiragana")
            if n == 'k':
                print(" Katakana")
            if n == 'b':
                print(" Random kana")

    print("=============================")






def function_mod():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("""
====== Choose program mod ===
Guess mod (g) | View mod (v)
  You have    |   Guess in
  to write    |   your mind
  the word    |   No input
  to guess    |   require
=============================""")

    mod = ""
    while(not mod == "g" and not mod == "v"):
        mod = input(">")

    main(mod)





def main(mod):    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("======== Choose languages ===")
    lang = ""


    #VIEW MOD languages selection
    if(mod == "v"):
        print("""Can have multiple ones
(ex : nhr)\n
   (kana)
 Hiragana (h) | Number (n)
 Katakana (k) | Romaji (r)
 Random   (b) |
=============================""")

        #input/verif of languages choice
        while(not len(lang)):
            langList = ['n', 'r', 'h', 'k', 'b'] #n = number, r = romaji, h = hira, k = kata, b = hira/kata (randomly)
            #user input
            lang = input(">")
            for letter in lang:
                #clear user input if one letter is not allow
                if not letter in langList:
                    lang = ""
                    break

    #GAME MOD languages selection
    elif(mod == "g"):
        print(" Number => Romaji (n)\n Romaji => Number (r)\n Hiragana => Number (h)\n Katakana => Number (k)\n Hira/Kata => Number (b)\n=============================")
        
        langList = ["n", "r", "h", "k", 'b']
        while(not lang in langList):
            lang = input(">")


    correct = 0
    wrong = 0
    streak = 0
    currentStreak = 0
    stop = ""
    while(not stop == "STOP") :
        nbr = random.randint(1, 999)
        romaji = nbr_to_romaji(nbr)
        hira = module_romaji_to_kana.romaji_to_hira(romaji)
        kata = module_romaji_to_kana.romaji_to_kata(romaji)
        
        printOptions(mod, lang)
    

        if(mod == "v"):
            print("\"STOP\" to end\n\n")
            for n in lang:
                if(not stop == "STOP"):
                    if n == "n":
                        stop = input(f"{nbr}\n")
                    if n == "r":
                        stop = input(f"{romaji}\n")
                    if n == "h":
                        stop = input(f"{hira}\n")
                    if n == "k":
                        stop = input(f"{kata}\n")
                    if n == "b":
                        if(random.randint(0,1)):
                            stop = input(f"{hira}\n")
                        else:
                            stop = input(f"{kata}\n")

        

        elif(mod == "g"):
            print(f"""================== Scores ===
 Correct:{correct}
 Wrong:{wrong}
 Best streak:{streak}
 Streak:{currentStreak}
=============================
Tap "Stop" to end\n\n""")

        
            saveLang = lang
            if lang == 'b':
                if (random.randint(0, 1)):
                    lang = 'h'
                else:
                    lang = 'k'

            if(lang == "n"):
                guess = input(f"In romaji ?\n\n {nbr}\n>")
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str.lower(romaji)):
                    input(f"""Oupsi. C'était "{romaji}"\n""")
                    wrong += 1
                    if(currentStreak > streak):
                        streak = currentStreak
                    currentStreak = 0
                elif(str.lower(guess) == romaji):
                    correct += 1
                    currentStreak += 1

            elif(lang == "r"):
                guess = input(f"Which number is it ?\n\n {romaji}\n>")
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str(nbr)):
                    input(f"""Oupsi. C'était "{nbr}"\n""")
                    wrong += 1
                    if(currentStreak > streak):
                        streak = currentStreak
                    currentStreak = 0
                elif(guess == str(nbr)):
                    correct += 1
                    currentStreak += 1

            elif(lang == "h"):
                guess = input(f"Which number is it ?\n\n {hira}\n>")
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str(nbr)):
                    input(f"""Oupsi. C'était "{nbr}"\n""")
                    wrong += 1
                    if(currentStreak > streak):
                        streak = currentStreak
                    currentStreak = 0
                elif(guess == str(nbr)):
                    correct += 1
                    currentStreak += 1

            elif(lang == "k"):
                guess = input(f"Which number is it ?\n\n {kata}\n>")
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str(nbr)):
                    input(f"""Oupsi. C'était "{nbr}"\n""")
                    wrong += 1
                    if(currentStreak > streak):
                        streak = currentStreak
                    currentStreak = 0
                elif(guess == str(nbr)):
                    correct += 1
                    currentStreak += 1

            #reset language
            lang = saveLang

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    restart = ""
    print("Restart and change mod ? (y/n)")
    while(restart == "" or not restart == "n"):
        if(restart == "y"):
            function_mod()
            break
        restart = input(">")





if __name__ == "__main__":
    presentation()
    function_mod()
