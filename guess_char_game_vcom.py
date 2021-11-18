from module_characters_jap_vcom import *
import random

def function():
    combo = 0
    max = 0

    vrai = "true"
    while(vrai == "true"):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"""
===================
Record : {max}
Score : {combo}
===================\n\n\n\n\n""")
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
            input(f'non connard, c\'est "{romaji}"')
            if(max < combo):
                max = combo
            combo = 0

    print(f"{max} à la suite. gg")


    again = input("again")
    if(again == "y"):
           function()




    
def main():
    function()

if __name__=="__main__":
    main()
