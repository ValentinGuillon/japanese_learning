import random

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



verbs = ["hanasu", "yomu", "asobu", "morau", "matsu", "omou", "motsu", "nomu", "kiku", "shinu", "nugu", "iu", "kau", "sumu", "iku", "noru", "naru", "wakaru", "aru", "oshieru", "miru", "taberu", "iru", "dekiru", "kaeru", "yameru", "ageru", "kuru", "suru"]
allForm = ["négative", "passé", "polie", "négative passé", "négative polie", "passé polie", "négative passé polie"]


verb = random.choice(verbs)
user = ""

while (1):
    form = random.choice(allForm)
    conjug = conjugVerbs(verb, form)
    user = input(f"\nverb = {verb}\nform = {form}\nconjug = {conjug}\n")
    if (user != ""):
        verb = random.choice(verbs)
        user = ""
