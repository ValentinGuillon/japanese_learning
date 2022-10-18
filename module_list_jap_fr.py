#module_list.py

from typing import NamedTuple

"""
nb elements par liste
transports = 10
colors = 11
animals = 20
weather = 7
clothes = 11
food = 34
house = 21
divers = 37
verbs = 29
adjs = 30
all = 210

#expressions = 32
expressions = 1

conjug_verbs = 33
conjug_adjs = 12

"""



class W(NamedTuple) :
    kana: chr #'h' or 'k' pour "hira" et "kata"
    jap: str
    japAlt: list #different writing for a word
    fr: str
    frAlt: list #different writing for a word

#print fr/jap properties of "word", and the alt version if ones exist
def printW(word):
    print(f" {word.jap}")

    if(len(word.japAlt)):
        print(end="  ====== ")
        for n in word.japAlt:
            print(f"{n}, ", end="")
        print()
    
    print(f"  {word.fr}") #{word.japAlt}\n  {word.fr}\n  {word.frAlt}")

    if(len(word.frAlt)):
        print(end="  ====== ")
        for n in word.frAlt:
            print(f"{n}, ", end="")
        print()


eAccents = ['é', 'è', 'ê']
iAccents = ['î', 'ï']
#return an accentless version of fr word (use this function only with a word with accents)
def removeAccents(word):
    accentlessWord = ""

    for letter in word:
        if letter in eAccents:
            letter = 'e'
        elif letter in iAccents:
            letter = 'i'
        accentlessWord += letter

    return accentlessWord

japAccents = ['â', 'î', 'û', 'ê', 'ô']
#return an accentless version of jap  word (use this function only with a word with accents)
def convertJapAccent(word):
    accentlessWord = ""

    for letter in word:
        if letter == 'â':
            letter = "aa"
        elif letter == 'î':
            letter = "ii"
        elif letter == 'û':
            letter = "uu"
        elif letter == 'ê':
            letter = "ei"
        elif letter == 'ô':
            letter = "ou"
        accentlessWord += letter
    
    return accentlessWord
        



#mots jap
all = []
#imin = 0, imax = 9
transports = [W('h', "kuruma",     [], "voiture", []),
              W('k', "sukûtâ",     [], "scooter", []),
              W('h', "jitensha",   [], "vélo",    []),
              W('k', "takushî",    [], "taxi",    []),
              W('h', "chikatetsu", [], "métro",   []),
              W('h', "densha",     [], "train",   []),
              W('h', "hikôki",     [], "avion",   []),
              W('h', "fune",       [], "bateau",  []),
              W('k', "baiku",      [], "moto",    []),
              W('k', "basu",       [], "bus",     [])]

#imin = 10, imax = 20
colors = [W('h', "shiro",    [], "blanc",  []),
          W('h', "chairo",   [], "marron", []),
          W('h', "kîro",     [], "jaune",  []),
          W('h', "haîro",    [], "gris",   []),
          W('h', "ao",       [], "bleu",   []),
          W('h', "kuro",     [], "noir",   []),
          W('h', "aka",      [], "rouge",  []),
          W('h', "orenji",   [], "orange", []),
          W('h', "murasaki", [], "violet", []),
          W('h', "midori",   [], "vert",   []),
          W('k', "pinku",    [], "rose",   [])]

#imin = 21, imax = 40
animals = [W('h', "inu",      [], "chien",    []),
           W('h', "ahiru",    [], "canard",   []),
           W('h', "usagi",    [], "lapin",    []),
           W('h', "saru",     [], "singe",    []),
           W('h', "nezumi",   [], "souris",   []),
           W('h', "uma",      [], "cheval",   []),
           W('h', "kuma",     [], "ours",     []),
           W('h', "tora",     [], "tigre",    []),
           W('k', "raion",    [], "lion",     []),
           W('h', "niwatori", [], "poulet",   []),
           W('h', "shika",    [], "biche",    []),
           W('h', "buta",     [], "cochon",   []),
           W('h', "neko",     [], "chat",     []),
           W('h', "tori",     [], "oiseau",   []),
           W('h', "kitsune",  [], "renard",   []),
           W('h', "ushi",     [], "vache",    []),
           W('h', "zô",       [], "éléphant", []),
           W('h', "hitsuji",  [], "mouton",   []),
           W('k', "koara",    [], "koala",    []),
           W('k', "panda",    [], "panda",    [])]

