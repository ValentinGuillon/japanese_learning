#jap_to_fr.py
import random
import module_romaji_to_kana
from module_list_jap_fr import * #class W(kana, jap, fr) => ex: W('h', "kuro", "noir")


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
            langList = ['f', 'r', 'h', 'k', 'b'] #f = french, r = romaji, h = hira, k = kata, b = hira/kata (randomly)
            #user input
            lang = input(">")
            for letter in lang:
                #clear user input if one letter is not allow
                if not letter in langList:
                    lang = ""
                    break


    #CATEGORY CHOICE
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    categList = ["A", "t", "c", "a", "w", "cl", "f", "h", "d", "vb", "adj", "cv", "ca", "e"]
    category = ""

    print("""
========= Choose category ===
All (A) (except the last 3)

Transports (t) | Colors (c)
Animals (a)    | Weather (w)
Clothes (cl)   | Food (f)
House (h)      |
Divers (d)     |

Verbs (vb) | Adjectives (adj)

Conjug of verbs (cv)
Conjug of adjectives (ca)
Expressions (e)
=============================""")

    while(not category in categList):
        category = input(">")

    #var used for Game mod
    correct = 0 
    wrong = 0
    streak = 0
    current_streak = 0

    stop = ""
    while(not stop == "STOP"):
        word_romaji = "[none]"
        word_fr = "[none]"
        #origin = '' #= word.kana
        
        #a word is randomly choose, bases on the category
        if(category == "A"):
            i = random.randint(0, len(all) - 1)
            word_romaji = all[i].jap
            word_fr = all[i].fr
        elif(category == "t"):
            i = random.randint(0, len(transports) - 1)
            word_romaji = transports[i].jap
            word_fr = transports[i].fr
        elif(category == "c"):
            i = random.randint(0, len(colors) - 1)
            word_romaji = colors[i].jap
            word_fr = colors[i].fr
        elif(category == "a"):
            i = random.randint(0, len(animals) - 1)
            word_romaji = animals[i].jap
            word_fr = animals[i].fr
        elif(category == "w"):
            i = random.randint(0, len(weather) - 1)
            word_romaji = weather[i].jap
            word_fr = weather[i].fr
        elif(category == "cl"):
            i = random.randint(0, len(clothes) - 1)
            word_romaji = clothes[i].jap
            word_fr = clothes[i].fr
        elif(category == "f"):
            i = random.randint(0, len(food) - 1)
            word_romaji = food[i].jap
            word_fr = food[i].fr
        elif(category == "h"):
            i = random.randint(0, len(house) - 1)
            word_romaji = house[i].jap
            word_fr = house[i].fr
        elif(category == "d"):
            i = random.randint(0, len(divers) - 1)
            word_romaji = divers[i].jap
            word_fr = divers[i].fr
        elif(category == "vb"):
            i = random.randint(0, len(verbs) - 1)
            word_romaji = verbs[i].jap
            word_fr = verbs[i].fr
        elif(category == "adj"):
            i = random.randint(0, len(adjs) - 1)
            word_romaji = adjs[i].jap
            word_fr = adjs[i].fr
        elif(category == "cv"):
            i = random.randint(0, len(conjug_verbs) - 1)
            word_romaji = conjug_verbs[i].jap
            word_fr = conjug_verbs[i].fr
        elif(category == "ca"):
            i = random.randint(0, len(conjug_adjs) - 1)
            word_romaji = conjug_adjs[i].jap
            word_fr = conjug_adjs[i].fr
        elif(category == "e"):
            i = random.randint(0, len(expressions) - 1)
            word_romaji = expressions[i].jap
            word_fr = expressions[i].fr
        else:
            print(word_romaji)
            print("Restarting...")
            main(mod)
        
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
 Streak:{current_streak}
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
                #wrong guess
                if(not guess == str.lower(word_romaji)):
                    input(f"""Oupsi. C'était "{word_romaji}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                #good guess
                elif(guess == str.lower(word_romaji)):
                    correct += 1
                    current_streak += 1

            elif(lang == "rf"):
                #user guess
                guess = str.lower(input(f"In french ?\n\n {word_romaji}\n>"))

                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #wrong guess
                if(not guess == str.lower(word_fr)):
                    input(f"""Oupsi. C'était "{word_fr}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                #good guess
                elif(guess == str.lower(word_fr)):
                    correct += 1
                    current_streak += 1

            elif(lang == "hr"):
                #user guess
                guess = str.lower(input(f"In romaji ?\n\n {word_hira}\n>"))

                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #wrong guess
                if(not guess == str.lower(word_romaji)):
                    input(f"""Oupsi. C'était "{word_romaji}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                #good guess
                elif(guess == str.lower(word_romaji)):
                    correct += 1
                    current_streak += 1

            elif(lang == "hf"):
                #user guess
                guess = str.lower(input(f"In french ?\n\n {word_hira}\n>"))

                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #wrong guess
                if(not guess == str.lower(word_fr)):
                    input(f"""Oupsi. C'était "{word_fr}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                #user guess
                elif(guess == str.lower(word_fr)):
                    correct += 1
                    current_streak += 1

            elif(lang == "kr"):
                #user guess
                guess = str.lower(input(f"In romaji ?\n\n {word_kata}\n>"))

                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #wrong guess
                if(not guess == str.lower(word_romaji)):
                    input(f"""Oupsi. C'était "{word_romaji}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                #user guess
                elif(guess == str.lower(word_romaji)):
                    correct += 1
                    current_streak += 1

            elif(lang == "kf"):
                #user guess
                guess = str.lower(input(f"In french ?\n\n {word_kata}\n>"))
                                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #wrong guess
                if(not guess == str.lower(word_fr)):
                    input(f"""Oupsi. C'était "{word_fr}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                #user guess
                elif(guess == str.lower(word_fr)):
                    correct += 1
                    current_streak += 1
            
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
