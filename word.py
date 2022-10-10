#jap_to_fr.py
from module_list_jap_fr import *
import random
from module_romaji_to_kana import *


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
    input("""Press Enter to proceed
when nothing is asked.
...""")
    input("""This symbol ">",
means an answer is expected.
=============================
""")

#return the game choose, before launch the program
def function_mod():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") 
    mod = input("""=== Choose program mod ======
Guess mod (g) | View mod (v)
  You have    |   Guess in
  to write    |   your mind
  the word    |   No input
  to guess    |   require
=============================
>""")
    while(not mod == "g" and not mod == "v"):
        mod = input(">")
    main(mod)

#print current category and languages
def printOptions(mod, category, lang):
    print("=== Mod =====================")
    if mod == "g":
        print(" Game")
    elif mod == "v":
        print(" View")
    
    print("=== Category ================")
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
    
    print("=== Languages ===============")
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
            print(" Random Kana")
    print("=============================")

    


def main(mod):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if(mod == "g"):
        lang = input("Langage mod :\nFrench   <=> Romaji (fr / rf)\nHiragana  => Romaji (hr)\nHiragana  => French (hf)\nKatakana  => Romaji (kr)\nKatakana  => French (kf)\nHira/Kata => Romaji (br)\nHira/Kata => French (bf)\n>")
        #katakana => Romaji, katakana => French
        while(not lang == "fr" and not lang == "rf" and not lang == "hr" and not lang == "hf" and not lang == "kr" and not lang == "kf" and not lang == "bf" and not lang == "br"):
            lang = input(">")
    
    if(mod == "v"):
        print("Language mod :\n(choose 3 langage) (ex : fhr)\n(can only have 1 kana type)\n\n French (f)\n Romaji (r)\n Hiragana (h)\n Katakana (k)\n Both (b)")

        #input of languages choice
        lang = ""
        while(not len(lang)):
            #user input
            lang = input(">")
            for letter in lang:
                print(letter)
                if not letter == 'f' and not letter == 'r' and not letter == 'h' and not letter == 'k' and not letter == 'b':
                    lang = ""

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    category = input("""
Choose the category :

All (A) (exept 3 lasts)

Transports (t) | Colors (c)
Animals (a)    | Weather (w)
Clothes (cl)   | Food (f)
House (h)
Divers (d)

Verbs (vb) | Adjectifs (adj)

Conjug of verbs (cv)
Conjug of adjectifs (ca)
Expressions (e)
>""")
    while(not category == "A" and not category == "t" and not category == "c" and not category == "a" and not category == "w" and not category == "cl" and not category == "f" and not category == "h" and not category == "d" and not category == "vb" and not category == "adj" and not category == "cv" and not category == "ca" and not category == "e"):
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
        #origin = '' = word.kana
        
        #un mot est aléatoirement choisis
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
        
        word_hira = romaji_to_hira(word_romaji)
        word_kata = romaji_to_kata(word_romaji)


        #VIEW MOD
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



        #GAME MOD
        if(mod == "g"):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            printOptions(mod, category, lang)
            print(f"""=== Scores ==================
Correct:{correct}
Wrong:{wrong}
Best streak:{streak}
Streak:{current_streak}
=============================
Tap "STOP" to end\n\n""")


            #random choice of kana
            tempLang = lang
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
            lang = tempLang
                




    restart = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRestart and change mod ? (y/n)\n>")
    while(restart == "" or not restart == "n"):
        if(restart == "y"):
            function_mod()
            break
        restart = input(">")
    
    


if __name__ == "__main__":
    presentation()    
    function_mod()
