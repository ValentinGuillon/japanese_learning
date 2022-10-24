#conjugation.py
import random
import module_romaji_to_kana
from module_list_jap_fr import * #class W(kana, jap, japAlt, fr, frAlt) => ex: W('h', "îe", ["iie"], "non", [])

#CONJUGAATION MAD TO IMPLEMENT
#!!! -ru verbs are always considered as 2nd group verb

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
    if(category == "cv"):
        print(" Conjugaison of Verbs")
    elif(category == "ca"):
        print(" Conjugaison of Adjectives")

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
    

def conjugAdf(word, form):
    pass
    #determine the adj's category (en i, en na)
    #conjug the adj, passed en category and form

"""
ADJ
(adj en i)
(adj en na)

forme négative
forme passé
forme négative passé
forme \"ça a l'air\"
forme négative de \"ça a l'air\"
transformation en adverbe
"""


forms = {"négative": "nai",
            "passé": "ta",
            "polie": "masu",
            "négative passé": "nakatta",
            "négative polie": "masen",
            "passé polie": "mashita",
            "négative passé polie": "masen deshita"}
def conjugVerbs(verb, form):
    conjug = ""
    group = 0
    termination = forms[form]
    #!!! passé vb1 gu bu mu nu = nda

    #determine the verbs's group (1, 2 or 3)
    if (verb == "suru" or verb == "kuru"):
        group = 3

    elif (verb[-2:] == "ru"):
        group = 2

    else:
        group = 1 

    #conjug the adj, passed en group and form
    """
    forme négative
    forme passé
    forme polie
    forme négative passé
    forme négative polie
    forme passé polie
    forme négative passé polie
    """ 

    if (group == 3):
        if (verb == "suru"):
            conjug = "shi" + termination
        elif (verb == "kuru"):
            conjug = "ki" + termination

    elif (group == 2):
        conjug = verb[:-2] + termination

    elif (group == 1):
        if (form == "polie" or form == "négative polie" or form == "passé polie" or form == "négative passé polie"):
            conjug = verb[:-1] + 'i' + termination

        elif (form == "négative"):
            if (verb[-3:-1] == "tsu"):
                conjug = verb[:-3] + 'ta' + termination
            elif (not verb[-2] in ['r', 'g', 'b', 'm', 'n', 's', 'k']):
                conjug = verb[:-1] + 'wa' + termination
            else:
                conjug = verb[:-1] + 'a' + termination

        elif (form == "passé"):
            if (verb[-3:-1] == "tsu"):
                conjug = verb[:-3] + 't' + termination
            elif (not verb[-2] in ['r', 'g', 'b', 'm', 'n', 's', 'k']):
                conjug = verb[:-1] + 't' + termination
            else:
                if (verb[-2] in ['r']):
                    conjug = verb[:-2] + 't' + termination
                if (verb[-2] in ['g']):
                    conjug = verb[:-2] + 'ida'
                if (verb[-2] in ['b', 'm', 'n']):
                    conjug = verb[:-2] + 'nda'
                if (verb[-2] in ['s']):
                    conjug = verb[:-2] + 'shi' + termination
                if (verb[-2] in ['k']):
                    conjug = verb[:-2] + 'i' + termination

        elif (form == "négative passé"):
            if (verb[-3:-1] == "tsu"):
                conjug = verb[:-3] + 'ta' + termination
            elif (not verb[-2] in ['r', 'g', 'b', 'm', 'n', 's', 'k']):
                conjug = verb[:-1] + 'wa' + termination
            else:
                conjug = verb[:-1] + 'a' + termination



    return conjug


"""
wanai    négative vb 1 -u
anai     négative vb 1 -_u
tanai    négative vb 1 -tsu

tta      passé vb 1 -u
tta      passé vb 1 -ru
tta      passé vb 1 -tsu
ida      passé vb 1 -gu
nda      passé vb 1 -bu
nda      passé vb 1 -mu
nda      passé vb 1 -nu
shita    passé vb 1 -su
ita      passé vb 1 -ku

imasu    polie vb 1

wanakatta    négative passé vb 1 -u
anakatta     négative passé vb 1 -_u
tanakatta    négative passé vb 1 -tsu

imasen            négative polie vb 1
imashita          passé polie vb 1
imasen deshita    négative passé polie vb 1


nai              négative vb 2
ta               passé vb 2
masu             polie vb 2
nakatta          négative passé vb 2
masen            négative polie vb 2
mashita          passé polie vb 2
masen deshita    négative passé polie vb 2


shinai, kinai                        négative vb 3
shita, kita                          passé vb 3
shimasu, kimasu                      polie vb 3,
shinakatta, kinakatta                négative passé vb 3
shimasen, kimasen                    négative polie vb 3
shimashita, kimashita                passé polie vb 3
shimasen deshita, kimasen deshita    négative passé polie vb 3

"""