#imin = 41, imax = 47
weather = [W('h', "kaminari", [], "orageux",     []),
           W('h', "kumori",   [], "nuageux",     []),
           W('h', "hare",     [], "ensoleillé",  []),
           W('h', "samui",    [], "froid",       []),
           W('h', "yuki",     [], "enneigé",     []),
           W('h', "atsui",    [], "chaud",       []),
           W('h', "ame",      [], "pluvieux",    [])]

#imin = 48, imax = 58
clothes = [W('h', "kutsushita", [], "chaussettes",     []),
           W('h', "kutsu",      [], "chaussures",      []),
           W('h', "jîpan",      [], "jeans",           []),
           W('h', "sukâto",     [], "jupe",            []),
           W('h', "kôto",       [], "manteau",         []),
           W('h', "zubon",      [], "pantalon",        []),
           W('k', "tîshatsu",   [], "t-shirt",         []),
           W('k', "sandaru",    [], "sandales",        []),
           W('h', "tanpan",     [], "short",           []),
           W('h', "doresu",     [], "robe",            []),
           W('h', "mizugi",     [], "maillot de bain", [])]

#imin = 59, imax = 92
food = [W('h', "tamanegi",     [], "oignon",              []),
        W('h', "budô",         [], "raisin",              []),
        W('h', "kamoniku",     [], "canard (viande)",     ["canard"]),
        W('k', "orenji",       [], "orange",              []),
        W('h', "suika",        [], "pastèque",            []),
        W('h', "tômorokoshi",  [], "maïs",                []),
        W('k', "remon",        [], "citron",              []),
        W('k', "burokkorî",    [], "brocoli",             []),
        W('h', "kyûri",        [], "concombre",           []),
        W('h', "ichigo",       [], "fraise",              []),
        W('h', "ninjin",       [], "carotte",             []),
        W('k', "kokonattsu",   [], "noix de coco",        []),
        W('h', "jagaimo",      [], "pomme de terre",      []),
        W('k', "bêkon",        [], "bécon",               []),
        W('h', "gyûnyû",       [], "lait",                []),
        W('h', "kyabetsu",     [], "chou",                []),
        W('h', "kinoko",       [], "champignon",          []),
        W('h', "kabocha",      [], "citrouille",          []),
        W('h', "mizu",         [], "eau",                 []),
        W('k', "tomato",       [], "tomate",              []),
        W('h', "ocha",         [], "thé",                 []),
        W('k', "eiyô dorinku", [], "boisson énergisante", []),
        W('k', "jûsu",         [], "jus",                 []),
        W('h', "kohitsuji",    [], "agneau (viande)",     ["agneau"]),
        W('h', "ringo",        [], "pomme",               []),
        W('k', "banana",       [], "banane",              []),
        W('k', "kôra",         [], "cola",                []),
        W('k', "kôhî",         [], "café",                []),
        W('h', "sakana",       [], "poisson (viande)",    ["poisson"]),
        W('h', "gyûniku",      [], "boeuf (viande)",      ["boeuf"]),
        W('h', "toriniku",     [], "poulet (viande)",     ["poulet"]),
        W('h', "nashi",        [], "poire",               []),
        W('h', "butaniku",     [], "porc (viande)",       ["porc"]),
        W('k', "painappuru",   [], "ananas",              [])]

#imin = 93, imax = 113
house = [W('k', "ea kondishonâ",    ["eakon"],   "climatiseur",         []),
         W('k', "kamera",           [],          "appareil photo",      []),
         W('k', "karendâ",          [],          "calendrier",          []),
         W('k', "kurejittokâdo",    [],          "carte bancaire",      ["carte de crédit", "carte de paiement"]),
         W('k', "konpyûta",         [],          "ordinateur",          []),
         W('k', "sutereofonikku",   ["sutereo"], "chaîne hi-fi",        []),
         W('k', "supûn",            [],          "cuillère",            []),
         W('k', "sofâ",             ["sofa"],    "canapé",              []),
         W('k', "têburu",           [],          "table",               []),
         W('k', "terebijon",        ["terebi"],  "télévision",          ["télé"]),
         W('k', "toiretto",         ["toire"],   "toilettes",           []),
         W('k', "doa",              [],          "porte",               []),
         W('k', "naifu",            [],          "couteau",             []),
         W('k', "nôto",             [],          "cahier",              []),
         W('k', "fôku",             [],          "fourchette",          []),
         W('k', "beddo",            [],          "lit",                 []),
         W('k', "pâsonarukonpyûta", ["pasokon"], "ordinateur portable", ["pc"]),
         W('k', "bôrupen",          ["pen"],     "stylo-bille",         ["stylo"]),
         W('k', "rajio",            [],          "radio",               []),
         W('k', "ranpu",            [],          "lampe",               []),
         W('k', "rimôtokontorôrâ",  ["rimokon"], "télécommande",        [])]

