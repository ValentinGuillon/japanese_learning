#kana_guess-game.py
import random
from module_characters_jap import *
import module_saves as saves


global TOTAL_STREAKS
global GREATER_STREAK
global AVERAGE_STREAK
global TOTAL_CORRECT
TOTAL_STREAKS = 0
GREATER_STREAK = 0
AVERAGE_STREAK = 0
TOTAL_CORRECT = 0

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
...""")
    input("Press Enter to proceed\nwhen nothing is asked.\n...")
    input("This symbol \">\",\nmeans an answer is expected.\n=============================\n""")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

#print current category and languages
def printOptions(lang):
    print("=============== Languages ===")
    for n in lang:
        if n == 'h':
            print(" Hiragana")
        if n == 'k':
            print(" Katakana")
        if n == 'b' :
            print(" Random kana")
    print("=============================")


def update_average() -> None:
    global AVERAGE_STREAK
    if TOTAL_STREAKS > 0:
        AVERAGE_STREAK = TOTAL_CORRECT // TOTAL_STREAKS

def save_streak() -> None:
    update_average()
    saves.save_streak_infos(TOTAL_STREAKS, GREATER_STREAK, AVERAGE_STREAK, TOTAL_CORRECT)





def main(combiAdded, combiplusAdded):
    global TOTAL_STREAKS
    global GREATER_STREAK
    global AVERAGE_STREAK
    global TOTAL_CORRECT

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    langList = ['h', 'k', 'b']
    lang = ""

    print("============= Choose kana ===\n Hiragana (h)\n Katakana (k)\n Both (b)\n=============================")
    while(not lang in langList):
        lang = input(">")
    
    
    if(combiAdded == 0):
        if(input("    Add combi kana ? (y/n)\n>") == 'y'):
            combiAdded = 1
            for n in char['sp']:
                char['all'].append(n)
    if(combiplusAdded == 0):
        if(input("    Add combi+ kana ? (y/n)\n>") == 'y'):
            combiAdded = 1
            combiplusAdded = 1
            for n in char['sp']:
                char['all'].append(n)
            for n in char['sp+']:
                char['all'].append(n)

    number = int(input("    How much ?\n>"))



    correct = 0
    wrong = 0
    streakCurrent = 0


    while(1):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        printOptions(lang)
        print(f"""================== Scores ===
 Correct:{correct}
 Wrong:{wrong}
 Best streak:{GREATER_STREAK}
 Average streak:{AVERAGE_STREAK}
 Streak:{streakCurrent}
=============================
Tap "STOP" to end
\n\n""")

        kana = ""
        romaji = ""
        x = number #number of kana to print
        saveLang = lang

        if(lang == 'b'):
            if(random.randint(0, 1)):
                lang = 'h'
            else:
                lang = 'k'

        while(x):
            i = random.randint(0, len(char['all']) -1)
            if(char['all'][i].roma != ""):
                romaji += char['all'][i].roma

                if (lang == 'h'):
                    kana += char['all'][i].hira
                elif (lang == 'k'):
                    kana += char['all'][i].kata
                    
                x -= 1
        

            
        
        print(f" {kana}")
        #user input
        userAnswer = input(">")

        #good guess
        if(userAnswer == romaji):
            correct += 1
            streakCurrent += 1

        #force stop prog
        elif(userAnswer == "STOP"):
           break
        
        #bad guess
        else:
            input(f"""Oupsi, it was "{romaji}"\n""")
            wrong += 1
            if(streakCurrent > GREATER_STREAK):
                GREATER_STREAK = streakCurrent

            TOTAL_STREAKS += 1
            TOTAL_CORRECT += streakCurrent
            save_streak()
            streakCurrent = 0
        
        #reset language
        lang = saveLang

    restart = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRestart ? (y/n)\n>")
    while(restart == "" or not restart == "n"):
        if(restart == "y"):
            main(combiAdded, combiplusAdded)
            break
        restart = input(">")


if __name__=="__main__":
    presentation()
    TOTAL_STREAKS, GREATER_STREAK, AVERAGE_STREAK, TOTAL_CORRECT = saves.load_streak_infos()
    main(0, 0)
