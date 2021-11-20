#jap_to_fr.py
from module_list_jap_fr import *
import random
from romaji_to_kana import romaji_to_hiragana


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
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if(mod == "g"):
        choose = input("Language mod :\nFrench => Romaji (fr)\nRomaji => French (rf)\nHiragana => Romaji (hr)\nHiragana => French (hf)\n>")
        #Katagana => Romaji, Katagana => French
        while(not choose == "fr" and not choose == "rf" and not choose == "hr" and not choose == "hf"):
            choose = input(">")
    
    if(mod == "v"):
        choose = input("Language mod :\nFrench => Hiragana => Romaji (fhr)\nFrench => Romaji => Hiragana (frh)\nRomaji => Hiragana => French (rhf)\nHiragana => Romaji => French (hrf)\n>")
        #, French => Katagana => Romaji, , French => Romaji => Katagana
        #, Romaji => Katagana => French, , Katagana => Romaji => French
        while(not choose == "fhr" and not choose == "frh" and not choose == "rhf" and not choose == "hrf"):
            choose = input(">")

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    choice = input("""
Choose the category :
    
All (but last 3) (A)

Transports (t) | Colors (c)
Animals (a)    | Weather (w)
Clothes (cl)   | Food (f)

Verbs (vb) | Adjectifs (adj)

Conjug of verbs (cv)
Conjug of adjectifs (ca)
Expressions (e)
>""")
    while(not choice == "A" and not choice == "t" and not choice == "c" and not choice == "a" and not choice == "w" and not choice == "cl" and not choice == "f" and not choice == "vb" and not choice == "adj" and not choice == "cv" and not choice == "ca" and not choice == "e"):
        choice = input(">")

    replay = ""
    while(replay == ""):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") 
        word_romaji = "[none]"
        word_fr = "[none]"
        
        if(choice == "A"):
            i = random.randint(0, len(all_jap) - 1)
            word_romaji = all_jap[i]
            word_fr = all_fr[i]
        elif(choice == "t"):
            i = random.randint(0, len(transports_jap) - 1)
            word_romaji = transports_jap[i]
            word_fr = transports_fr[i]
        elif(choice == "c"):
            i = random.randint(0, len(colors_jap) - 1)
            word_romaji = colors_jap[i]
            word_fr = colors_fr[i]
        elif(choice == "a"):
            i = random.randint(0, len(animals_jap) - 1)
            word_romaji = animals_jap[i]
            word_fr = animals_fr[i]
        elif(choice == "w"):
            i = random.randint(0, len(weather_jap) - 1)
            word_romaji = weather_jap[i]
            word_fr = weather_fr[i]
        elif(choice == "cl"):
            i = random.randint(0, len(clothes_jap) - 1)
            word_romaji = clothes_jap[i]
            word_fr = clothes_fr[i]
        elif(choice == "f"):
            i = random.randint(0, len(food_jap) - 1)
            word_romaji = food_jap[i]
            word_fr = food_fr[i]
        elif(choice == "vb"):
            i = random.randint(0, len(verbs_jap) - 1)
            word_romaji = verbs_jap[i]
            word_fr = verbs_fr[i]
        elif(choice == "adj"):
            i = random.randint(0, len(adjs_jap) - 1)
            word_romaji = adjs_jap[i]
            word_fr = adjs_fr[i]
        elif(choice == "cv"):
            i = random.randint(0, len(conjug_verbs_jap) - 1)
            word_romaji = conjug_verbs_jap[i]
            word_fr = conjug_verbs_fr[i]
        elif(choice == "ca"):
            i = random.randint(0, len(conjug_adjs_jap) - 1)
            word_romaji = conjug_adjs_jap[i]
            word_fr = conjug_adjs_fr[i]
        elif(choice == "e"):
            i = random.randint(0, len(expressions_jap) - 1)
            word_romaji = expressions_jap[i]
            word_fr = expressions_fr[i]
        else:
            print(word_romaji)
            print("Restarting...")
            function(mod)
        
        word_hiragana = romaji_to_hiragana(word_romaji)

        if(mod == "v"):
            if(choose == "fhr"):
                input(f"{word_fr}\n") 
                input(f"{word_hiragana}\n")
                input(f"{word_romaji}\n")

            elif(choose == "frh"):
                input(f"{word_fr}\n")
                input(f"{word_romaji}\n")
                input(f"{word_hiragana}\n")
            
            elif(choose == "rhf"):
                input(f"{word_romaji}\n")
                input(f"{word_hiragana}\n")
                input(f"{word_fr}\n")

            elif(choose == "hrf"):
                input(f"{word_hiragana}\n")
                input(f"{word_romaji}\n")
                input(f"{word_fr}\n")

            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") 
            replay = input("Again ? (Enter or n)\n>")
        
        if(mod == "g"):
            if(choose == "fr"):
                guess = str.lower(input(f""""STOP" to end the game\n\n\n\nIn romaji ?\n\n{word_fr}\n>"""))
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str.lower(word_romaji)):
                    input(f"""Oupsi. C'était "{word_romaji}"\n""")

            elif(choose == "rf"):
                guess = str.lower(input(f""""STOP" to end the game\n\n\n\nIn french ?\n\n{word_romaji}\n>"""))
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str.lower(word_fr)):
                    input(f"""Oupsi. C'était "{word_fr}"\n""")

            elif(choose == "hr"):
                guess = str.lower(input(f""""STOP" to end the game\n\n\n\nIn romaji ?\n\n{word_hiragana}\n>"""))
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str.lower(word_romaji)):
                    input(f"""Oupsi. C'était "{word_romaji}"\n""")

            elif(choose == "hf"):
                guess = str.lower(input(f""""STOP" to end the game\n\n\n\nIn french ?\n\n{word_hiragana}\n>"""))
                if(str.upper(guess) == "STOP"):
                    break
                if(not guess == str.lower(word_fr)):
                    input(f"""Oupsi. C'était "{word_fr}"\n""")
                
        

    restart = input("Restart ? (y/n)\n>")
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