#imin = 114, imax = 149
divers = [W('h', "ai",               [], "amour",                  []),
          W('h', "ue",               [], "en haut",                ["haut"]),
          W('h', "aoi",              [], "bleu (adjectif)",        ["bleu"]),
          W('h', "ie",               [], "maison",                 []),
          W('h', "Îe",               [], "non",                    []),
          W('h', "sekai",            [], "monde",                  []),
          W('h', "kagi",             [], "clé",                    []),
          W('h', "akai",             [], "rouge (adjectif)",       ["rouge"]),
          W('h', "osushi",           [], "sushi (avec respect)",   ["sushi"]),
          W('h', "kugi",             [], "clou",                   []),
          W('h', "keigo",            [], "entrainement",           []),
          W('h', "saka",             [], "pente",                  []),
          W('h', "ya",               [], "magasin",                []),
          W('h', "hanaya",           [], "fleuriste",              []),
          W('h', "sakanaya",         [], "poissonnier",            []),
          W('h', "yuki",             [], "neige",                  []),
          W('h', "yoru",             [], "nuit",                   []),
          W('h', "karada",           [], "corps",                  []),
          W('h', "rikai",            [], "compréhension",          []),
          W('h', "ji",               [], "heure",                  []),
          W('h', "matsuri",          [], "festival",               []),
          W('h', "kûki",             [], "air",                    []),
          W('h', "tokei",            [], "montre / horloge",       ["horloge", "montre"]),
          W('h', "kinô",             [], "hier",                   []),
          W('h', "sakka",            [], "écrivain",               []),
          W('h', "irasutoneitâ",     [], "dessinateur",            []),
          W('h', "shashinka",        [], "photographe",            []),
          W('h', "seiyû",            [], "doubleur",               []),
          W('h', "kantoku",          [], "réalisateur",            []),
          W('h', "keikan",           [], "policier",               []),
          W('h', "kodomo no sensee", [], "animateur pour enfants", ["animateur"]),
          W('h', "gaka",             [], "peintre",                []),
          W('h', "kyaku",            [], "client",                 []),
          W('h', "jugyô",            [], "cours",                  []),
          W('h', "ryokô",            [], "voyage",                 []),
          W('h', "sanmyaku",         [], "chaîne de montagnes",    [])]

#imin = 150, imax = 178
verbs = [W('h', "hanasu",  [], "parler",                     []),
         W('h', "yomu",    [], "lire",                       []),
         W('h', "asobu",   [], "jouer / se divertir",        ["jouer", "se divertir"]),
         W('h', "morau",   [], "recevoir",                   []),
         W('h', "matsu",   [], "attendre",                   []),
         W('h', "omou",    [], "penser",                     []),
         W('h', "motsu",   [], "tenir / posséder",           ["tenir", "posséder"]),
         W('h', "nomu",    [], "boire",                      []),
         W('h', "kiku",    [], "demander",                   []),
         W('h', "shinu",   [], "mourir",                     []),
         W('h', "nugu",    [], "se déshabiller",             []),
         W('h', "iu",      [], "dire",                       []),
         W('h', "kau",     [], "acheter",                    []),
         W('h', "sumu",    [], "vivre / habiter",            ["vivre", "habiter"]),
         W('h', "iku",     [], "aller",                      []),
         W('h', "noru",    [], "monter dans",                []),
         W('h', "naru",    [], "devenir",                    []),
         W('h', "wakaru",  [], "comprendre",                 []),
         W('h', "aru",     [], "être / avoir (objet)",       ["Être / avoir", "être", "avoir"]),
         W('h', "oshieru", [], "enseigner / dire",           ["enseigner", "dire"]),
         W('h', "miru",    [], "regarder / voir",            ["regarder", "voir"]),
         W('h', "taberu",  [], "manger",                     []),
         W('h', "iru",     [], "être / avoir (être vivant)", ["être / avoir", "être", "avoir"]),
         W('h', "dekiru",  [], "être capable / pouvoir",     ["être capable", "pouvoir"]),
         W('h', "kaeru",   [], "rentrer / retourner",        ["rentrer", "retourner"]),
         W('h', "yameru",  [], "arrêter / abandonner",       ["arrêter", "arreter", "abandonner"]),
         W('h', "ageru",   [], "donner",                     []),
         W('h', "kuru",    [], "venir",                      []),
         W('h', "suru",    [], "faire",                      [])]

