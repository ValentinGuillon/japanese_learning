#romaji_to_kana.py
from module_characters_jap import *
from module_romaji_to_kana import *


def presentation():
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


def function():
    while(1):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        text = input("Write your sentence/word\n(romaji only)\n>")
        to_hira = romaji_to_hira(text)
        to_kata = romaji_to_kata(text)
        input(f"\nHiragana\n {to_hira}\n\nKatakana\n {to_kata}\n...")





def main() :
    presentation()
    function()
    
if __name__ == "__main__":
    main() 
