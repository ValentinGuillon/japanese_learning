from module_characters_jap_vcom import *
import string

def function():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    text = input("Write your sentence/word\n(romaji only)\n>")
    to_hiragana = romaji_to_hiragana(text)
    input("traducting...")
    input(f"{to_hiragana}\n")
    
    restart = ""
    while(restart == ""):
        restart = input("New sentence/word ? (y/n)\n>")
        if(restart == "y"):
            function()
    


def romaji_to_hiragana(text):
    text = text.lower()
    all = string.ascii_lowercase
    vowels = "a" + "e" + "i" + "o" + "u"
    vowels_circumflex = "â" + "ê" + "î" + "ô" + "û"
    consonnes = "b" + "c" + "d" + "f" + "g" + "h" + "j" + "k" + "l" + "m" + "n" + "p" + "q" + "r" + "s" + "t" + "v" + "w" + "x" + "y" + "z"

    to_hiragana = ""
    c = "" 
    text = " " + text #c'est pour les cas où la première lettre et la dernière sont deux mêmes consonnes. Parceque dans la suite, le prog fait des vérif' sur le i-1, et si c'est la première lettre, ça va regarder la dernière lettre.
    i = 0
    for x in text:
        j = 0
        #if is "n"
        if(x == "n"): 
            #if is "n" on the last character
            if(len(text[i:]) == 1):
                j = 0
                for y in char['romaji']['all']:
                    if(y == x):
                        c = char['hiragana']['all'][j]
                        break
                    j += 1
                    
                to_hiragana += c
                #print(c)
            
            #if is "n + not vowel"
            elif(not text[i+1] in vowels and not text[i+1] in vowels_circumflex):
                j = 0
                for y in char['romaji']['all']:
                    if(y == x):
                        c = char['hiragana']['all'][j]
                        break
                    j += 1
                    
                to_hiragana += c
                #print(c)

        #if is "vowel_circumflex"
        elif(x in vowels_circumflex): 
            if(x == "â"):
                x = "a"
            elif(x == "ê"):
                x = "e"
            elif(x == "î"):
                x = "i"
            elif(x == "ô"):
                x = "o"
            elif(x == "û"):
                x = "u"

            #if is "vowel_circumflex" solo
            if(not text[i-1] in consonnes):
                j = 0
                for y in char['romaji']['all']:
                    if(y == x):
                        c = char['hiragana']['all'][j]
                        break
                    j += 1
                to_hiragana += c
                #print(c)
            
            #if is "cons + vowel_circumflex"
            elif(text[i-1] in consonnes):
                #if is "cons + cons + vowel_circumflex" and consonnes are same
                if(text[i-2] == text[i-1]):
                    c = text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    to_hiragana += small_tsu + c
                    #print(c)

                #if is "cons1 + cons2 + vowel_circumflex" and cons1 is not "n"
                elif(text[i-2] in consonnes and not text[i-2] == "n"):
                    c = text[i-2] + text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    to_hiragana += c
                    #print(c)

                else:
                    c = text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    to_hiragana += c
                    #print(c)

            j = 0
            for y in char['romaji']['all']:
                if(y == x):
                    c = char['hiragana']['all'][j]
                    break
                j += 1
            to_hiragana += c


        #if is "vowel"
        elif(x in vowels): 
            #if is not "cons + vowel"
            if(not text[i-1] in consonnes):
                j = 0
                for y in char['romaji']['all']:
                    if(y == x):
                        c = char['hiragana']['all'][j]
                        break
                    j += 1
                to_hiragana += c
                #print(c)

            #if is "cons + vowel"    
            elif(text[i-1] in consonnes):
                #if is "cons + cons + vowel" and consonnes are same
                if(text[i-2] in consonnes and text[i-2] == text[i-1]): 
                    c = text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    
                    to_hiragana += small_tsu + c
                    #print(c)

                #if is "cons + cons + vowel" and cons1 is not "n"
                elif(text[i-2] in consonnes and not text[i-2] == "n"): 
                    c = text[i-2] + text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    
                    to_hiragana += c
                    #print(c)
                else:
                    c = text[i-1] + x
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    to_hiragana += c
                    #print(c)

        #if is space or not a letter (!&@...)            
        elif(not x in all): 
            to_hiragana += x
            #print(x)
        i += 1
    
    to_hiragana = to_hiragana[1:] #et mtn on enlève l'espace du début
    return(to_hiragana)





def main() :
    input("""
    	
=============================
        This program
          traduct
      a sentence from
          romaji
            to
           kana
=============================
Press Enter to proceed when nothing is asked.
...
""")
    input("""This symbol ">", means a answer is expected.
=============================
""")
    function()
    
if __name__ == "__main__":
    main() 