#imin = 179, imax = 208
adjs = [W('h', "hayai",      [], "rapide / tôt",                ["rapide", "tôt"]),
        W('h', "tanoshii",   [], "amusant",                     []),
        W('h', "samui",      [], "froid",                       []),
        W('h', "sugoi",      [], "incroyable / impressionnant", ["incroyable", "impressionnant"]),
        W('h', "ii",         [], "bon / bien / correct",        ["bon", "bien", "correct"]),
        W('h', "kakkoii",    [], "cool / beau-gosse",           ["cool", "beau-gosse"]),
        W('h', "warui",      [], "mauvais",                     []),
        W('h', "atsui",      [], "chaud",                       []),
        W('h', "chîsai",     [], "petit",                       []),
        W('h', "yasui",      [], "pas cher",                    []),
        W('h', "omoshiroi",  [], "intéressant",                 []),
        W('h', "muzukashii", [], "difficile",                   []),
        W('h', "itai",       [], "douloureux / aïe",            ["douloureux", "aïe"]),
        W('h', "takai",      [], "cher / haut",                 ["cher", "haut"]),
        W('h', "kowai",      [], "effrayant",                   []),
        W('h', "yasashii",   [], "gentil",                      []),
        W('h', "atarashii",  [], "neuf / nouveau",              ["neuf", "nouveau"]),
        W('h', "isogashii",  [], "occupé",                      []),
        W('h', "ôkii",       [], "gros / grand",                ["gros", "grand"]),
        W('h', "oishii",     [], "bon (goût)",                  ["bon"]),
        W('h', "jôzu",       [], "habille / doué",              ["habille", "doué"]),
        W('h', "kirei",      [], "beau / belle / joli",         ["beau", "belle", "joli"]),
        W('h', "suki",       [], "aimé / être aimé",            ["aimé", "être aimé"]),
        W('h', "kirai",      [], "détesté / être détesté",      ["détesté", "être détesté"]),
        W('h', "kantan",     [], "simple / facile",             ["simple", "facile"]),
        W('h', "hen",        [], "bizarre / étrange",           ["bizarre", "étrange"]),
        W('h', "taihen",     [], "situation difficile",         []),
        W('h', "anzen",      [], "sûr / en sécurité",           ["sûr", "en sécurité"]),
        W('h', "genki",      [], "en forme / en bonne santé",   ["en forme", "en bonne santé"]),
        W('h', "benri",      [], "pratique",                    [])]

#imin = 209, imax = 209
expressions = [W('h', "sumimasen", [], "excusez-moi / pardon pour le dérangement", ["excusez-moi", "pardon pour le dérangement"])]