"""
VERB
(vb 1er g)
(vb 1er g) -u
(vb 1er g) -ru
(vb 1er g) -tsu
(vb 1er g) -gu
(vb 1er g) -bu
(vb 1er g) -mu
(vb 1er g) -nu
(vb 1er g) -su
(vb 1er g) -ku
(vb 1er g) -u
(vb 1er g) -_u
(vb 1er g) -tsu
(vb 1er g) -u
(vb 1er g) -_u
(vb 1er g) -tsu
(vb 2e g)
(vb 3e g)

forme négative
forme passé
forme polie
forme négative passé
forme négative polie
forme passé polie
forme négative passé polie
"""






def main(mod):
    #LANGUAGES CHOICE
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    lang = ""

    #ask languages for Game mod
    if(mod == "g"):
        langList = ["fr", "rf", "hr", "hf", "kr", "kf", "bf", "br"] #f = french, r = romaji, h = hira, k = kata, b = hira/kata (randomly)

        print("""
======== Choose languages ===
French   <=> Romaji (fr / rf)
Hiragana  => Romaji (hr)
Hiragana  => French (hf)
Katakana  => Romaji (kr)
Katakana  => French (kf)
Hira/Kata => Romaji (br)
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
        iIndex = 0
        borneMin = 0
        borneMax = len(all) -1
        
        #a word is randomly choose, bases on the category
        if(category == "cv"):
            iIndex = random.randint(0, len(conjug_verbs) - 1)
        if(category == "ca"):
            iIndex = random.randint(0, len(conjug_adjs) - 1)

        if(category not in categList):
            input("Error...\nRestarting...")
            main(mod)
        
        word = W('', "", [], "", [])
        word_romaji = "[none]"
        word_fr = "[none]"
        #origin = '' #= word.kana

        if(category == "cv"):
            word = conjug_verbs[iIndex]
            word_romaji = word.jap
            word_fr = word.fr
        if(category == "ca"):
            word = conjug_adjs[iIndex]
            word_romaji = word.jap
            word_fr = word.fr


        word_hira = module_romaji_to_kana.romaji_to_hira(word_romaji)
        word_kata = module_romaji_to_kana.romaji_to_kata(word_romaji)


        #VIEW MOD process
        if(mod == "v"):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            printOptions(mod, category, lang)
            print("Tap \"STOP\" to end\n\n")

            for n in lang:
                if(not stop == "STOP"):
                    if n == 'f':
                        stop = input(f"{word_fr}\n")
                    if n == 'r':
                        stop = input(f"{word_romaji}\n")
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


            if(lang == "fr"):
                #user guess
                guess = str.lower(input(f"In romaji ?\n\n {word_fr}\n>"))

                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess
                if(guess == str.lower(word_romaji) or isAnswerInAlt(guess, word.japAlt)):
                    correct += 1
                    streakCurrent += 1
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_romaji}\"")
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
                #user guess
                guess = str.lower(input(f"In french ?\n\n {word_romaji}\n>"))

                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess
                elif(guess == str.lower(word_fr) or isAnswerInAlt(guess, word.frAlt)):
                    correct += 1
                    streakCurrent += 1
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_fr}\"")
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

            elif(lang == "hr"):
                #user guess
                guess = str.lower(input(f"In romaji ?\n\n {word_hira}\n>"))

                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess
                if(guess == str.lower(word_romaji) or isAnswerInAlt(guess, word.japAlt)):
                    correct += 1
                    streakCurrent += 1
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_romaji}\"")
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

            elif(lang == "hf"):
                #user guess
                guess = str.lower(input(f"In french ?\n\n {word_hira}\n>"))

                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess
                if(guess == str.lower(word_fr) or isAnswerInAlt(guess, word.frAlt)):
                    correct += 1
                    streakCurrent += 1
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_fr}\"")
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

            elif(lang == "kr"):
                #user guess
                guess = str.lower(input(f"In romaji ?\n\n {word_kata}\n>"))

                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess
                if(guess == str.lower(word_romaji) or isAnswerInAlt(guess, word.japAlt)):
                    correct += 1
                    streakCurrent += 1
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_romaji}\"")
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

            elif(lang == "kf"):
                #user guess
                guess = str.lower(input(f"In french ?\n\n {word_kata}\n>"))
                                #verification
                #force stopping prog
                if(str.upper(guess) == "STOP"):
                    break
                #good guess
                if(guess == str.lower(word_fr) or isAnswerInAlt(guess, word.frAlt)):
                    correct += 1
                    streakCurrent += 1
                #wrong guess
                else:
                    print(f"Oupsi. C'était \"{word_fr}\"")
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
