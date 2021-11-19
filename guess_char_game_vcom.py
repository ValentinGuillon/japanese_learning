from module_characters_jap_vcom import *
import random

def function():
    combo = 0
    max = 0

    vrai = "true"
    while(vrai == "true"):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"""
"STOP" to end the game
=======================
Record : {max}
Score : {combo}
=======================\n\n\n\n\n""")
        x = 4
        hiragana = ""
        romaji = ""
        romaji_2 = ""

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
            input(f'Oupsi, c\'était "{romaji}"\n')
            if(max < combo):
                max = combo
            combo = 0

    print(f"{max} à la suite")

    restart = ""
    while(restart == ""):
        restart = input("Restart ? (y/n)\n>")
        if(restart == "y"):
           function()




    
def main():
    input("""
=================================================
   This program is a guessing game with score.
            Gives you multiples kanas.
         You have to write them in romaji.
=================================================
...
""")
    input("""
This symbol ">", means you have to write.
If there is no symbol, press Enter to proceed.
Restart the game or exit the program,
will reset the high score.
""")
    function()

if __name__=="__main__":
    main()