conjug_verbs = [W('h', "-u -> -imasu",          ["imasu"],          "forme polie (vb 1er g)",                ["polie vb 1"]),
                W('h', "-u -> -imasen",         ["imasen"],         "forme négative polie (vb 1er g)",       ["négative polie vb 1"]),
                W('h', "-u -> -imashita",       ["imashita"],       "forme passé polie (vb 1er g)",          ["passé polie vb 1"]),
                W('h', "-u -> -imasen deshita", ['imasen deshita'], "forme négative passé polie (vb 1er g)", ["négative passé polie vb 1"]),

                W('h', "-u -> -tta",    ["tta"],   "forme passé (vb 1er g) -u",   ["passé vb 1"]),
                W('h', "-ru -> -tta",   ["tta"],   "forme passé (vb 1er g) -ru",  ["passé vb 1"]),
                W('h', "-tsu -> -tta",  ["tta"],   "forme passé (vb 1er g) -tsu", ["passé vb 1"]),
                W('h', "-gu -> -ida",   ["ida"],   "forme passé (vb 1er g) -gu",  ["passé vb 1"]),
                W('h', "-bu -> -nda",   ["nda"],   "forme passé (vb 1er g) -bu",  ["passé vb 1"]),
                W('h', "-mu -> -nda",   ["nda"],   "forme passé (vb 1er g) -mu",  ["passé vb 1"]),
                W('h', "-nu -> -nda",   ["nda"],   "forme passé (vb 1er g) -nu",  ["passé vb 1"]),
                W('h', "-su -> -shita", ["shita"], "forme passé (vb 1er g) -su",  ["passé vb 1"]),
                W('h', "-ku -> -ita",   ["ita"],   "forme passé (vb 1er g) -ku",  ["passé vb 1"]),

                W('h', "-u -> -wanai",   ["wanai"], "forme négative (vb 1er g) -u",   ["négative vb 1"]),
                W('h', "-_u -> -_anai",  ["anai"],  "forme négative (vb 1er g) -_u",  ["négative vb 1"]),
                W('h', "-tsu -> -tanai", ["tanai"], "forme négative (vb 1er g) -tsu", ["négative vb 1"]),

                W('h', "-u -> -wanakatta",   ["wanakatta"], "forme négative passé (vb 1er g) -u",   ["négative passé vb 1"]),
                W('h', "-_u -> -_anakatta",  ["anakatta"],  "forme négative passé (vb 1er g) -_u",  ["négative passé vb 1"]),
                W('h', "-tsu -> -tanakatta", ["tanakatta"], "forme négative passé (vb 1er g) -tsu", ["négative passé vb 1"]),

                W('h', "-ru -> -masu",          ["masu"],          "forme polie (vb 2e g)",                ["polie vb 2"]),
                W('h', "-ru -> -masen",         ["masen"],         "forme négative polie (vb 2e g)",       ["négative polie vb 2"]),
                W('h', "-ru -> -mashita",       ["mashita"],       "forme passé polie (vb 2e g)",          ["passé polie vb 2"]),
                W('h', "-ru -> -masen deshita", ["masen deshita"], "forme négative passé polie (vb 2e g)", ["négative passé vb 2"]),
                W('h', "-ru -> -ta",            ["ta"],            "forme passé (vb 2e g)",               ["passé vb 2"]),
                W('h', "-ru -> -nai",           ["nai"],           "forme négative (vb 2e g)",            ["négative vb 2"]),
                W('h', "-ru -> -nakatta",       ["nakatta"],       "forme négative passé (vb 2e g)",      ["négative passé vb 2"]),

                W('h', "suru -> shimasu  || kuru -> kimasu",                   ["shimasu / kimasu", "shimasu", "kimasu"],                                     "forme polie (vb 3e g)",                ["polie vb 3"]),
                W('h', "suru -> shimasen  || kuru -> kimasen",                 ["shimasen / kimasen", "shimasen", "kimasen"],                                 "forme négative polie (vb 3e g)",       ["négative polie vb 3"]),
                W('h', "suru -> shimashita  || kuru -> kimashita",             ["shimashita / kimashita", "shimashita", "kimashita"],                         "forme passé polie (vb 3e g)",          ["passé polie vb 3"]),
                W('h', "suru -> shimasen deshita  || kuru -> kimasen deshita", ["shimasen deshita / kimasen deshita", "shimasen deshita", "kimasen deshita"], "forme négative passé polie (vb 3e g)", ["négative passé polie vb 3"]),
                W('h', "suru -> shita  || kuru -> kita",                       ["shita / kita", "shita", "kita"],                                             "forme passé (vb 3e g)",               ["passé vb 3"]),
                W('h', "suru -> shinai  || kuru -> kinai",                     ["shinai / kinai", "shinai", "kinai"],                                         "forme négative (vb 3e g)",            ["négative vb 3"]),
                W('h', "suru -> shinakatta  || kuru -> kinakatta",             ["shinakatta / kinakatta", "shinakatta", "kinakatta"],                         "forme négative passé (vb 3e g)",      ["négative passé vb 3"])]

