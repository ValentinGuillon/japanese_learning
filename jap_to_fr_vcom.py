from module_list_jap_fr_vcom import *
import random

def function():
    choose = input("jap or fr ? (j/f)\n>")
    choice = input("""
Choose the category :
    
All (except last 3) (Enter)

Transports (t) | Colors (c)
Animals (a)    | Weather (w)
Clothes (cl)   | Food (f)

Verbs (vb) | Adjectifs (adj)

Conjug of verbs (cv)
Conjug of adjectifs (ca)
Expressions (e)
>""")

    replay = ""
    while(replay == ""):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") 
        word_jap = "[none]"
        word_fr = "[none]"
        
        if(choice == ""):
            i = random.randint(0, len(all_jap) - 1)
            word_jap = all_jap[i]
            word_fr = all_fr[i]
        elif(choice == "t"):
            i = random.randint(0, len(transports_jap) - 1)
            word_jap = transports_jap[i]
            word_fr = transports_fr[i]
        elif(choice == "c"):
            i = random.randint(0, len(colors_jap) - 1)
            word_jap = colors_jap[i]
            word_fr = colors_fr[i]
        elif(choice == "a"):
            i = random.randint(0, len(animals_jap) - 1)
            word_jap = animals_jap[i]
            word_fr = animals_fr[i]
        elif(choice == "w"):
            i = random.randint(0, len(weather_jap) - 1)
            word_jap = weather_jap[i]
            word_fr = weather_fr[i]
        elif(choice == "cl"):
            i = random.randint(0, len(clothes_jap) - 1)
            word_jap = clothes_jap[i]
            word_fr = clothes_fr[i]
        elif(choice == "f"):
            i = random.randint(0, len(food_jap) - 1)
            word_jap = food_jap[i]
            word_fr = food_fr[i]
        elif(choice == "vb"):
            i = random.randint(0, len(verbs_jap) - 1)
            word_jap = verbs_jap[i]
            word_fr = verbs_fr[i]
        elif(choice == "adj"):
            i = random.randint(0, len(adjs_jap) - 1)
            word_jap = adjs_jap[i]
            word_fr = adjs_fr[i]
        elif(choice == "cv"):
            i = random.randint(0, len(conjug_verbs_jap) - 1)
            word_jap = conjug_verbs_jap[i]
            word_fr = conjug_verbs_fr[i]
        elif(choice == "ca"):
            i = random.randint(0, len(conjug_adjs_jap) - 1)
            word_jap = conjug_adjs_jap[i]
            word_fr = conjug_adjs_fr[i]
        elif(choice == "e"):
            i = random.randint(0, len(expressions_jap) - 1)
            word_jap = expressions_jap[i]
            word_fr = expressions_fr[i]
        else:
            print(word_jap)
            print("Restarting...")
            function()
        
        from romaji_to_kana_vcom import romaji_to_hiragana
        word_hiragana = romaji_to_hiragana(word_jap)

        if(choose == "j"):
            input(f"{word_hiragana}\n")
            input(f"{word_jap}\n")
            input(f"{word_fr}\n") 

        elif(choose == "f"):
            input(f"{word_fr}\n")
            input(f"{word_hiragana}\n")
            input(f"{word_jap}\n") 
        
        replay = input("Again ? (Enter or n)\n>")

    restart = ""
    while(restart == ""):
        restart = input("Restart ? (y/n)\n>")
        if(restart == "y"):
            function() 
    
    
    


def main():
    input("""
    	
=============================
        This program
          give you
           a word
            then
         translate
=============================
When there is no choices
press Enter
""")
    
    function()

if __name__ == "__main__":
    main() 