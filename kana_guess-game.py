#kana_guess-game.py
from module_characters_jap import *
import random


def presentation():
    input("""
=============================
        This program
     is a guessing game
         with score.
  Gives you multiples kana.
          You have
   to write them in romaji.
=============================
Press Enter to proceed
when nothing is asked.
...
""")
    input("""Restart the game
or exit the program,
will reset the high score.
...
""")
    input("""This symbol ">",
means an answer is expected.
=============================
""")

def function(combi_added, combiplus_added):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    lang = input("Which kana ?\n Hiragana (h)\n Katakana (k)\n Both (b)\n>")
    while(not lang == "h" and not lang == "k" and not lang == "b"):
        lang = input(">")
    
    if(combi_added == 0):
        if(input("Add combi kana ? (y/n)\n>") == 'y'):
            combi_added = 1
            for n in char['romaji']['sp']:
                char['romaji']['all'].append(n)
            for n in char['hira']['sp']:
                char['hira']['all'].append(n)
            for n in char['kata']['sp']:
                char['kata']['all'].append(n)
    if(combiplus_added == 0):
        if(input("Add combi+ kana ? (y/n)\n>") == 'y'):
            combiplus_added = 1
            for n in char['romaji']['sp+']:
                char['romaji']['all'].append(n)
            for n in char['hira']['sp+']:
                char['hira']['all'].append(n)
            for n in char['kata']['sp+']:
                char['kata']['all'].append(n)

    number = int(input("How much ?\n>"))


    correct = 0
    wrong = 0
    streak = 0
    current_streak = 0

    vrai = "true"
    while(vrai == "true"):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f""""STOP" to end\n===============
    Correct:{correct}\n      Wrong:{wrong}\nBest streak:{streak}\n     Streak:{current_streak}\n===============\n\n\n\n""")
        kana = ""
        romaji = ""
        x = number
        rand_lang = lang

        if(lang == 'b'):
            if(random.randint(0, 1) == 0):
                rand_lang = 'h'
            else:
                rand_lang = 'k'

        while(not x == 0):
            if (rand_lang == 'h'):
                i = random.randint(0, len(char['hira']['all']) -1)
                kana += char['hira']['all'][i]
            elif (rand_lang == 'k'):
                i = random.randint(0, len(char['kata']['all']) -1)
                kana += char['kata']['all'][i]

            romaji += char['romaji']['all'][i]
            x -= 1
            
        
        print(f" {kana}")
        user_answer = input(">")
        if(user_answer == romaji):
            correct += 1
            current_streak += 1
        elif(user_answer == "STOP"):
           break
        else:
            input(f"""Oupsi, it was "{romaji}"\n""")
            wrong += 1
            if(current_streak > streak):
                streak = current_streak
            current_streak = 0

    restart = input(" Restart ? (y/n)\n>")
    while(restart == "" or not restart == "n"):
        if(restart == "y"):
            function(combi_added, combiplus_added)
            break
        restart = input(">")




    
def main():
    presentation()
    function(0, 0)

if __name__=="__main__":
    main()