conjug_adjs = [W('h', "-i -> -kunai",     ["kunai"],     "forme négative (adj en i)",                   ["négative adj i"]),
               W('h', "-i -> -katta",     ["katta"],     "forme passé (adj en i)",                      ["passé adj i"]),
               W('h', "-i -> -kunakatta", ["kunakatta"], "forme négative passé (adj en i)",             ["négative passé adj i"]),
               W('h', "-i -> -sô",        ["sô"],        "forme \"ça a l'air\" (adj en i)",             ["ça à l'air adj i"]),
               W('h', "-i -> -kunasasô",  ["kunasasô"],  "forme négative de \"ça a l'air\" (adj en i)", ["négative ça à l'air adj i"]),
               W('h', "-i -> -ku",        ["ku"],        "transformation en adverbe (adj en i)",        ["adverbe adj i"]),

               W('h', "+ janai",     ["janai"],     "forme négative (adj en na)",                   ["négative adj na"]),
               W('h', "+ datta",     ["datta"],     "forme passé (adj en na)",                      ["passé adj na"]),
               W('h', "+ janakatta", ["janakatta"], "forme négative passé (adj en na)",             ["négative passé adj na"]),
               W('h', "+ -sô",       ["sô"],        "forme \"ça a l'air\" (adj en na)",             ["ça à l'air adj na"]),
               W('h', "+ -janasasô", ["janasasô"],  "forme négative de \"ça a l'air\" (adj en na)", ["négative ça à l'air adj na"]),
               W('h', "+ ni",        ["ni"],        "transformation en adverbe (adj en na)",        ["adverbe adj na"])]













#all =
for n in transports:
    all.append(n)
for n in colors:
    all.append(n)
for n in animals:
    all.append(n)
for n in weather:
    all.append(n)
for n in clothes:
    all.append(n)
for n in food:
    all.append(n)
for n in house:
    all.append(n)
for n in divers:
    all.append(n)
for n in verbs:
    all.append(n)
for n in adjs:
    all.append(n)
for n in expressions:
    all.append(n)




#add an alternative version to "frAlt" and "japAlt", if the word contains accents
#in All
for word in all:
    #JAP
    #check alt list
    if(len(word.japAlt)):
        for wordAlt in word.japAlt:
            accentFound = 0
            for letter in wordAlt:
                if letter in japAccents:
                    accentFound =  1

            if accentFound:
                word.japAlt.append(convertJapAccent(wordAlt))

    accentFound = 0
    #check the word
    for letter in word.jap:
        if letter in japAccents:
            accentFound =  1
    if accentFound:
        word.japAlt.insert(0, convertJapAccent(word.jap))


    #FR
    #check alt list
    if(len(word.frAlt)):
        for wordAlt in word.frAlt:
            accentFound = 0
            for letter in wordAlt:
                if letter in eAccents or letter in iAccents:
                    accentFound =  1

            if accentFound:
                #word.frAlt.append(removeAccents(wordAlt))
                word.frAlt.insert(word.frAlt.index(wordAlt) + 1, removeAccents(wordAlt))

    accentFound = 0
    #check the word
    for letter in word.fr:
        if letter in eAccents or letter in iAccents:
            accentFound =  1

    if accentFound:
        word.frAlt.insert(0, removeAccents(word.fr))


#in conjug_verbs
for word in conjug_verbs:
    #JAP
    #check alt list
    if(len(word.japAlt)):
        for wordAlt in word.japAlt:
            accentFound = 0
            for letter in wordAlt:
                if letter in japAccents:
                    accentFound =  1

            if accentFound:
                #word.japAlt.append(convertJapAccent(wordAlt))
                word.japAlt.insert(word.japAlt.index(wordAlt) + 1, convertJapAccent(wordAlt))

    accentFound = 0
    #check the word
    for letter in word.jap:
        if letter in japAccents:
            accentFound =  1
    if accentFound:
        word.japAlt.insert(0, convertJapAccent(word.jap))


    #FR
    #check alt list
    if(len(word.frAlt)):
        for wordAlt in word.frAlt:
            accentFound = 0
            for letter in wordAlt:
                if letter in eAccents or letter in iAccents:
                    accentFound =  1

            if accentFound:
                # word.frAlt.append(removeAccents(wordAlt))
                word.frAlt.insert(word.frAlt.index(wordAlt) + 1, removeAccents(wordAlt))

    accentFound = 0
    #check the word
    for letter in word.fr:
        if letter in eAccents or letter in iAccents:
            accentFound =  1

    if accentFound:
        word.frAlt.insert(0, removeAccents(word.fr))


