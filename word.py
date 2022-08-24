#jap_to_fr.py
from module_list_jap_fr import *
import random
from module_romaji_to_kana import *


def function_mod():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") 
    mod = input("""Program mod :
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
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if(mod == "g"):
        lang = input("Langage mod :\nFrench => Romaji (fr)\nRomaji => French (rf)\nHiragana => Romaji (hr)\nHiragana => French (hf)\nKatagana => Romaji (kr)\nKatagana => French (kf)\n>")
        #Katagana => Romaji, Katagana => French
        while(not lang == "fr" and not lang == "rf" and not lang == "hr" and not lang == "hf" and not lang == "kr" and not lang == "kf"):
            lang = input(">")
    
    if(mod == "v"):
        lang = input("Language mod :\nHiragana:\nFrench => Hiragana => Romaji (fhr)\nFrench => Romaji => Hiragana (frh)\nRomaji => Hiragana => French (rhf)\nHiragana => Romaji => French (hrf)\n\nKatagana :\nFrench => Katagana => Romaji (fkr)\nFrench => Romaji => Katagana (frk)\nRomaji => Katagana => French (rkf)\nKatagana => Romaji => French (krf)\n>")
        #, French => Katagana => Romaji, , French => Romaji => Katagana
        #, Romaji => Katagana => French, , Katagana => Romaji => French
        while(not lang == "fhr" and not lang == "frh" and not lang == "rhf" and not lang == "hrf" and not lang == "fkr" and not lang == "frk" and not lang == "rkf" and not lang == "krf"):
            lang = input(">")

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    category = input("""
Choose the category :

All (but last 3) (A)

Transports (t) | Colors (c)
Animals (a)    | Weather (w)
Clothes (cl)   | Food (f)
Divers (d)

Verbs (vb) | Adjectifs (adj)

Conjug of verbs (cv)
Conjug of adjectifs (ca)
Expressions (e)
>""")
    while(not category == "A" and not category == "t" and not category == "c" and not category == "a" and not category == "w" and not category == "cl" and not category == "f" and not category == "d" and not category == "vb" and not category == "adj" and not category == "cv" and not category == "ca" and not category == "e"):
        category = input(">")

    correct = 0
    wrong = 0
    streak = 0
    current_streak = 0

    stop = ""
    while(not stop == "STOP"):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\"STOP\" to end\n\n\n\n\n") 
        word_romaji = "[none]"
        word_fr = "[none]"
        
        if(category == "A"):
            i = random.randint(0, len(all_jap) - 1)
            word_romaji = all_jap[i]
            word_fr = all_fr[i]
        elif(category == "t"):
            i = random.randint(0, len(transports_jap) - 1)
            word_romaji = transports_jap[i]
            word_fr = transports_fr[i]
        elif(category == "c"):
            i = random.randint(0, len(colors_jap) - 1)
            word_romaji = colors_jap[i]
            word_fr = colors_fr[i]
        elif(category == "a"):
            i = random.randint(0, len(animals_jap) - 1)
            word_romaji = animals_jap[i]
            word_fr = animals_fr[i]
        elif(category == "w"):
            i = random.randint(0, len(weather_jap) - 1)
            word_romaji = weather_jap[i]
            word_fr = weather_fr[i]
        elif(category == "cl"):
            i = random.randint(0, len(clothes_jap) - 1)
            word_romaji = clothes_jap[i]
            word_fr = clothes_fr[i]
        elif(category == "f"):
            i = random.randint(0, len(food_jap) - 1)
            word_romaji = food_jap[i]
            word_fr = food_fr[i]
        elif(category == "d"):
            i = random.randint(0, len(divers_jap) - 1)
            word_romaji = divers_jap[i]
            word_fr = divers_fr[i]
        elif(category == "vb"):
            i = random.randint(0, len(verbs_jap) - 1)
            word_romaji = verbs_jap[i]
            word_fr = verbs_fr[i]
        elif(category == "adj"):
            i = random.randint(0, len(adjs_jap) - 1)
            word_romaji = adjs_jap[i]
            word_fr = adjs_fr[i]
        elif(category == "cv"):
            i = random.randint(0, len(conjug_verbs_jap) - 1)
            word_romaji = conjug_verbs_jap[i]
            word_fr = conjug_verbs_fr[i]
        elif(category == "ca"):
            i = random.randint(0, len(conjug_adjs_jap) - 1)
            word_romaji = conjug_adjs_jap[i]
            word_fr = conjug_adjs_fr[i]
        elif(category == "e"):
            i = random.randint(0, len(expressions_jap) - 1)
            word_romaji = expressions_jap[i]
            word_fr = expressions_fr[i]
        else:
            print(word_romaji)
            print("Restarting...")
            function(mod)
        
        word_hiragana = romaji_to_hiragana(word_romaji)
        word_katagana = romaji_to_katagana(word_romaji)

        if(mod == "v"):
            if(lang == "fhr"):
                stop = input(f"{word_fr}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_hiragana}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_romaji}\n")

            elif(lang == "frh"):
                stop = input(f"{word_fr}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_romaji}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_hiragana}\n")
            
            elif(lang == "rhf"):
                stop = input(f"{word_romaji}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_hiragana}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_fr}\n")

            elif(lang == "hrf"):
                stop = input(f"{word_hiragana}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_romaji}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_fr}\n")

            elif(lang == "fkr"):
                stop = input(f"{word_fr}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_katagana}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_romaji}\n")

            elif(lang == "frk"):
                stop = input(f"{word_fr}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_romaji}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_katagana}\n")

            elif(lang == "rkf"):
                stop = input(f"{word_romaji}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_katagana}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_fr}\n")

            elif(lang == "krf"):
                stop = input(f"{word_katagana}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_romaji}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_fr}\n")
                



        if(mod == "g"):
            if(lang == "fr"):
                guess = str.lower(input(f""""STOP" to end the game\n===============
Correct:{correct}\nWrong:{wrong}\nBest streak:{streak}\nStreak:{current_streak}\n===============\n\n\n\nIn romaji ?\n\n{word_fr}\n>"""))
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str.lower(word_romaji)):
                    input(f"""Oupsi. C'était "{word_romaji}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                elif(guess == str.lower(word_romaji)):
                    correct += 1
                    current_streak += 1

            elif(lang == "rf"):
                guess = str.lower(input(f""""STOP" to end the game\n===============
Correct:{correct}\nWrong:{wrong}\nBest streak:{streak}\nStreak:{current_streak}\n===============\n\n\n\nIn french ?\n\n{word_romaji}\n>"""))
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str.lower(word_fr)):
                    input(f"""Oupsi. C'était "{word_fr}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                elif(guess == str.lower(word_fr)):
                    correct += 1
                    current_streak += 1

            elif(lang == "hr"):
                guess = str.lower(input(f""""STOP" to end the game\n===============
Correct:{correct}\nWrong:{wrong}\nBest streak:{streak}\nStreak:{current_streak}\n===============\n\n\n\nIn romaji ?\n\n{word_hiragana}\n>"""))
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str.lower(word_romaji)):
                    input(f"""Oupsi. C'était "{word_romaji}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                elif(guess == str.lower(word_romaji)):
                    correct += 1
                    current_streak += 1

            elif(lang == "hf"):
                guess = str.lower(input(f""""STOP" to end the game\n===============
Correct:{correct}\nWrong:{wrong}\nBest streak:{streak}\nStreak:{current_streak}\n===============\n\n\n\nIn french ?\n\n{word_hiragana}\n>"""))
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str.lower(word_fr)):
                    input(f"""Oupsi. C'était "{word_fr}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                elif(guess == str.lower(word_fr)):
                    correct += 1
                    current_streak += 1

            elif(lang == "kr"):
                guess = str.lower(input(f""""STOP" to end the game\n===============
Correct:{correct}\nWrong:{wrong}\nBest streak:{streak}\nStreak:{current_streak}\n===============\n\n\n\nIn romaji ?\n\n{word_katagana}\n>"""))
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str.lower(word_romaji)):
                    input(f"""Oupsi. C'était "{word_romaji}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                elif(guess == str.lower(word_romaji)):
                    correct += 1
                    current_streak += 1

            elif(lang == "kf"):
                guess = str.lower(input(f""""STOP" to end the game\n===============
Correct:{correct}\nWrong:{wrong}\nBest streak:{streak}\nStreak:{current_streak}\n===============\n\n\n\nIn french ?\n\n{word_katagana}\n>"""))
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str.lower(word_fr)):
                    input(f"""Oupsi. C'était "{word_fr}"\n""")
                    wrong += 1
                    if(current_streak > streak):
                        streak = current_streak
                    current_streak = 0
                elif(guess == str.lower(word_fr)):
                    correct += 1
                    current_streak += 1
                

    restart = input("\n\nRestart and change mod ? (y/n)\n>")
    while(restart == "" or not restart == "n"):
        if(restart == "y"):
            function_mod()
            break
        restart = input(">")
    
    
    


def main():
    input("""
=============================
        This program
         gives you
           a word
            then
       a translation
=============================
...
""")
    input("""Press Enter to proceed
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
