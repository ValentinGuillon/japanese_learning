#romaji_to_kana.py
from modules.module_characters_jap import *
from modules.module_romaji_to_kana import *

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