#in conjug_adjs
for word in conjug_adjs:
    #JAP
    #check alt list
    if(len(word.japAlt)):
        for wordAlt in word.japAlt:
            accentFound = 0
            for letter in wordAlt:
                if letter in japAccents:
                    accentFound =  1

            if accentFound:
                # word.japAlt.append(convertJapAccent(wordAlt))
                word.japAlt.insert(word.japAlt.index(wordAlt) + 1, convertJapAccent(wordAlt))

    accentFound = 0
    #check the word
    for letter in word.jap:
        if letter in japAccents:
            accentFound =  1
    if accentFound:
        word.japAlt.insert(0, convertJapAccent(word.jap))


    #FR
    #check alt list
    if(len(word.frAlt)):
        for wordAlt in word.frAlt:
            accentFound = 0
            for letter in wordAlt:
                if letter in eAccents or letter in iAccents:
                    accentFound =  1

            if accentFound:
                # word.frAlt.append(removeAccents(wordAlt))
                word.frAlt.insert(word.frAlt.index(wordAlt) + 1, removeAccents(wordAlt))

    accentFound = 0
    #check the word
    for letter in word.fr:
        if letter in eAccents or letter in iAccents:
            accentFound =  1

    if accentFound:
        word.frAlt.insert(0, removeAccents(word.fr))



#pour vérifie que les mots correspondent
"""
i = 0
for n in all:
    if (i < 10):
        print(" ", end="")
    print(i, end=" ")
    printW(n)
    i = i + 1

for n in conjug_verbs:
    if (i < 10):
        print(" ", end="")
    print(i, end=" ")
    printW(n)
    i = i + 1
for n in conjug_adjs:
    if (i < 10):
        print(" ", end="")
    print(i, end=" ")
    printW(n)
    i = i + 1
"""

"""
i = 1
print("\nHiragana :")
for n in all:
    if n.kana == 'h':
        if (i < 10):
            print(" ", end="")
        print(i, end=" ")
        printW(n)
        i = i + 1

i = 1
print("\nKatakana :")
for n in all:
    if n.kana == 'k':
        if (i < 10):
            print(" ", end="")
        print(i, end=" ")
        printW(n)
        i = i + 1
"""






#pour vérifier le nombre d'éléments dans chaque liste
"""
print("\nTransport")
i = len(transports)
print(i)
print(transports[i - 1])

print("\nColors")
i = len(colors)
print(i)
print(colors[i - 1])

print("\nAnimals")
i = len(animals)
print(i)
print(animals[i - 1])

print("\nWeather")
i = len(weather)
print(i)
print(weather[i - 1])

print("\nClothes")
i = len(clothes)
print(i)
print(clothes[i - 1])

print("\nFood")
i = len(food)
print(i)
print(food[i - 1])

print("\nHouse")
i = len(house)
print(i)
print(house[i - 1])

print("\nDivers")
i = len(divers)
print(i)
print(divers[i - 1])

print("\nVerbs")
i = len(verbs)
print(i)
print(verbs[i - 1])

print("\nAdjectives")
i = len(adjs)
print(i)
print(adjs[i - 1])

print("\nExpressions")
i = len(expressions)
print(i)
print(expressions[i - 1])

print("\nConjugaison verbs")
i = len(conjug_verbs)
print(i)
print(conjug_verbs[i - 1])

print("\nConjugaison adjectives")
i = len(conjug_adjs)
print(i)
print(conjug_adjs[i - 1])

print("\nAll")
i = len(all)
print(i)
print(all[i - 1])
"""




