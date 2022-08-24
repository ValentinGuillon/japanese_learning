#romaji_to_kana.py
from module_characters_jap import *
from module_romaji_to_kana import *

def function():
    lang = input("Romaji => Hiragana (h)\nRomaji => Katagana(k)\n>")
    while(not lang == "h" and not lang == "k"):
        lang = input(">")

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    text = input("Write your sentence/word\n(romaji only)\n>")
    to_hiragana = romaji_to_hiragana(text)
    to_katagana = romaji_to_katagana(text)
    input("traducting...")
    if (lang == "h"):
        input(f"{to_hiragana}\n")
    elif (lang == "k"):
        input(f"{to_katagana}\n")
    
    restart = ""
    while(restart == ""):
        restart = input("New sentence/word ? (y/n)\n>")
        if(restart == "y"):
            function()





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
Press Enter to proceed
when nothing is asked.
...
""")
    input("""This symbol ">",
means an answer is expected.
=============================
""")
    function()
    
if __name__ == "__main__":
    main() 
