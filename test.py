import random

formsVerb = {"négative": "nai",
            "passé": "ta",
            "polie": "masu",
            "négative passé": "nakatta",
            "négative polie": "masen",
            "passé polie": "mashita",
            "négative passé polie": "masen deshita"}

verbs = ["hanasu", "yomu", "asobu", "morau", "matsu", "omou", "motsu", "nomu", "kiku", "shinu", "nugu", "iu", "kau", "sumu", "iku", "noru", "naru", "wakaru", "aru", "oshieru", "miru", "taberu", "iru", "dekiru", "kaeru", "yameru", "ageru", "kuru", "suru"]
allFormVerb = ["négative", "passé", "polie", "négative passé", "négative polie", "passé polie", "négative passé polie"]

adjs = ["hayai", "tanoshii", "samui", "sugoi", "ii", "kakkoii", "warui", "atsui", "chîsai", "yasui", "omoshiroi", "muzukashii", "itai", "takai", "kowai", "yasashii", "atarashii", "isogashii", "ôkii", "oishii", "jôzu", "kirei", "suki", "kirai", "kantan", "hen", "taihen", "anzen", "genki", "benri"]
allFormAdj = ["négative", "passé", "ça à l'air", "négative passé", "négative ça à l'air", "adverbe"]


i = random.randint(0, len(formsVerb) - 1)


print(list(formsVerb.keys())[i])
