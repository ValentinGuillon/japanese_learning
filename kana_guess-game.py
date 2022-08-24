#guess_char_game.py
from module_characters_jap import *
import random

def function():
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    lang = input("Hiragana (h)\nKatagana (k)\nBoth (g)\n>")
    while(not lang == "h" and not lang == "k" and not lang == "g"):
        lang = input(">")
    
    correct = 0
    wrong = 0
    streak = 0
    current_streak = 0
    number = int(input("How many characters ?\n>"))

    vrai = "true"
    while(vrai == "true"):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f""""STOP" to end the game\n===============
Correct:{correct}\nWrong:{wrong}\nBest streak:{streak}\nStreak:{current_streak}\n===============\n\n\n\n""")
        kana = ""
        romaji = ""
        romaji_2 = ""
        x = number

        while(not x == 0):
            if (lang == "h"):
                i = random.randint(0, len(char['hiragana']['all']) -1)
                kana += char['hiragana']['all'][i]
            elif (lang == "k"):
                i = random.randint(0, len(char['katagana']['all']) -1)
                kana += char['katagana']['all'][i]
            elif (lang == "g"):
                if(random.randint(0, 1)):
                    i = random.randint(0, len(char['hiragana']['all']) -1)
                    kana += char['hiragana']['all'][i]
                else:
                    i = random.randint(0, len(char['katagana']['all']) -1)
                    kana += char['katagana']['all'][i]

            romaji += char['romaji']['all'][i]
            romaji_2 += char['romaji']['all'][i] + " "
            x -= 1
            
        
        print(f"{kana}")
        reponse = input(">")
        if(reponse == romaji):
            correct += 1
            current_streak += 1
        elif(reponse == "STOP"):
           break
        else:
            input(f"""Oupsi, c'était "{romaji}"\n""")
            wrong += 1
            if(current_streak > streak):
                streak = current_streak
            current_streak = 0

    restart = input("Restart ? (y/n)\n>")
    while(restart == "" or not restart == "n"):
        if(restart == "y"):
            function()
            break
        restart = input(">")




    
def main():
    input("""
=============================
        This program
     is a guessing game
         with score.
  Gives you multiples kanas.
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
    function()

if __name__=="__main__":
    main()
