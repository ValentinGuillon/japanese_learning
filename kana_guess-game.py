#kana_guess-game.py
import random
from module_characters_jap import *


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





def main(combiAdded, combiplusAdded):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    lang = input("Which kana ?\n Hiragana (h)\n Katakana (k)\n Both (b)\n>")
    while(not lang == "h" and not lang == "k" and not lang == "b"):
        lang = input(">")
    
    if(combiAdded == 0):
        if(input("Add combi kana ? (y/n)\n>") == 'y'):
            combiAdded = 1
            for n in char['sp']:
                char['all'].append(n)
    if(combiplusAdded == 0):
        if(input("Add combi+ kana ? (y/n)\n>") == 'y'):
            combiAdded = 1
            combiplusAdded = 1
            for n in char['sp']:
                char['all'].append(n)
            for n in char['sp+']:
                char['all'].append(n)

    number = int(input("How much ?\n>"))


    """
    for n in char['sp']:
        char['all'].append(n)
    for n in char['sp+']:
        char['all'].append(n)
    """

    correct = 0
    wrong = 0
    streak = 0
    streakCurrent = 0

    vrai = "true"
    while(vrai == "true"):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f""""STOP" to end\n=============================
    Correct:{correct}\n      Wrong:{wrong}\nBest streak:{streak}\n     Streak:{streakCurrent}\n=============================\n\n\n\n""")
        kana = ""
        romaji = ""
        x = number
        randLang = lang

        if(lang == 'b'):
            if(random.randint(0, 1) == 0):
                randLang = 'h'
            else:
                randLang = 'k'

        while(not x == 0):
            i = random.randint(0, len(char['all']) -1)
            if(char['all'][i].roma != ""):
                romaji += char['all'][i].roma

                if (randLang == 'h'):
                    kana += char['all'][i].hira
                elif (randLang == 'k'):
                    kana += char['all'][i].kata
                    
                x -= 1

            
        
        print(f" {kana}")
        userAnswer = input(">")
        if(userAnswer == romaji):
            correct += 1
            streakCurrent += 1
        elif(userAnswer == "STOP"):
           break
        else:
            input(f"""Oupsi, it was "{romaji}"\n""")
            wrong += 1
            if(streakCurrent > streak):
                streak = streakCurrent
            streakCurrent = 0

    restart = input(" Restart ? (y/n)\n>")
    while(restart == "" or not restart == "n"):
        if(restart == "y"):
            main(combiAdded, combiplusAdded)
            break
        restart = input(">")


if __name__=="__main__":
    presentation()
    main(0, 0)
