#module_list_jap_fr.py

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
    fr: str
    jap: int

def printW(a):
    print(f" {a.fr} -> {a.jap}")



#mots jap
all_jap = []
transports_jap = [W("Kuruma", W("Sukûtâ", W("Jitensha", W("Takushî", W("Chikatetsu", W("Densha", W("Hikôki", W("Fune", W("Baiku", W("Basu"]
colors_jap = [W("Shiro", W("Chairo", W("Kiiro", W("Haiiro", W("Ao", W("Kuro", W("Aka", W("Orenji", W("Murasaki", W("Midori", W("Pinku"]
animals_jap = [W("Inu", W("Ahiru", W("Usagi", W("Saru", W("Nezumi", W("Uma", W("Kuma", W("Tora", W("Raion", W("Niwatori", W("Shika", W("Buta", W("Neko", W("Tori", W("Kitsune", W("Ushi", W("Zô", W("Hitsuji", W("Koara", W("Panda" ]
weather_jap = [W("Kaminari", W("Kumori", W("Hare", W("Samui", W("Yuki", W("Atsui", W("Ame"]
clothes_jap = [W("Kutsushita", W("Kutsu", W("Jîpan", W("Sukâto", W("Kôto", W("Zubon", W("Tîshatsu", W("Sandaru", W("Tan pan", W("Doresu", W("Mizugi" ]
food_jap = [W("Tamanegi", W("Budô", W("Kamoniku", W("Orenji", W("Suika", W("Tômorokoshi", W("Remon", W("Burokkorî", W("Kyûri", W("Ichigo", W("Ninjin", W("Kokonattsu", W("Jagaimo", W("Bêkon", W("Gyûnyû", W("Kyabetsu", W("Kinoko", W("Kabocha", W("Mizu", W("Tomato", W("Ocha", W("Eiyô dorinku", W("Jûsu", W("Kohitsuji", W("Ringo", W("Banana", W("Kôra", W("Kôhî", W("Sakana", W("Gyûniku", W("Toriniku", W("Nashi", W("Butaniku", W("Painappuru"]
house_jap = [W("Eakon", W("Kamera", W("Karendâ", W("Kurejittokâdo", W("Konpyûta", W("Sutereo / Sutereofonikku", W("Supûn", W("Sofâ", W("Têburu", W("Terebi / Terebijon", W("Toire / Toiretto", W("Doa", W("Naifu", W("Nôto", W("Fôku", W("Beddo", W("Pasokon", W("Pen / Bôrupen", W("Rajio", W("Ranpu", W("Rimokon"]
divers_jap = ["Ai", "Ue", "Aoi", "Ie", "Iie", "Sekai", "Kagi", "Akai", "Osushi", "Kugi", "Keigo", "Saka", "Ya", "Hanaya", "Sakanaya", "Yuki", "Yoru", "Karada", "Rikai", "Ji", "Omatsuri", "Kuuki", "Tokei", "Kinoe", "Sakka", "Irasutoneitaa", "Shashinka", "Seiyuu", "Eegakantoku", "Keesan", "Kodomo no sensee", "Gaka", "Kyaku", "Jugyoe", "Ocha", "Ryokoe", "Sanmyaku"]
verbs_jap = ["Hanasu", "Yomu", "Asobu", "Morau", "Matsu", "Omou", "Motsu", "Nomu", "Kiku", "Shinu", "Nugu", "Iu", "Kau", "Sumu", "Iku", "Noru", "Naru", "Wakaru", "Aru", "Oshieru", "Miru", "Taberu", "Iru", "Dekiru", "Kaeru", "Yameru", "Ageru", "Kuru", "Suru"]
adjs_jap = ["Hayai", "Tanoshii", "Samui", "Sugoi", "Ii", "Kakkoii", "Warui", "Atsui", "Chiisai", "Yasui", "Omoshiroi", "Muzukashii", "Itai", "Takai", "Kowai", "Yasashii", "Atarashii", "Isogashii", "Ookii", "Oishii", "Jôzu", "Kirei", "Suki", "Kirai", "Kantan", "Hen", "Taihen", "Anzen", "Genki", "Benri"]
conjug_verbs_jap = ["-u -> -imasu", "-u -> -imasen", "-u -> -imashita", "-u -> -imasen deshita",
                        "-u -> -tta", "-ru -> -tta", "-tsu -> -tta", "-gu -> -ida", "-bu -> -nda", "-mu -> -nda", "-nu -> -nda", "-su -> -shita", "-ku -> -ita",
                        "-u -> -wanai", "-_u -> -_anai", "-tsu -> -tanai",
                        "-u -> -wanakatta", "-_u -> -_anakatta", "-tsu -> -tanakatta",
                    "-ru -> -masu", "-ru -> -masen", "-ru -> -mashita", "-ru -> -masen deshita", "-ru -> -ta", "-ru -> -nai", "-ru -> -nakatta",
                    "Suru -> Shimasu  || Kuru -> Kimasu", "Suru -> Shimasen  || Kuru -> Kimasen", "Suru -> Shimashita  || Kuru -> Kimashita", "Suru -> Shimasen deshita  || Kuru -> Kimasen deshita", "Suru -> Shita  || Kuru -> Kita", "Suru -> Shinai  || Kuru -> Kinai", "Suru -> Shinakatta  || Kuru -> Kinakatta"]
conjug_adjs_jap = ["-i -> -kunai", "-i -> -katta", "-i -> -kunakatta", "-i -> -sô", "-i -> -kunasasô", "-i -> -ku",
                  "+ janai", "+ datta", "+ janakatta", "+ -sô", "+ -janasasô", "+ ni"]
expressions_jap = ["Sumimasen" ]

#all_jap =
for n in transports_jap:
    all_jap.append(n)
for n in colors_jap:
    all_jap.append(n)
for n in animals_jap:
    all_jap.append(n)
for n in weather_jap:
    all_jap.append(n)
for n in clothes_jap:
    all_jap.append(n)
for n in food_jap:
    all_jap.append(n)
for n in house_jap:
    all_jap.append(n)
for n in divers_jap:
    all_jap.append(n)
for n in verbs_jap:
    all_jap.append(n)
for n in adjs_jap:
    all_jap.append(n)


#mots fr
all_fr = []
transports_fr = ["Voiture", "Scooter", "Vélo", "Taxi", "Métro", "Train", "Avion", "Bateau", "Moto", "Bus"]
colors_fr = ["Blanc", "Marron", "Jaune", "Gris", "Bleu", "Noir", "Rouge", "Orange", "Violet", "Vert", "Rose"]
animals_fr = ["Chien", "Canard", "Lapin", "Singe", "Souris", "Cheval", "Ours", "Tigre", "Lion", "Poulet", "Biche", "Cochon", "Chat", "Oiseau", "Renard", "Vache", "Éléphant", "Mouton", "Koala", "Panda" ]
weather_fr = ["Orageux", "Nuageux", "Ensoleillé", "Froid", "Enneigé", "Chaud", "Pluvieux"]
clothes_fr = ["Chaussettes", "Chaussures", "Jeans", "Jupe", "Manteau", "Pantalon", "T-shirt", "Sandales", "Short", "Robe", "Maillot de bain" ]
food_fr = ["Oignon", "Raisin", "Canard (viande)", "Orange", "Pastèque", "Maïs", "Citron", "Brocoli", "Concombre", "Fraise", "Carotte", "Noix de coco", "Pomme de terre", "Bécon", "Lait", "Chou", "Champignon", "Citrouille", "Eau", "Tomate", "Thé", "Boisson énergisante", "Jus", "Agneau (viande)", "Pomme", "Banane", "Cola", "Café", "Poisson (viande)", "Boeuf (viande)", "Poulet (viande)", "Poire", "Porc (viande)", "Ananas"]
house_fr = ["Climatiseur", "Appareil photo", "Calendrier", "Carte de paiement", "Ordinateur", "Chaîne Hi-Fi", "Cuillère", "Canapé", "Table", "Télévision", "Toilettes", "Porte", "Couteau", "Cahier", "Fourchette", "Lit", "PC (Ordi portable)", "Stylo / Stylo-bille", "Radio", "Lampe", "Télécommande"]
divers_fr = ["Amour", "En haut / Haut", "Bleu (adjectif)", "Maison", "Non", "Monde", "Clé", "Rouge (adjectif)", "Sushi (avec respect)", "Clou", "Entrainement", "Pente", "Magasin", "Fleuriste", "Poissonnier", "Neige", "Nuit", "Corps", "Compréhension", "Heure", "Nom d'un Festival", "Air", "Montre / Horloge", "Hier", "Écrivain", "Dessinateur", "Photographe", "Doubleur", "Réalisateur", "Policier", "Animateur pour enfants", "Peintre", "Client", "Cours", "Thé", "Voyage", "Chaîne de montagnes"]
verbs_fr = ["Parler", "Lire", "Jouer / Se divertir", "Recevoir", "Attendre", "Penser", "Tenir / Posséder", "Boire", "Demander", "Mourir", "Se déshabiller", "Dire", "Acheter", "Vivre / Habiter", "Aller", "Monter dans", "Devenir", "Comprendre", "Être / Avoir (objet)", "Enseigner / Dire", "Regarder / Voir", "Manger", "Être / Avoir (être vivant)", "Être capable / Pouvoir", "Rentrer / Retourner", "Arrêter / Abandonner", "Donner", "Venir", "Faire"]
adjs_fr = ["Rapide / Tôt", "Amusant", "Froid", "Incroyable / Impressionnant", "Bon / Bien / Correct", "Cool / Beau-gosse", "Mauvais", "Chaud", "Petit", "Pas cher", "Intéressant", "Difficile", "Douloureux / Aïe", "Cher / Haut", "Effrayant", "Gentil", "Neuf / Nouveau", "Occupé", "Gros / Grand", "Bon (goût)", "Habille / Doué", "Beau / Belle / Jolie", "Aimé / Être aimé", "Détester / Être détester", "Simple / Facile", "Bizarre / Étrange", "Situation difficile", "Sûr / En sécurité", "En forme / En bonne santé", "Pratique"]
conjug_verbs_fr = ["Forme polie (verbes 1er g)", "Forme négative polie (verbes 1er g)", "Forme passé polie (verbes 1er g)", "Forme négative passé polie (verbes 1er g)",
                       "Forme passé (verbes 1er g) -u", "Forme passé (verbes 1er g) -ru", "Forme passé (verbes 1er g) -tsu", "Forme passé (verbes 1er g) -gu", "Forme passé (verbes 1er g) -bu", "Forme passé (verbes 1er g) -mu", "Forme passé (verbes 1er g) -nu", "Forme passé (verbes 1er g) -su", "Forme passé (verbes 1er g) -ku",
                       "Forme négative (verbes 1er g) -u", "Forme négative (verbes 1er g) -_u", "Forme négative (verbes 1er g) -tsu",
                       "Forme négative passé (verbes 1er g) -u", "Forme négative passé (verbes 1er g) -_u", "Forme négative passé (verbes 1er g) -tsu",
                   "Forme polie (verbes 2e g)", "Forme négative polie (verbes 2e g)", "Forme passé polie (verbes 2e g)", "Forme négative passé polie (verbes 2e g)", "Forme passé (verbes 2e g)", "Forme négative (verbes 2e g)", "Forme négative passé (verbes 2e g)",
                   "Forme polie (verbes 3e g)", "Forme négative polie (verbes 3e g)", "Forme passé polie (verbes 3e g)", "Forme négative passé polie (verbes 3e g)", "Forme passé (verbes 3e g)", "Forme négative (verbes 3e g)", "Forme négative passé (verbes 3e g)"]
conjug_adjs_fr = ["Forme négative (adjectifs en i)", "Forme passée (adjectifs en i)", "Forme négative passée (adjectifs en i)", "Forme ''ça a l'air'' (adjectifs en i)", "Forme négative de ''ça a l'air'' (adjectifs en i)", "Transformation en adverbe (adjectifs en i)",
                  "Forme négative (adjectifs en na)", "Forme passée (adjectifs en na)", "Forme négative passée (adjectifs en na)", "Forme ''ça a l'air'' (adjectifs en na)", "Forme négative de ''ça a l'air'' (adjectifs en na)", "Transformation en adverbe (adjectifs en na)"]
expressions_fr = ["Excusez-moi / Pardon pour le dérangement" ]

#all_fr =
for n in transports_fr:
    all_fr.append(n)
for n in colors_fr:
    all_fr.append(n)
for n in animals_fr:
    all_fr.append(n)
for n in weather_fr:
    all_fr.append(n)
for n in clothes_fr:
    all_fr.append(n)
for n in food_fr:
    all_fr.append(n)
for n in house_fr:
    all_fr.append(n)
for n in divers_fr:
    all_fr.append(n)
for n in verbs_fr:
    all_fr.append(n)
for n in adjs_fr:
    all_fr.append(n)


"""
#pour vérifie que les mots correspondent
verif_fr = all_fr
for n in conjug_verbs_fr:
    verif_fr.append(n)
for n in conjug_adjs_fr:
    verif_fr.append(n)
for n in expressions_fr:
    verif_fr.append(n)
verif_jap = all_jap
for n in conjug_verbs_jap:
    verif_jap.append(n)
for n in conjug_adjs_jap:
    verif_jap.append(n)
for n in expressions_jap:
    verif_jap.append(n)


for i in range(0, len(verif_fr)):
    print(verif_fr[i], end=" =========> ")
    print(verif_jap[i])
    #print(verif_jap[i], end=" ::::> ")
    #print(i)
"""


#pour vérifier le nombre d'éléments dans chaque liste
'''
print("\nTransport")
i_fr = len(transports_fr)
i_jap = len(transports_jap)
print(i_fr)
print(i_jap)
print(transports_fr[i_fr - 1])
print(transports_jap[i_jap - 1])

print("\nColors")
i_fr = len(colors_fr)
i_jap = len(colors_jap)
print(i_fr)
print(i_jap)
print(colors_fr[i_fr - 1])
print(colors_jap[i_jap - 1])

print("\nAnimals")
i_fr = len(animals_fr)
i_jap = len(animals_jap)
print(i_fr)
print(i_jap)
print(animals_fr[i_fr - 1])
print(animals_jap[i_jap - 1])

print("\nWeather")
i_fr = len(weather_fr)
i_jap = len(weather_jap)
print(i_fr)
print(i_jap)
print(weather_fr[i_fr - 1])
print(weather_jap[i_jap - 1])

print("\nClothes")
i_fr = len(clothes_fr)
i_jap = len(clothes_jap)
print(i_fr)
print(i_jap)
print(clothes_fr[i_fr - 1])
print(clothes_jap[i_jap - 1])

print("\nFood")
i_fr = len(food_fr)
i_jap = len(food_jap)
print(i_fr)
print(i_jap)
print(food_fr[i_fr - 1])
print(food_jap[i_jap - 1])

print("\nHouse")
i_fr = len(house_fr)
i_jap = len(house_jap)
print(i_fr)
print(i_jap)
print(house_fr[i_fr - 1])
print(house_jap[i_jap - 1])

print("\nDivers")
i_fr = len(divers_fr)
i_jap = len(divers_jap)
print(i_fr)
print(i_jap)
print(divers_fr[i_fr - 1])
print(divers_jap[i_jap - 1])

print("\nVerbs")
i_fr = len(verbs_fr)
i_jap = len(verbs_jap)
print(i_fr)
print(i_jap)
print(verbs_fr[i_fr - 1])
print(verbs_jap[i_jap - 1])

print("\nAdjectives")
i_fr = len(adjs_fr)
i_jap = len(adjs_jap)
print(i_fr)
print(i_jap)
print(adjs_fr[i_fr - 1])
print(adjs_jap[i_jap - 1])

print("\nConjugaison verbs")
i_fr = len(conjug_verbs_fr)
i_jap = len(conjug_verbs_jap)
print(i_fr)
print(i_jap)
print(conjug_verbs_fr[i_fr - 1])
print(conjug_verbs_jap[i_jap - 1])

print("\nConjugaison adjectives")
i_fr = len(conjug_adjs_fr)
i_jap = len(conjug_adjs_jap)
print(i_fr)
print(i_jap)
print(conjug_adjs_fr[i_fr - 1])
print(conjug_adjs_jap[i_jap - 1])

print("\nExpressions")
i_fr = len(expressions_fr)
i_jap = len(expressions_jap)
print(i_fr)
print(i_jap)
print(expressions_fr[i_fr - 1])
print(expressions_jap[i_jap - 1])

print("\nAll")
i_fr = len(all_fr)
i_jap = len(all_jap)
print(i_fr)
print(i_jap)
print(all_fr[i_fr - 1])
print(all_jap[i_jap - 1])
'''
