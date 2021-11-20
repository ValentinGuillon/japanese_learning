#guess_char_game.py
from module_characters_jap import *
import random

def function():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    combo = 0
    max = 0
    number = int(input("How many characters ?\n>"))

    vrai = "true"
    while(vrai == "true"):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"""
"STOP" to end the game
=======================
Record : {max}
Score : {combo}
=======================\n\n\n\n\n""")
        hiragana = ""
        romaji = ""
        romaji_2 = ""
        x = number

        while(not x == 0):
            i = random.randint(0, len(char['hiragana']['all']) -1)
            hiragana += char['hiragana']['all'][i]
            romaji += char['romaji']['all'][i]
            romaji_2 += char['romaji']['all'][i] + " "
            x -= 1
            
        
        print(f"{hiragana}")
        reponse = input(">")
        if(reponse == romaji):
            print("c'est bon connard")
            combo += 1
        elif(reponse == "STOP"):
           break
        else:
            input(f"""Oupsi, c'était "{romaji}"\n""")
            if(max < combo):
                max = combo
            combo = 0

    print(f"{max} à la suite\n")

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
