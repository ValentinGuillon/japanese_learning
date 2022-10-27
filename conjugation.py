#conjugation.py
import random
import module_romaji_to_kana
from module_list_jap_fr import * #class W(kana, jap, japAlt, fr, frAlt) => ex: W('h', "îe", ["iie"], "non", [])

#CONJUGAATION MAD TO IMPLEMENT
#!!! -ru verbs are always considered as 2nd group verb
#!!! add adjs/verbs exceptions 

def presentation():
    input("""
=============================
        This program
          conjugs
    verbs and adjectives
=============================
...""")
    input("Press Enter to proceed\nwhen nothing is asked.\n...")
    input("This symbol \">\",\nmeans an answer is expected.\n=============================\n""")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

#return the game mod chosen, before launch the actual function's program
def function_mod():  
    modList = ['g', 'v'] #g = game, v = view
    mod = ""

    print("""
====== Choose program mod ===
Guess mod (g) | View mod (v)
  You have    |   Guess in
  to write    |   your mind
  the word    |   No input
  to guess    |   require
 ---------------------------
     Conjugation mod (c)
     You give a verb/adj,
       how to conjug it,
     and show the result
=============================""")

    while(not mod in modList):
        mod = input(">")
    main(mod)

#print current category and languages
def printOptions(mod, category, lang):
    print("===================== Mod ===")
    if mod == "g":
        print(" Game")
    elif mod == "v":
        print(" View")
    
    print("================ Category ===")
    if (category == "cv"):
        print(" Conjugaison of Verbs")
    elif (category == "ca"):
        print(" Conjugaison of Adjectives")
    elif (category == "C"):
    	print(" Random")

    print("=============== Languages ===")
    for n in lang:
        if n == 'f':
            print(" French")
        if n == 'r':
            print(" Romaji")
        if n == 'h':
            print(" Hiragana")
        if n == 'k':
            print(" Katakana")
        if n == 'b' :
            print(" Random kana")
    print("=============================")

def isAnswerInAlt(answer, alt):
    if answer in alt:
        return 1

    return 0
    
formsAdj = {"négative": "nai",
            "passé": "tta",
            "ça à l'air": "sô",
            "négative passé": "katta",
            "négative ça à l'air": "nasasô"}
#exceptAdjs = {} #exemple {"adj1": 'i', "adj2": "na", "adj3", "na"}
def conjugAdj(adj, form): #form = ["négative", "passé", "ça à l'air", "négative passé", "négative ça à l'air", "adverbe"]
    conjug = ""
    group = ""
    termination = formsAdj[form]

    #determine the adj's category (en i, en na)
    #if (adj in exceptAdj):
    #    pass
    #elif
    if (adj[-1] == 'i'):
        group = 'i'
    else:
        group = "na"

    #conjug the adj, passed en category and form
    if (group == 'i'):
        if (form in ["négative", "négative passé", "négative ça à l'air"]):
            conjug = adj[:-1] + "ku" + termination
        elif (form == "passé"):
            conjug = adj[:-1] + "ka" + termination
        elif (form == "ça à l'air"):
            conjug = adj[:-1] + termination
        elif (form == "adverbe"):
            conjug = adj[:-1] + "ku"
    elif (group == "na"):
        if (form in ["négative", "négative passé", "négative ça à l'air"]):
            conjug = adj + "ja" + termination
        elif (form == "passé"):
            conjug = adj + "da" + termination
        elif (form == "ça à l'air"):
            conjug = adj + termination
        elif (form == "adverbe"):
            conjug = adj + "ni"

    return conjug


formsVerb = {"négative": "nai",
            "passé": "ta",
            "polie": "masu",
            "négative passé": "nakatta",
            "négative polie": "masen",
            "passé polie": "mashita",
            "négative passé polie": "masen deshita"}