"""
import random


category = "A"


iIndexInAll = 0
borneMin = 0
borneMax = len(all) - 1
#origin = '' #= word.kana

#a word is randomly choose, bases on the category
if(category == "A"):
    iIndexInAll = random.randint(0, len(all) - 1)




borneMin = 0
borneMax = len(transports) - 1
if(category == "t"):
    iIndexInAll = random.randint(borneMin, borneMax)

borneMin = borneMax + 1
borneMax += len(colors)
if(category == "c"):
    iIndexInAll = random.randint(borneMin, borneMax)

borneMin = borneMax + 1
borneMax += len(animals)
if(category == "a"):
    iIndexInAll = random.randint(borneMin, borneMax)

borneMin = borneMax + 1
borneMax += len(weather)
if(category == "w"):
    iIndexInAll = random.randint(borneMin, borneMax)

borneMin = borneMax + 1
borneMax += len(clothes)
if(category == "cl"):
    iIndexInAll = random.randint(borneMin, borneMax)

borneMin = borneMax + 1
borneMax += len(food)
if(category == "f"):
    iIndexInAll = random.randint(borneMin, borneMax)

borneMin = borneMax + 1
borneMax += len(house)
if(category == "h"):
    iIndexInAll = random.randint(borneMin, borneMax)

borneMin = borneMax + 1
borneMax += len(divers)
if(category == "d"):
    iIndexInAll = random.randint(borneMin, borneMax)

borneMin = borneMax + 1
borneMax += len(verbs)
if(category == "vb"):
    iIndexInAll = random.randint(borneMin, borneMax)

borneMin = borneMax + 1
borneMax += len(adjs)
if(category == "adj"):
    iIndexInAll = random.randint(borneMin, borneMax)


borneMin = borneMax + 1
borneMax += len(expressions)
if(category == "e"):
    iIndexInAll = random.randint(borneMin, borneMax)

if(category == "cv"):
    iIndexInAll = random.randint(0, len(conjug_verbs) - 1)
if(category == "ca"):
    iIndexInAll = random.randint(0, len(conjug_adjs) - 1)


"""



"""
for i in range(borneMin, borneMax + 1):
    print(f"{i} ", end="")
    printW(all[i])
"""



"""
#imin = 0, imax = 9
transports = [W('h', "kuruma",     [], "voiture", []),
              W('k', "basu",       [], "bus",     [])]

#imin = 10, imax = 20
colors = [W('h', "shiro",    [], "blanc",  []),
          W('k', "pinku",    [], "rose",   [])]

#imin = 21, imax = 40
animals = [W('h', "inu",      [], "chien",    []),
           W('k', "panda",    [], "panda",    [])]

#imin = 41, imax = 47
weather = [W('h', "kaminari", [], "orageux",     []),
           W('h', "ame",      [], "pluvieux",    [])]

#imin = 48, imax = 58
clothes = [W('h', "kutsushita", [], "chaussettes",     []),
           W('h', "mizugi",     [], "maillot de bain", [])]

#imin = 59, imax = 92
food = [W('h', "tamanegi",     [], "oignon",              []),
        W('k', "painappuru",   [], "ananas",              [])]

#imin = 93, imax = 113
house = [W('k', "ea kondishonâ",    ["eakon"],   "climatiseur",         []),
         W('k', "rimôtokontorôrâ",  ["rimokon"], "télécommande",        [])]

#imin = 114, imax = 149
divers = [W('h', "ai",               [], "amour",                  []),
          W('h', "sanmyaku",         [], "chaîne de montagnes",    [])]

#imin = 150, imax = 178
verbs = [W('h', "hanasu",  [], "parler",                     []),
         W('h', "suru",    [], "faire",                      [])]

#imin = 179, imax = 208
adjs = [W('h', "hayai",      [], "rapide / tôt",                ["rapide", "tôt"]),
        W('h', "benri",      [], "pratique",                    [])]

#imin = 209, imax = 209
expressions = [W('h', "sumimasen", [], "excusez-moi / pardon pour le dérangement", ["excusez-moi", "pardon pour le dérangement"])]

conjug_verbs = [W('h', "-u -> -imasu",          ["imasu"],          "forme polie (vb 1er g)",                ["polie vb 1"]),                                 "forme négative (vb 3e g)",            ["négative vb 3"]),
                W('h', "suru -> shinakatta  || kuru -> kinakatta",             ["shinakatta / kinakatta", "shinakatta", "kinakatta"],                         "forme négative passé (vb 3e g)",      ["négative passé vb 3"])]

conjug_adjs = [W('h', "-i -> -kunai",     ["kunai"],     "forme négative (adj en i)",                   ["négative adj i"]),
               W('h', "+ ni",        ["ni"],        "transformation en adverbe (adj en na)",        ["adverbe adj na"])]
"""

