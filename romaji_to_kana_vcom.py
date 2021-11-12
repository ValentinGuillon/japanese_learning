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
    
    i = 0
    for x in text:
        j = 0
        if(x == "n"): #if is "n"
            if(len(text[i:]) == 1): #if is "n" on the last character
                for y in char['romaji']['all']:
                    if(y == x):
                        c = char['hiragana']['all'][j]
                        break
                    j += 1
                    
                to_hiragana += c
                #print(c) 
            
            elif(not text[i+1] in vowels and not text[i+1] in vowels_circumflex): #if is not "n + vowel"
                for y in char['romaji']['all']:
                    if(y == x):
                        c = char['hiragana']['all'][j]
                        break
                    j += 1
                    
                to_hiragana += c
                #print(c)

        elif(x in vowels_circumflex): #if is "vowel_circumflex"
            if(x == "â"):
                temp_c = "a"
            elif(x == "ê"):
                temp_c = "e"
            elif(x == "î"):
                temp_c = "i"
            elif(x == "ô"):
                temp_c = "o"
            elif(x == "û"):
                temp_c = "u"

            if(not text[i-1] in consonnes): #if is not "cons + vowel_circumflex"
                for y in char['romaji']['all']:
                    if(y == temp_c):
                        c = char['hiragana']['all'][j] + char['hiragana']['all'][j]
                        break
                    j += 1
                    
                to_hiragana += c
                #print(c)
                
            elif(text[i-1] in consonnes): #if is "cons + vowel_circumflex"
                if(text[i-2] in consonnes and not text[i-2] == "n"): #if is "cons + cons + vowel_circumflex"
                    c = text[i-2] + text[i-1] + temp_c
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    to_hiragana += c
                    #print(c)
 
                    j = 0
                    for y in char['romaji']['all']:
                        if(y == temp_c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    
                    to_hiragana += c
                    #print(c)

                else:
                    c = text[i-1] + temp_c
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    to_hiragana += c
                    #print(c)

                    j = 0
                    for y in char['romaji']['all']:
                        if(y == temp_c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    to_hiragana += c
                    #print(c)


        elif(x in vowels): #if is "vowel"
            if(not text[i-1] in consonnes): #if is not "cons + vowel"
                for y in char['romaji']['all']:
                    if(y == x):
                        c = char['hiragana']['all'][j]
                        break
                    j += 1
                    
                to_hiragana += c
                #print(c)
                
            elif(text[i-1] in consonnes): #if is "cons + vowel"
                if(text[i-2] in consonnes and not text[i-2] == "n"): #if is "cons + cons + vowel"
                    c = text[i-2] + text[i-1] + x
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    
                    to_hiragana += c
                    #print(c)
                else:
                    c = text[i-1] + x
                    for y in char['romaji']['all']:
                        if(y == c):
                            c = char['hiragana']['all'][j]
                            break
                        j += 1
                    to_hiragana += c
                    #print(c)
                    
        elif(not x in all): #if is space or not a letter (!&@...)
            to_hiragana += x
            #print(x)
        i += 1
    
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
When there is no choices
press Enter
""")
    function()
    
if __name__ == "__main__":
    main() 