#exceptVerbs = {} #exemple {"vb1": 2, "vb2": 2, "vb3", 1}
def conjugVerb(verb, form): #form = ["négative", "passé", "polie", "négative passé", "négative polie", "passé polie", "négative passé polie"]
    conjug = ""
    group = 0
    termination = formsVerb[form]
    #!!! passé vb1 gu bu mu nu = nda

    #determine the verbs's group (1, 2 or 3)
    #if (verb in exceptVerbs):
    #    pass
    #elif
    if (verb == "suru" or verb == "kuru"):
        group = 3

    elif (verb[-2:] == "ru"):
        group = 2

    else:
        group = 1 

    #conjug the adj, based on group and form
    if (group == 3):
        if (verb == "suru"):
            conjug = "shi" + termination
        elif (verb == "kuru"):
            conjug = "ki" + termination

    elif (group == 2):
        #-ru -> termination
        conjug = verb[:-2] + termination

    elif (group == 1):
        if (form == "polie" or form == "négative polie" or form == "passé polie" or form == "négative passé polie"):
            #-u -> -i + termination
            conjug = verb[:-1] + 'i' + termination

        elif (form == "négative"):
            if (verb[-3:-1] == "tsu"):
                #-tsu -> -ta + nai
                conjug = verb[:-3] + 'ta' + termination
            elif (not verb[-2] in ['r', 'g', 'b', 'm', 'n', 's', 'k']):
                #-u -> -wa + nai
                conjug = verb[:-1] + 'wa' + termination
            else:
                #-_u -> -_a + nai
                conjug = verb[:-1] + 'a' + termination

        elif (form == "passé"):
            if (verb[-3:-1] == "tsu"):
                #-tsu -> -t + ta
                conjug = verb[:-3] + 't' + termination
            elif (not verb[-2] in ['r', 'g', 'b', 'm', 'n', 's', 'k']):
                #-u -> -t + ta
                conjug = verb[:-1] + 't' + termination
            else:
                if (verb[-2] in ['r']):
                    #-ru -> -t + ta
                    conjug = verb[:-2] + 't' + termination
                if (verb[-2] in ['g']):
                    #-gu -> -ida
                    conjug = verb[:-2] + 'ida'
                if (verb[-2] in ['b', 'm', 'n']):
                    #-bu/-mu/-nu -> -nda
                    conjug = verb[:-2] + 'nda'
                if (verb[-2] in ['s']):
                    #-su -> -shi + ta
                    conjug = verb[:-2] + 'shi' + termination
                if (verb[-2] in ['k']):
                    #-ru -> -t + ta
                    conjug = verb[:-2] + 'i' + termination

        elif (form == "négative passé"):
            if (verb[-3:-1] == "tsu"):
                #-tsu -> -ta + nakatta
                conjug = verb[:-3] + 'ta' + termination
            elif (not verb[-2] in ['r', 'g', 'b', 'm', 'n', 's', 'k']):
                #-u -> -wa + nakatta
                conjug = verb[:-1] + 'wa' + termination
            else:
                #-_u -> -_a + nakatta
                conjug = verb[:-1] + 'a' + termination

    return conjug






