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

conjug_verbs = 33
conjug_adjs = 12

#expressions = 32
expressions = 1
"""



class W(NamedTuple) :
    kana: chr #'h' or 'k' pour "hira" et "kata"
    jap: str
    fr: str

def printW(word):
    print(f" {word.jap} -> {word.fr}")



#mots jap
all = []
transports = [W('h', "Kuruma", "Voiture"), W('k', "Sukûtâ", "Scooter"), W('h', "Jitensha", "Vélo"), W('k', "Takushî", "Taxi"), W('h', "Chikatetsu", "Métro"), W('h', "Densha", "Train"), W('h', "Hikôki", "Avion"), W('h', "Fune", "Bateau"), W('k', "Baiku", "Moto"), W('k', "Basu", "Bus")]
colors = [W('h', "Shiro", "Blanc"), W('h', "Chairo", "Marron"), W('h', "Kiiro", "Jaune"), W('h', "Haiiro", "Gris"), W('h', "Ao", "Bleu"), W('h', "Kuro", "Noir"), W('h', "Aka", "Rouge"), W('h', "Orenji", "Orange"), W('h', "Murasaki", "Violet"), W('h', "Midori", "Vert"), W('k', "Pinku", "Rose")]
animals = [W('h', "Inu", "Chien"), W('h', "Ahiru", "Canard"), W('h', "Usagi", "Lapin"), W('h', "Saru", "Singe"), W('h', "Nezumi", "Souris"), W('h', "Uma", "Cheval"), W('h', "Kuma", "Ours"), W('h', "Tora", "Tigre"), W('k', "Raion", "Lion"), W('h', "Niwatori", "Poulet"), W('h', "Shika", "Biche"), W('h', "Buta", "Cochon"), W('h', "Neko", "Chat"), W('h', "Tori", "Oiseau"), W('h', "Kitsune", "Renard"), W('h', "Ushi", "Vache"), W('h', "Zô", "Éléphant"), W('h', "Hitsuji", "Mouton"), W('k', "Koara", "Koala"), W('k', "Panda", "Panda")]
weather = [W('h', "Kaminari", "Orageux"), W('h', "Kumori", "Nuageux"), W('h', "Hare",  "Ensoleillé"), W('h', "Samui", "Froid"), W('h', "Yuki", "Enneigé"), W('h', "Atsui", "Chaud"), W('h', "Ame", "Pluvieux")]
clothes = [W('h', "Kutsushita", "Chaussettes"), W('h', "Kutsu", "Chaussures"), W('h', "Jîpan", "Jeans"), W('h', "Sukâto", "Jupe"), W('h', "Kôto", "Manteau"), W('h', "Zubon", "Pantalon"), W('k', "Tîshatsu", "T-shirt"), W('k', "Sandaru", "Sandales"), W('h', "Tan pan", "Short"), W('h', "Doresu", "Robe"), W('h', "Mizugi", "Maillot de bain")]
food = [W('h', "Tamanegi", "Oignon"), W('h', "Budô", "Raisin"), W('h', "Kamoniku", "Canard (viande)"), W('k', "Orenji", "Orange"), W('h', "Suika", "Pastèque"), W('h', "Tômorokoshi", "Maïs"), W('k', "Remon", "Citron"), W('k', "Burokkorî", "Brocoli"), W('h', "Kyûri", "Concombre"), W('h', "Ichigo", "Fraise"), W('h', "Ninjin", "Carotte"), W('k', "Kokonattsu", "Noix de coco"), W('h', "Jagaimo", "Pomme de terre"), W('k', "Bêkon", "Bécon"), W('h', "Gyûnyû", "Lait"), W('h', "Kyabetsu", "Chou"), W('h', "Kinoko", "Champignon"), W('h', "Kabocha", "Citrouille"), W('h', "Mizu", "Eau"), W('k', "Tomato", "Tomate"), W('h', "Ocha", "Thé"), W('k', "Eiyô dorinku", "Boisson énergisante"), W('k', "Jûsu", "Jus"), W('h', "Kohitsuji", "Agneau (viande)"), W('h', "Ringo", "Pomme"), W('k', "Banana", "Banane"), W('k', "Kôra", "Cola"), W('k', "Kôhî", "Café"), W('h', "Sakana", "Poisson (viande)"), W('h', "Gyûniku", "Boeuf (viande)"), W('h', "Toriniku", "Poulet (viande)"), W('h', "Nashi", "Poire"), W('h', "Butaniku", "Porc (viande)"), W('k', "Painappuru", "Ananas")]
house = [W('k', "Eakon", "Climatiseur"), W('k', "Kamera", "Appareil photo"), W('k', "Karendâ", "Calendrier"), W('k', "Kurejittokâdo", "Carte de paiement"), W('k', "Konpyûta", "Ordinateur"), W('k', "Sutereo / Sutereofonikku", "Chaîne Hi-Fi"), W('k', "Supûn", "Cuillère"), W('k', "Sofâ", "Canapé"), W('k', "Têburu", "Table"), W('k', "Terebi / Terebijon", "Télévision"), W('k', "Toire / Toiretto", "Toilettes"), W('k', "Doa", "Porte"), W('k', "Naifu", "Couteau"), W('k', "Nôto", "Cahier"), W('k', "Fôku", "Fourchette"), W('k', "Beddo", "Lit"), W('k', "Pasokon", "PC (Ordi portable)"), W('k', "Pen / Bôrupen", "Stylo / Stylo-bille"), W('k', "Rajio", "Radio"), W('k', "Ranpu", "Lampe"), W('k', "Rimokon", "Télécommande")]
divers = [W('h', "Ai", "Amour"), W('h', "Ue", "En haut / Haut"), W('h', "Aoi", "Bleu (adjectif)"), W('h', "Ie", "Maison"), W('h', "Iie", "Non"), W('h', "Sekai", "Monde"), W('h', "Kagi", "Clé"), W('h', "Akai", "Rouge (adjectif)"), W('h', "Osushi", "Sushi (avec respect)"), W('h', "Kugi", "Clou"), W('h', "Keigo", "Entrainement"), W('h', "Saka", "Pente"), W('h', "Ya", "Magasin"), W('h', "Hanaya", "Fleuriste"), W('h', "Sakanaya", "Poissonnier"), W('h', "Yuki", "Neige"), W('h', "Yoru", "Nuit"), W('h', "Karada", "Corps"), W('h', "Rikai", "Compréhension"), W('h', "Ji", "Heure"), W('h', "Omatsuri", "Nom d'un Festival"), W('h', "Kuuki", "Air"), W('h', "Tokei", "Montre / Horloge"), W('h', "Kinoe", "Hier"), W('h', "Sakka", "Écrivain"), W('h', "Irasutoneitaa", "Dessinateur"), W('h', "Shashinka", "Photographe"), W('h', "Seiyuu", "Doubleur"), W('h', "Eegakantoku", "Réalisateur"), W('h', "Keesan", "Policier"), W('h', "Kodomo no sensee", "Animateur pour enfants"), W('h', "Gaka", "Peintre"), W('h', "Kyaku", "Client"), W('h', "Jugyoe", "Cours"), W('h', "Ocha", "Thé"), W('h', "Ryokoe", "Voyage"), W('h', "Sanmyaku", "Chaîne de montagnes")]
verbs = [W('h', "Hanasu", "Parler"), W('h', "Yomu", "Lire"), W('h', "Asobu", "Jouer / Se divertir"), W('h', "Morau", "Recevoir"), W('h', "Matsu", "Attendre"), W('h', "Omou", "Penser"), W('h', "Motsu", "Tenir / Posséder"), W('h', "Nomu", "Boire"), W('h', "Kiku", "Demander"), W('h', "Shinu", "Mourir"), W('h', "Nugu", "Se déshabiller"), W('h', "Iu", "Dire"), W('h', "Kau", "Acheter"), W('h', "Sumu", "Vivre / Habiter"), W('h', "Iku", "Aller"), W('h', "Noru",  "Monter dans"), W('h', "Naru", "Devenir"), W('h', "Wakaru", "Comprendre"), W('h', "Aru", "Être / Avoir (objet)"), W('h', "Oshieru", "Enseigner / Dire"), W('h', "Miru", "Regarder / Voir"), W('h', "Taberu", "Manger"), W('h', "Iru", "Être / Avoir (être vivant)"), W('h', "Dekiru", "Être capable / Pouvoir"), W('h', "Kaeru", "Rentrer / Retourner"), W('h', "Yameru", "Arrêter / Abandonner"), W('h', "Ageru", "Donner"), W('h', "Kuru", "Venir"), W('h', "Suru", "Faire")]
adjs = [W('h', "Hayai", "Rapide / Tôt"), W('h', "Tanoshii", "Amusant"), W('h', "Samui", "Froid"), W('h', "Sugoi", "Incroyable / Impressionnant"), W('h', "Ii", "Bon / Bien / Correct"), W('h', "Kakkoii", "Cool / Beau-gosse"), W('h', "Warui", "Mauvais"), W('h', "Atsui", "Chaud"), W('h', "Chiisai", "Petit"), W('h', "Yasui", "Pas cher"), W('h', "Omoshiroi", "Intéressant"), W('h', "Muzukashii", "Difficile"), W('h', "Itai", "Douloureux / Aïe"), W('h', "Takai", "Cher / Haut"), W('h', "Kowai", "Effrayant"), W('h', "Yasashii", "Gentil"), W('h', "Atarashii", "Neuf / Nouveau"), W('h', "Isogashii", "Occupé"), W('h', "Ookii", "Gros / Grand"), W('h', "Oishii", "Bon (goût)"), W('h', "Jôzu", "Habille / Doué"), W('h', "Kirei", "Beau / Belle / Jolie"), W('h', "Suki", "Aimé / Être aimé"), W('h', "Kirai", "Détester / Être détester"), W('h', "Kantan", "Simple / Facile"), W('h', "Hen", "Bizarre / Étrange"), W('h', "Taihen", "Situation difficile"), W('h', "Anzen", "Sûr / En sécurité"), W('h', "Genki", "En forme / En bonne santé"), W('h', "Benri", "Pratique")]
conjug_verbs = [W('h', "-u -> -imasu", "Forme polie (verbes 1er g)"), W('h', "-u -> -imasen", "Forme négative polie (verbes 1er g)"), W('h', "-u -> -imashita", "Forme passé polie (verbes 1er g)"), W('h', "-u -> -imasen deshita", "Forme négative passé polie (verbes 1er g)"),

                W('h', "-u -> -tta", "Forme passé (verbes 1er g) -u"), W('h', "-ru -> -tta", "Forme passé (verbes 1er g) -ru"), W('h', "-tsu -> -tta", "Forme passé (verbes 1er g) -tsu"), W('h', "-gu -> -ida", "Forme passé (verbes 1er g) -gu"), W('h', "-bu -> -nda", "Forme passé (verbes 1er g) -bu"), W('h', "-mu -> -nda", "Forme passé (verbes 1er g) -mu"), W('h', "-nu -> -nda", "Forme passé (verbes 1er g) -nu"), W('h', "-su -> -shita", "Forme passé (verbes 1er g) -su"), W('h', "-ku -> -ita", "Forme passé (verbes 1er g) -ku"),

                W('h', "-u -> -wanai", "Forme négative (verbes 1er g) -u"), W('h', "-_u -> -_anai", "Forme négative (verbes 1er g) -_u"), W('h', "-tsu -> -tanai", "Forme négative (verbes 1er g) -tsu"),

                W('h', "-u -> -wanakatta", "Forme négative passé (verbes 1er g) -u"), W('h', "-_u -> -_anakatta", "Forme négative passé (verbes 1er g) -_u"), W('h', "-tsu -> -tanakatta", "Forme négative passé (verbes 1er g) -tsu"),

                W('h', "-ru -> -masu", "Forme polie (verbes 2e g)"), W('h', "-ru -> -masen", "Forme négative polie (verbes 2e g)"), W('h', "-ru -> -mashita", "Forme passé polie (verbes 2e g)"), W('h', "-ru -> -masen deshita", "Forme négative passé polie (verbes 2e g)"), W('h', "-ru -> -ta", "Forme passé (verbes 2e g)"), W('h', "-ru -> -nai", "Forme négative (verbes 2e g)"), W('h', "-ru -> -nakatta", "Forme négative passé (verbes 2e g)"),

                W('h', "Suru -> Shimasu  || Kuru -> Kimasu", "Forme polie (verbes 3e g)"), W('h', "Suru -> Shimasen  || Kuru -> Kimasen", "Forme négative polie (verbes 3e g)"), W('h', "Suru -> Shimashita  || Kuru -> Kimashita", "Forme passé polie (verbes 3e g)"), W('h', "Suru -> Shimasen deshita  || Kuru -> Kimasen deshita", "Forme négative passé polie (verbes 3e g)"), W('h', "Suru -> Shita  || Kuru -> Kita", "Forme passé (verbes 3e g)"), W('h', "Suru -> Shinai  || Kuru -> Kinai", "Forme négative (verbes 3e g)"), W('h', "Suru -> Shinakatta  || Kuru -> Kinakatta", "Forme négative passé (verbes 3e g)")]
conjug_adjs = [W('h', "-i -> -kunai", "Forme négative (adjectifs en i)"), W('h', "-i -> -katta", "Forme passée (adjectifs en i)"), W('h', "-i -> -kunakatta", "Forme négative passée (adjectifs en i)"), W('h', "-i -> -sô", "Forme ''ça a l'air'' (adjectifs en i)"), W('h', "-i -> -kunasasô", "Forme négative de ''ça a l'air'' (adjectifs en i)"), W('h', "-i -> -ku", "Transformation en adverbe (adjectifs en i)"),
               W('h', "+ janai", "Forme négative (adjectifs en na)"), W('h', "+ datta", "Forme passée (adjectifs en na)"), W('h', "+ janakatta", "Forme négative passée (adjectifs en na)"), W('h', "+ -sô", "Forme ''ça a l'air'' (adjectifs en na)"), W('h', "+ -janasasô", "Forme négative de ''ça a l'air'' (adjectifs en na)"), W('h', "+ ni", "Transformation en adverbe (adjectifs en na)")]


expressions = [W('h', "Sumimasen", "Excusez-moi / Pardon pour le dérangement")]










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




#pour vérifie que les mots correspondent
"""
i = 1
for n in all:
    if (i < 10):
        print(" ", end="")
    print(i, end=" ")
    printW(n)
    i = i + 1

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

print("\nConjugaison verbs")
i = len(conjug_verbs)
print(i)
print(conjug_verbs[i - 1])

print("\nConjugaison adjectives")
i = len(conjug_adjs)
print(i)
print(conjug_adjs[i - 1])

print("\nExpressions")
i = len(expressions)
print(i)
print(expressions[i - 1])

print("\nAll")
i = len(all)
print(i)
print(all[i - 1])
"""
