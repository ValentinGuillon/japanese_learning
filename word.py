#jap_to_fr.py
from nis import cat
import random
import module_romaji_to_kana
from module_list_jap_fr import * #class W(kana, jap, japAlt, fr, frAlt) => ex: W('h', "îe", ["iie"], "non", [])


def presentation():
    input("""
=============================
        This program
          gives you
           a word
            then
       his translation
=============================
...""")
    input("Press Enter to proceed\nwhen nothing is asked.\n...")
    input("This symbol \">\",\nmeans an answer is expected.\n=============================\n""")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

#return the game mod chosen, before launch the actual function's program
def function_mod():  
    modList = ['g', 'v'] #g = game, v = view
    mod = ""

    print("""
====== Choose program mod ===
Guess mod (g) | View mod (v)
  You have    |   Guess in
  to write    |   your mind
  the word    |   No input
  to guess    |   require
=============================""")

    while(not mod in modList):
        mod = input(">")
    main(mod)

#print current category and languages
def printOptions(mod, category, lang):
    print("===================== Mod ===")
    if mod == "g":
        print(" Game")
    elif mod == "v":
        print(" View")
    
    print("================ Category ===")
    if(category == "A"):
        print(" All")
    elif(category == "t"):
        print(" Transports")
    elif(category == "c"):
        print(" Colors")
    elif(category == "a"):
        print(" Animals")
    elif(category == "w"):
        print(" Weather")
    elif(category == "cl"):
        print(" Clothes")
    elif(category == "f"):
        print(" Food")
    elif(category == "h"):
        print(" House")
    elif(category == "d"):
        print(" Divers")
    elif(category == "vb"):
        print(" Verbs")
    elif(category == "adj"):
        print(" Adjectives")
    elif(category == "cv"):
        print(" Conjugaison of Verbs")
    elif(category == "ca"):
        print(" Conjugaison of Adjectives")
    elif(category == "e"):
        print(" Expressions")

    print("=============== Languages ===")
    for n in lang:
        if n == 'f':
            print(" French")
        if n == 'r':
            print(" Romaji")
        if n == 'h':
            print(" Hiragana")
        if n == 'k':
            print(" Katakana")
        if n == 'b' :
            print(" Random kana")
    print("=============================")

def isAnswerInAlt(answer, alt):
    if answer in alt:
        return 1

    return 0
    


