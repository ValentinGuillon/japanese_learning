import random

formsVerb = {"négative": "nai",
            "passé": "ta",
            "polie": "masu",
            "négative passé": "nakatta",
            "négative polie": "masen",
            "passé polie": "mashita",
            "négative passé polie": "masen deshita"}
#exceptVerbs = {} #exemple {"vb1": 2, "vb2": 2, "vb3", 1}
def conjugVerbs(verb, form): #form = ["négative", "passé", "polie", "négative passé", "négative polie", "passé polie", "négative passé polie"]
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


formsAdj = {"négative": "nai",
            "passé": "tta",
            "ça à l'air": "sô",
            "négative passé": "katta",
            "négative ça à l'air": "nasasô"}
def conjugAdj(adj, form):
    conjug = ""
    group = ""
    if (form != "adverbe"):
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



verbs = ["hanasu", "yomu", "asobu", "morau", "matsu", "omou", "motsu", "nomu", "kiku", "shinu", "nugu", "iu", "kau", "sumu", "iku", "noru", "naru", "wakaru", "aru", "oshieru", "miru", "taberu", "iru", "dekiru", "kaeru", "yameru", "ageru", "kuru", "suru"]
allFormVerb = ["négative", "passé", "polie", "négative passé", "négative polie", "passé polie", "négative passé polie"]

adjs = ["hayai", "tanoshii", "samui", "sugoi", "ii", "kakkoii", "warui", "atsui", "chîsai", "yasui", "omoshiroi", "muzukashii", "itai", "takai", "kowai", "yasashii", "atarashii", "isogashii", "ôkii", "oishii", "jôzu", "kirei", "suki", "kirai", "kantan", "hen", "taihen", "anzen", "genki", "benri"]
allFormAdj = ["négative", "passé", "ça à l'air", "négative passé", "négative ça à l'air", "adverbe"]



verb = random.choice(verbs)
adj = random.choice(adjs)
user = ""

while (0):
    form = random.choice(allFormVerb)
    conjug = conjugVerbs(verb, form)
    user = input(f"\nverb = {verb}\nform = {form}\nconjug = {conjug}\n")
    if (user != ""):
        verb = random.choice(verbs)
        user = ""

while (1):
    form = random.choice(allFormAdj)
    conjug = conjugAdj(adj, form)
    user = input(f"\adj = {adj}\nform = {form}\nconjug = {conjug}\n")
    if (user != ""):
        adj = random.choice(adjs)
        user = ""
