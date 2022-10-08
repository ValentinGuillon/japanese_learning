#jap_to_fr.py
from module_list_jap_fr import *
import random
from module_romaji_to_kana import *


def presentation():
    input("""
===========================================
        This program
         gives you
           a word
            then
       a translation
===========================================
...
""")
    input("""Press Enter to proceed
when nothing is asked.
...
""")
    input("""This symbol ">",
means an answer is expected.
===========================================
""")

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
        lang = input("Langage mod :\nFrench => Romaji (fr)\nRomaji => French (rf)\nHiragana => Romaji (hr)\nHiragana => French (hf)\nkatakana => Romaji (kr)\nkatakana => French (kf)\n>")
        #katakana => Romaji, katakana => French
        while(not lang == "fr" and not lang == "rf" and not lang == "hr" and not lang == "hf" and not lang == "kr" and not lang == "kf"):
            lang = input(">")
    
    if(mod == "v"):
        '''
        lang = input("Language mod :\nHiragana:\nFrench => Hiragana => Romaji (fhr)\nFrench => Romaji => Hiragana (frh)\nRomaji => Hiragana => French (rhf)\nHiragana => Romaji => French (hrf)\n\nkatakana :\nFrench => katakana => Romaji (fkr)\nFrench => Romaji => katakana (frk)\nRomaji => katakana => French (rkf)\nkatakana => Romaji => French (krf)\n>")'''

        lang = input("Language mod :\n(choose 3 langage) (ex : fhr)\n(can only have 1 kana type)\n\n French (f)\n Romaji (r)\n Hiragana (h)\n Katakana (k)\n>")
        
        #, French => katakana => Romaji, , French => Romaji => katakana
        #, Romaji => katakana => French, , katakana => Romaji => French
        while(not lang == "fhr" and not lang == "frh" and not lang == "rhf" and not lang == "hrf" and not lang == "fkr" and not lang == "frk" and not lang == "rkf" and not lang == "krf"):
            lang = input(">")

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
            function(mod)
        
        word_hira = romaji_to_hira(word_romaji)
        word_kata = romaji_to_kata(word_romaji)

        if(mod == "v"):
            if(lang == "fhr"):
                stop = input(f"{word_fr}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_hira}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_romaji}\n")

            elif(lang == "frh"):
                stop = input(f"{word_fr}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_romaji}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_hira}\n")
            
            elif(lang == "rhf"):
                stop = input(f"{word_romaji}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_hira}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_fr}\n")

            elif(lang == "hrf"):
                stop = input(f"{word_hira}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_romaji}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_fr}\n")

            elif(lang == "fkr"):
                stop = input(f"{word_fr}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_kata}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_romaji}\n")

            elif(lang == "frk"):
                stop = input(f"{word_fr}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_romaji}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_kata}\n")

            elif(lang == "rkf"):
                stop = input(f"{word_romaji}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_kata}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_fr}\n")

            elif(lang == "krf"):
                stop = input(f"{word_kata}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_romaji}\n")
                if(not stop == "STOP"):
                    stop = input(f"{word_fr}\n")
                



        if(mod == "g"):
            if(lang == "fr"):
                guess = str.lower(input(f""""STOP" to end the game\n=============================
Correct:{correct}\nWrong:{wrong}\nBest streak:{streak}\nStreak:{current_streak}\n=============================\n\n\n\nIn romaji ?\n\n{word_fr}\n>"""))
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
                guess = str.lower(input(f""""STOP" to end the game\n=============================
Correct:{correct}\nWrong:{wrong}\nBest streak:{streak}\nStreak:{current_streak}\n=============================\n\n\n\nIn french ?\n\n{word_romaji}\n>"""))
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
                guess = str.lower(input(f""""STOP" to end the game\n=============================
Correct:{correct}\nWrong:{wrong}\nBest streak:{streak}\nStreak:{current_streak}\n=============================\n\n\n\nIn romaji ?\n\n{word_hira}\n>"""))
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
                guess = str.lower(input(f""""STOP" to end the game\n=============================
Correct:{correct}\nWrong:{wrong}\nBest streak:{streak}\nStreak:{current_streak}\n=============================\n\n\n\nIn french ?\n\n{word_hira}\n>"""))
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
                guess = str.lower(input(f""""STOP" to end the game\n=============================
Correct:{correct}\nWrong:{wrong}\nBest streak:{streak}\nStreak:{current_streak}\n=============================\n\n\n\nIn romaji ?\n\n{word_kata}\n>"""))
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
                guess = str.lower(input(f""""STOP" to end the game\n=============================
Correct:{correct}\nWrong:{wrong}\nBest streak:{streak}\nStreak:{current_streak}\n=============================\n\n\n\nIn french ?\n\n{word_kata}\n>"""))
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
    presentation()    
    function_mod()

if __name__ == "__main__":
    main() 