def main(mod):
    #LANGUAGES CHOICE
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    lang = ""

    #ask languages for Game mod
    if(mod == "g"):
        langList = ["fr", "rf", "hr", "hf", "kr", "kf", "bf", "br"] #f = french, r = romaji, h = hira, k = kata, b = hira/kata (randomly)

        print("""
======== Choose languages ===
French   <=> Romaji (fr / rf)
Hiragana  => Romaji (hr)
Hiragana  => French (hf)
Katakana  => Romaji (kr)
Katakana  => French (kf)
Hira/Kata => Romaji (br)
Hira/Kata => French (bf)
=============================""")

        while(not lang in langList):
            lang = input(">")


    #ask languages for View mod
    if(mod == "v"):
        print("""
======== Choose languages ===
Can have multiple ones
(ex : fhr)\n
   (kana)         (alpha)
 Hiragana (h) | French (f)
 Katakana (k) | Romaji (r)
 Both (b)     |
=============================""")

        #input of languages choice
        while(not len(lang)):
            #user input (until input is allow)
            lang = input(">")

            langList = ['f', 'r', 'h', 'k', 'b'] #f = french, r = romaji, h = hira, k = kata, b = hira/kata (randomly)
            for letter in lang:
                #clear user input if one letter is not allow
                if not letter in langList:
                    lang = ""
                    break


    #characters CATEGORY CHOICE
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    category = ""

    print("""
========= Choose category ===
All (A) (except the last 2)

Transports (t) | Colors (c)
Animals (a)    | Weather (w)
Clothes (cl)   | Food (f)
House (h)      |
Divers (d)     |

Verbs (vb) | Adjectives (adj)
Expressions (e)

Conjug of verbs (cv)
Conjug of adjectives (ca)
=============================""")

    categList = ["A", "t", "c", "a", "w", "cl", "f", "h", "d", "vb", "adj", "e", "cv", "ca"]
    while(not category in categList):
        category = input(">")


    correct = 0 
    wrong = 0
    streak = 0
    streakCurrent = 0
    stop = ""
    while(not stop == "STOP"):
        iIndex = 0
        borneMin = 0
        borneMax = len(all) -1
        
        #a word is randomly choose, bases on the category
        if(category == "A"):
            iIndex = random.randint(0, len(all) - 1)

        borneMin = 0
        borneMax = len(transports) -1
        if(category == "t"):
            iIndex = random.randint(borneMin, borneMax)

        borneMin = borneMax + 1
        borneMax += len(colors)
        if(category == "c"):
            iIndex = random.randint(borneMin, borneMax)

        borneMin = borneMax + 1
        borneMax += len(animals)
        if(category == "a"):
            iIndex = random.randint(borneMin, borneMax)

        borneMin = borneMax + 1
        borneMax += len(weather)
        if(category == "w"):
            iIndex = random.randint(borneMin, borneMax)

        borneMin = borneMax + 1
        borneMax += len(clothes)
        if(category == "cl"):
            iIndex = random.randint(borneMin, borneMax)

        borneMin = borneMax + 1
        borneMax += len(food)
        if(category == "f"):
            iIndex = random.randint(borneMin, borneMax)

        borneMin = borneMax + 1
        borneMax += len(house)
        if(category == "h"):
            iIndex = random.randint(borneMin, borneMax)

        borneMin = borneMax + 1
        borneMax += len(divers)
        if(category == "d"):
            iIndex = random.randint(borneMin, borneMax)

        borneMin = borneMax + 1
        borneMax += len(verbs)
        if(category == "vb"):
            iIndex = random.randint(borneMin, borneMax)

        borneMin = borneMax + 1
        borneMax += len(adjs)
        if(category == "adj"):
            iIndex = random.randint(borneMin, borneMax)

        borneMin = borneMax + 1
        borneMax += len(expressions)
        print(borneMin, borneMax)
        if(category == "e"):
            iIndex = random.randint(borneMin, borneMax)

        if(category == "cv"):
            iIndex = random.randint(0, len(conjug_verbs) - 1)
        if(category == "ca"):
            iIndex = random.randint(0, len(conjug_adjs) - 1)

        if(category not in categList):
            input("Error...\nRestarting...")
            main(mod)
        
        word = W('', "", [], "", [])
        word_romaji = "[none]"
        word_fr = "[none]"
        #origin = '' #= word.kana

        if(category in categList and category != "cv" and category != "ca"):
            word = all[iIndex]
            word_romaji = word.jap
            word_fr = word.fr
        if(category == "cv"):
            word = conjug_verbs[iIndex]
            word_romaji = word.jap
            word_fr = word.fr
        if(category == "ca"):
            word = conjug_adjs[iIndex]
            word_romaji = word.jap
            word_fr = word.fr





        word_hira = module_romaji_to_kana.romaji_to_hira(word_romaji)
        word_kata = module_romaji_to_kana.romaji_to_kata(word_romaji)


        #VIEW MOD process
        if(mod == "v"):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            printOptions(mod, category, lang)
            print("Tap \"STOP\" to end\n\n")

            for n in lang:
                if(not stop == "STOP"):
                    if n == 'f':
                        stop = input(f"{word_fr}\n")
                    if n == 'r':
                        stop = input(f"{word_romaji}\n")
                    if n == 'h':
                        stop = input(f"{word_hira}\n")
                    if n == 'k':
                        stop = input(f"{word_kata}\n")
                    if n == 'b' :
                        if (random.randint(0, 1)):
                            stop = input(f"{word_hira}\n")
                        else :
                            stop = input(f"{word_kata}\n")



        #GAME MOD process
        if(mod == "g"):

            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            printOptions(mod, category, lang)
            print(f"""================== Scores ===
 Correct:{correct}
 Wrong:{wrong}
 Best streak:{streak}
 Streak:{streakCurrent}
=============================
Tap "STOP" to end\n\n""")


            #random choice of kana
            saveLang = lang
            if lang[0] == 'b':
                if (random.randint(0, 1)):
                    lang = 'h' + lang[1]
                else:
                    lang = 'k' + lang[1]


            if(lang == "fr"):
                #user guess
                guess = str.lower(input(f"In romaji ?\n\n {word_fr}\n>"))

                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess
                if(guess == str.lower(word_romaji) or isAnswerInAlt(guess, word.japAlt)):
                    correct += 1
                    streakCurrent += 1
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_romaji}\"")
                    wrong += 1
                    if(streakCurrent > streak):
                        streak = streakCurrent
                    streakCurrent = 0

                    if(len(word.japAlt)):
                        if(input("Wanna see alternative ? (y/Enter)>") == 'y'):
                            for n in word.japAlt:
                                print(f" {n}")
                            input()
                    else:
                        input()

            elif(lang == "rf"):
                #user guess
                guess = str.lower(input(f"In french ?\n\n {word_romaji}\n>"))

                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess
                elif(guess == str.lower(word_fr) or isAnswerInAlt(guess, word.frAlt)):
                    correct += 1
                    streakCurrent += 1
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_fr}\"")
                    wrong += 1
                    if(streakCurrent > streak):
                        streak = streakCurrent
                    streakCurrent = 0

                    if(len(word.frAlt)):
                        if(input("Wanna see alternative ? (y/Enter)>") == 'y'):
                            for n in word.frAlt:
                                print(f" {n}")
                            input()
                    else:
                        input()

            elif(lang == "hr"):
                #user guess
                guess = str.lower(input(f"In romaji ?\n\n {word_hira}\n>"))

                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess
                if(guess == str.lower(word_romaji) or isAnswerInAlt(guess, word.japAlt)):
                    correct += 1
                    streakCurrent += 1
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_romaji}\"")
                    wrong += 1
                    if(streakCurrent > streak):
                        streak = streakCurrent
                    streakCurrent = 0

                    if(len(word.japAlt)):
                        if(input("Wanna see alternative ? (y/Enter)>") == 'y'):
                            for n in word.japAlt:
                                print(f" {n}")
                            input()
                    else:
                        input()

            elif(lang == "hf"):
                #user guess
                guess = str.lower(input(f"In french ?\n\n {word_hira}\n>"))

                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess
                if(guess == str.lower(word_fr) or isAnswerInAlt(guess, word.frAlt)):
                    correct += 1
                    streakCurrent += 1
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_fr}\"")
                    wrong += 1
                    if(streakCurrent > streak):
                        streak = streakCurrent
                    streakCurrent = 0

                    if(len(word.frAlt)):
                        if(input("Wanna see alternative ? (y/Enter)>") == 'y'):
                            for n in word.frAlt:
                                print(f" {n}")
                            input()
                    else:
                        input()

            elif(lang == "kr"):
                #user guess
                guess = str.lower(input(f"In romaji ?\n\n {word_kata}\n>"))

                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess
                if(guess == str.lower(word_romaji) or isAnswerInAlt(guess, word.japAlt)):
                    correct += 1
                    streakCurrent += 1
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_romaji}\"")
                    wrong += 1
                    if(streakCurrent > streak):
                        streak = streakCurrent
                    streakCurrent = 0

                    if(len(word.japAlt)):
                        if(input("Wanna see alternative ? (y/Enter)>") == 'y'):
                            for n in word.japAlt:
                                print(f" {n}")
                            input()
                    else:
                        input()

            elif(lang == "kf"):
                #user guess
                guess = str.lower(input(f"In french ?\n\n {word_kata}\n>"))
                                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess
                if(guess == str.lower(word_fr) or isAnswerInAlt(guess, word.frAlt)):
                    correct += 1
                    streakCurrent += 1
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_fr}\"")
                    wrong += 1
                    if(streakCurrent > streak):
                        streak = streakCurrent
                    streakCurrent = 0

                    if(len(word.frAlt)):
                        if(input("Wanna see alternative ? (y/Enter)>") == 'y'):
                            for n in word.frAlt:
                                print(f" {n}")
                            input()
                    else:
                        input()
            
            #reset language
            lang = saveLang
                




    restart = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRestart and change mod ? (y/n)\n>")
    while(restart == "" or not restart == "n"):
        if(restart == "y"):
            function_mod()
            break
        restart = input(">")
    
    


if __name__ == "__main__":
    presentation()    
    function_mod()
