import random
from romaji_to_kana_vcom import romaji_to_hiragana


def langage():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    lang = input("Choose langage:\nRomaji (r)\nHiragana (h)\n>")
    while(not lang == "r" and not lang == "h"):
        lang = input(">")
    function(lang)

def function(lang):
    topics = ["job", "country", "family how many members", "family who"]
    #Questions
    q_name = ["Onamae wa nan desu ka.", 
            "Onamae wa?"]
    q_job = ["Oshigoto wa nan desu ka.",
           "Oshigoto wa?"]
    q_country = ["Okuni wa nan desu ka.",
               "Okuni wa?", 
               "Dochira kara nan desu ka.", 
               "Dochira kara?"]
    q_family_howmany = ["Kazoku wa nan-nin desu ka."]
    q_family_who = ["Kazoku wa dare ga imasu ka.", 
                     "Kazoku wa dare desu ka."]
    
    #answers
    a_name = ["Watashi wa [namae]san desu.", 
              "[Namae]san desu."]
    a_job = ["Watashi wa [shigoto] desu.",
             "[shigoto] desu."]
    a_country = ["Watashi wa [kuni] kara desu.",
                 "[Kuni] kara desu."]
    a_family_howmany = ["Watashi no kazoku wa [bangô]-nin desu."]
    a_family_who = ["[Ichiin] to ... watashi desu."]


    answer = ""
    while(not topics == []):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        lead = input(""""STOP" to end the program.\n\n\n\nTake initiative? (y/n)\n>""")
        if(lead == "STOP"):
            topics = []
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        if(lead == "y"):
            print("Which topic? (first letter)")
            i = len(topics)
            for n in topics:
                i -= 1
                if(i == 0):
                    print(n)
                else:
                    print(n, end="\n")
                    
            choose = input(">")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            if(choose == "j"):
                topics.remove("job")
                print("Me :")
                for n in q_job:
                    if(lang == "r"):
                        print(n)
                    elif(lang == "h"):
                        print(romaji_to_hiragana(n))
                answer = random.choice(a_job)
                print("")
                input("answering...")
                print("\nComputer :")
                if(lang == "r"):
                    print(answer)
                elif(lang == "h"):
                    print(romaji_to_hiragana(answer))
                input("")
                    
            elif(choose == "c"):
                topics.remove("country")
                print("Me :")
                for n in q_country:
                    if(lang == "r"):
                        print(n)
                    elif(lang == "h"):
                        print(romaji_to_hiragana(n))
                answer = random.choice(a_country)
                print("")
                input("answering...")
                print("\nComputer :")
                if(lang == "r"):
                    print(answer)
                elif(lang == "h"):
                    print(romaji_to_hiragana(answer))
                input("")
                    
            elif(choose == "fhmm"):
                topics.remove("family how many members")
                print("Me :")
                for n in q_family_howmany:
                    if(lang == "r"):
                        print(n)
                    elif(lang == "h"):
                        print(romaji_to_hiragana(n))
                answer = random.choice(a_family_howmany)
                print("")
                input("answering...")
                print("\nComputer :")
                if(lang == "r"):
                    print(answer)
                elif(lang == "h"):
                    print(romaji_to_hiragana(answer))
                input("")
                    
            elif(choose == "fw"):
                topics.remove("family who")
                print("Me :")
                for n in q_family_who:
                    if(lang == "r"):
                        print(n)
                    elif(lang == "h"):
                        print(romaji_to_hiragana(n))
                answer = random.choice(a_family_who)
                print("")
                input("answering...")
                print("\nComputer :")
                if(lang == "r"):
                    print(answer)
                elif(lang == "h"):
                    print(romaji_to_hiragana(answer))
                input("")
            
            
        elif(lead == "n"):
            question = random.choice(topics)
            if(question == "job"):
                topics.remove("job" )
                question = random.choice(q_job)
                if(lang == "r"):
                    print(f"Com :\n{question}")
                elif(lang == "h"):
                    print(f"Com :\n{romaji_to_hiragana(question)}")
                input("")
                print("Me :")
                for n in a_job:
                    if(lang == "r"):
                        print(n)
                    elif(lang == "h"):
                        print(romaji_to_hiragana(n))
                input("")

            elif(question == "country"):
                topics.remove("country")
                question = random.choice(q_country)
                if(lang == "r"):
                    print(f"Com :\n{question}")
                elif(lang == "h"):
                    print(f"Com :\n{romaji_to_hiragana(question)}")
                input("")
                print("Me :")
                for n in a_country:
                    if(lang == "r"):
                        print(n)
                    elif(lang == "h"):
                        print(romaji_to_hiragana(n))
                input("")

            elif(question == "family how many members"):
                topics.remove("family how many members")
                question = random.choice(q_family_howmany)
                if(lang == "r"):
                    print(f"Com :\n{question}")
                elif(lang == "h"):
                    print(f"Com :\n{romaji_to_hiragana(question)}")
                input("")
                print("Me :")
                for n in a_family_howmany:
                    if(lang == "r"):
                        print(n)
                    elif(lang == "h"):
                        print(romaji_to_hiragana(n))
                input("")

            elif(question == "family who"):
                topics.remove("family who")
                question = random.choice(q_family_who)
                if(lang == "r"):
                    print(f"Com :\n{question}")
                elif(lang == "h"):
                    print(f"Com :\n{romaji_to_hiragana(question)}")
                input("")
                print("Me :")
                for n in a_family_who:
                    if(lang == "r"):
                        print(n)
                    elif(lang == "h"):
                        print(romaji_to_hiragana(n))
                input("")
            

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("There is no more topics.")
    restart = input("Restart ? (y/n)\n>")
    while(restart == "" or not restart == "n"):
        if(restart == "y"):
            langage()
            break
        restart = input(">")






def main():
    input("""
==============================================
     This program simule a conversation.
          Choose on each step
      if you ask questions or answer it
==============================================
Press Enter to proceed when nothing is asked.
...
""")
    input("""This symbol ">", means an answer is expected.
==============================================
""")
    langage()

if __name__ == "__main__":
    main() 