def main(mod):
    #LANGUAGES CHOICE
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    lang = ""

    #ask languages for Game mod
    if(mod == "g"):
        langList = ["fr", "rf", "hf", "kf", "bf"] #f = french, r = romaji, h = hira, k = kata, b = hira/kata (randomly)

        print("""
======== Choose languages ===
French   <=> Romaji (fr / rf)
Hiragana  => French (hf)
Katakana  => French (kf)
Hira/Kata => French (bf)
=============================""")

        while(not lang in langList):
            lang = input(">")


    #ask languages for View mod
    if(mod == "v"):
        print("""
======== Choose languages ===
Can have multiple ones
(ex : fhr)\n
   (kana)         (alpha)
 Hiragana (h) | French (f)
 Katakana (k) | Romaji (r)
 Both (b)     |
=============================""")

        #input of languages choice
        while(not len(lang)):
            #user input (until input is allow)
            lang = input(">")

            langList = ['f', 'r', 'h', 'k', 'b'] #f = french, r = romaji, h = hira, k = kata, b = hira/kata (randomly)
            for letter in lang:
                #clear user input if one letter is not allow
                if not letter in langList:
                    lang = ""
                    break


    #characters CATEGORY CHOICE
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    category = ""

    print("""
========= Choose category ===
Conjug of verbs (cv)
Conjug of adjectives (ca)
Radom (C) (not implement yet)
=============================""")

    categList = ["cv", "ca"]
    while(not category in categList):
        category = input(">")


    correct = 0 
    wrong = 0
    streak = 0
    streakCurrent = 0
    stop = ""
    while(not stop == "STOP"):
        iWord = 0
        iForm = 0
        
        #a word is randomly choose, bases on the category
        if(category == "cv"):
            iWord = random.randint(0, len(verbs) - 1)
            iForm = random.randint(0, len(formsVerb) - 1)
            
        if(category == "ca"):
            iWord = random.randint(0, len(adjs) - 1)
            iForm = random.randint(0, len(formsAdj) - 1)

        if(category not in categList):
            input("Error...\nRestarting...")
            main(mod)
        
        
        word = W('', "", [], "", [])
        word_romaji = "[none]"
        word_fr = "[none]"
        form = '[none]'
        #origin = '' #= word.kana


        if(category == "cv"):
            word = verbs[iWord]
            form = list(formsVerb.keys())[iForm]  #list(formsVerb.keys())[i]
            word_romaji = word.jap
            word_fr = word.fr
            word_romajiConjuged = conjugVerb(word_romaji, form)
            i = 0
            for wordAlt in word.japAlt:
                wordAlt = conjugVerb(wordAlt, form)
                word.japAlt[i] = wordAlt
                i = i + 1
            
        if(category == "ca"):
            word = adjs[iWord]
            form = list(formsAdj.keys())[iForm]  #list(formsVerb.keys())[i]
            word_romaji = word.jap
            word_fr = word.fr
            word_romajiConjuged = conjugAdj(word_romaji, form)
            i = 0
            for wordAlt in word.japAlt:
                wordAlt = conjugAdj(wordAlt, form)
                word.japAlt[i] = wordAlt
                i = i + 1

            

        word_hira = module_romaji_to_kana.romaji_to_hira(word_romajiConjuged)
        word_kata = module_romaji_to_kana.romaji_to_kata(word_romajiConjuged)
        

        #VIEW MOD process
        if(mod == "v"):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            printOptions(mod, category, lang)
            print("Tap \"STOP\" to end\n\n")

            for n in lang:
                if(not stop == "STOP"):
                    if n == 'f':
                        stop = input(f"{word_fr} -> {form}\n")
                    if n == 'r':
                        stop = input(f"{word_romajiConjuged}\n")
                    if n == 'h':
                        stop = input(f"{word_hira}\n")
                    if n == 'k':
                        stop = input(f"{word_kata}\n")
                    if n == 'b' :
                        if (random.randint(0, 1)):
                            stop = input(f"{word_hira}\n")
                        else :
                            stop = input(f"{word_kata}\n")



        #GAME MOD process
        if(mod == "g"):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            printOptions(mod, category, lang)
            print(f"""================== Scores ===
 Correct:{correct}
 Wrong:{wrong}
 Best streak:{streak}
 Streak:{streakCurrent}
=============================
Tap "STOP" to end\n\n""")


            #random choice of kana
            saveLang = lang
            if lang[0] == 'b':
                if (random.randint(0, 1)):
                    lang = 'h' + lang[1]
                else:
                    lang = 'k' + lang[1]

            wordIsGood = 0
            formIsGood = 0

            if(lang == "fr"):
                #user guess
                guess = str.lower(input(f" {word_fr} -> {form}\n\nIn romaji ?\n>"))

                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess
                if(guess == str.lower(word_romajiConjuged) or isAnswerInAlt(guess, word.japAlt)):
                    correct += 1
                    streakCurrent += 1
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_romajiConjuged}\"")
                    wrong += 1
                    if(streakCurrent > streak):
                        streak = streakCurrent
                    streakCurrent = 0

                    if(len(word.japAlt)):
                        if(input("Wanna see alternative ? (y/Enter)>") == 'y'):
                            for n in word.japAlt:
                                print(f" {n}")
                            input()
                    else:
                        input()

            elif(lang == "rf"):
                #user guess for the word
                guess = str.lower(input(f" {word_romajiConjuged}\n\nIn french ? (just the word)\n>"))

                #verification word
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess word
                elif(guess == str.lower(word_fr) or isAnswerInAlt(guess, word.frAlt)):
                    wordIsGood = 1
                
                #user guess for the form
                guess = str.lower(input(f"In french ? (just the form)\n>"))
                
                #verification form
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess form
                elif(guess == str.lower(form) or guess == str.lower(removeAccents(form))):
                    formIsGood = 1
                    
                #good word AND form
                if (wordIsGood and formIsGood):
                    correct += 1
                    streakCurrent += 1
                
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_fr}\" -> {form}")
                    wrong += 1
                    if(streakCurrent > streak):
                        streak = streakCurrent
                    streakCurrent = 0

                    if(len(word.frAlt)):
                        if(input("Wanna see alternative ? (y/Enter)>") == 'y'):
                            for n in word.frAlt:
                                print(f" {n}")
                            input()
                    else:
                        input()
            #A FAIRE
            elif(lang == "hf"):
                #user guess for the word
                guess = str.lower(input(f" {word_hira}\n\nIn french ? (just the word)\n>"))

                #verification word
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess word
                elif(guess == str.lower(word_fr) or isAnswerInAlt(guess, word.frAlt)):
                    wordIsGood = 1
                
                #user guess for the form
                guess = str.lower(input(f"In french ? (just the form)\n>"))
                
                #verification form
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess form
                elif(guess == str.lower(form) or guess == str.lower(removeAccents(form))):
                    formIsGood = 1
                    
                #good word AND form
                if (wordIsGood and formIsGood):
                    correct += 1
                    streakCurrent += 1
                
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_fr}\" -> {form}")
                    wrong += 1
                    if(streakCurrent > streak):
                        streak = streakCurrent
                    streakCurrent = 0

                    if(len(word.frAlt)):
                        if(input("Wanna see alternative ? (y/Enter)>") == 'y'):
                            for n in word.frAlt:
                                print(f" {n}")
                            input()
                    else:
                        input()
            #A FAIRE
            elif(lang == "kf"):
                #user guess for the word
                guess = str.lower(input(f" {word_kata}\n\nIn french ? (just the word)\n>"))

                #verification word
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess word
                elif(guess == str.lower(word_fr) or isAnswerInAlt(guess, word.frAlt)):
                    wordIsGood = 1
                
                #user guess for the form
                guess = str.lower(input(f"In french ? (just the form)\n>"))
                
                #verification form
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess form
                elif(guess == str.lower(form) or guess == str.lower(removeAccents(form))):
                    formIsGood = 1
                    
                #good word AND form
                if (wordIsGood and formIsGood):
                    correct += 1
                    streakCurrent += 1
                
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_fr}\" -> {form}")
                    wrong += 1
                    if(streakCurrent > streak):
                        streak = streakCurrent
                    streakCurrent = 0

                    if(len(word.frAlt)):
                        if(input("Wanna see alternative ? (y/Enter)>") == 'y'):
                            for n in word.frAlt:
                                print(f" {n}")
                            input()
                    else:
                        input()
            
            #reset language
            lang = saveLang
                




    restart = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRestart and change mod ? (y/n)\n>")
    while(restart == "" or not restart == "n"):
        if(restart == "y"):
            function_mod()
            break
        restart = input(">")
    
    


if __name__ == "__main__":
    presentation()    
    function_mod()
