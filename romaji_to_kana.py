#romaji_to_kana.py
import module_romaji_to_kana
from module_characters_jap import *


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


def main():
    while(1):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        text = input("Write your sentence/word\n(romaji only)\n>")
        toHira = module_romaji_to_kana.romaji_to_hira(text)
        toKata = module_romaji_to_kana.romaji_to_kata(text)
        input(f"\nHiragana\n {toHira}\n\nKatakana\n {toKata}\n...")



if __name__ == "__main__":
    presentation()
    main()
