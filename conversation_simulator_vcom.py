import random

def function():
    topics = ["job", "country", "family how many members", "family who" ]
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
    a_name = ["Watashi wa [name]san desu.", 
              "[Name]san desu."]
    a_job = ["Watashi wa [job] desu.",
             "[Job] desu."]
    a_country = ["Watashi wa [pays] kara desu.",
                 "[Pays] kara desu."]
    a_family_howmany = ["Watashi no kazoku wa [n°]-nin desu."]
    a_family_who = ["[Member] to ... watashi desu."]


    answer = ""
    while(not topics == []):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        lead = input("Take initiative? (y/n) >")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        if(lead == "y"):
            print("Topic? (first letter)")
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
                    print(n)
                answer = random.choice(a_job)
                print("")
                input("answering...")
                print("\nComputer :")
                print(answer)
                input("")
                    
            elif(choose == "c"):
                topics.remove("country")
                print("Me :")
                for n in q_country:
                    print(n)
                answer = random.choice(a_country)
                print("")
                input("answering...")
                print("\nComputer :")
                print(answer)
                input("")
                    
            elif(choose == "fhmm"):
                topics.remove("family how many members")
                print("Me :")
                for n in q_family_howmany:
                    print(n)
                answer = random.choice(a_family_howmany)
                print("")
                input("answering...")
                print("\nComputer :")
                print(answer)
                input("")
                    
            elif(choose == "fw"):
                topics.remove("family who")
                print("Me :")
                for n in q_family_who:
                    print(n)
                answer = random.choice(a_family_who)
                print("")
                input("answering...")
                print("\nComputer :")
                print(answer)
                input("")
            
            
        elif(lead == "n"):
            question = random.choice(topics)
            if(question == "job"):
                topics.remove("job" )
                question = random.choice(q_job)
                print(f"Com :\n{question}")
                input("")
                print("Me :")
                for n in a_job:
                    print(n)
                input("")

            elif(question == "country"):
                topics.remove("country")
                question = random.choice(q_country)
                print(f"Com :\n{question}")
                input("")
                print("Me :")
                for n in a_country:
                    print(n)
                input("")

            elif(question == "family how many members"):
                topics.remove("family how many members")
                question = random.choice(q_family_howmany)
                print(f"Com :\n{question}")
                input("")
                print("Me :")
                for n in a_family_howmany:
                    print(n)
                input("")

            elif(question == "family who"):
                topics.remove("family who")
                question = random.choice(q_family_who)
                print(f"Com :\n{question}")
                input("")
                print("Me :")
                for n in a_family_who:
                    print(n)
                input("")
            
            


    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("There is no more topics.")
    restart = ""
    while(restart == ""):
        restart = input("Restart ? (y/n)\n>")
        if(restart == "y"):
            function()






def main():
    input("""
    	
=============================
        This program
           simule
       a conversation.
    Choose on each step
           if you
       ask questions
        or answer it
=============================
When there is no choices
press Enter
""")
    function()

if __name__ == "__main__":
    main() 