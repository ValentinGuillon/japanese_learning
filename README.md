# programs_for_japanese
This repository contains interactive programs used to my japanese's learning.<br><br>

Ne sachant pas comment faire pour lancer un prog directement ici, ou même si c'est possible,<br>pour tester les programmes, il faudra les copier/coller<br>
IMPORTANT:<br>Si vous le faites, il vous faudra obligatoirement les modules "characters_jap" et "list_jap_fr", mais aussi "romaji_to_kana"<br><br>


L'affichage des programmes est adapté au format des téléphones.<br>

Tous les programmes se "rejoue" instantanément.<br>
Par exemple, le prog' "numbers" va afficher un nombre en Japonais, puis en français, et rebelotte.<br>
La plupart des programmes permettent le choix de la langue.<br>
Par exemple, en choississant le Français, le programme affichera d'abord les mots en Français, puis en Japonais.<br>
Tous programmes ont un mode "view" et/ou un mode "game".<br>
"view" permet au joueur de n'avoir quasi rien à faire, hormis appuyer sur Entrée pour passer à la suite du programme.<br>
"game" demande au joueur d'écrire une réponse.


Comme c'est un peu le bazar dans le rangement des programmes,<br>voici quelques indications pour ceux-ci :<br>
<ul>
  <b>Les modules</b>
  <ul>
    <li><em>module_characters_jap.py</em><br>Listes des charactères, en romaji et en hiragana</li>
    <li><em>module_list_jap_fr.py</em><br> Listes de mots, en Français et en Japonais (romaji)</li>
  </ul>
</ul>

<br>
<ul>
  <b>Les outils</b><br>
  <ul>
    <li><em>romaji_to_kana.py</em><br>Ce programme est un "traducteur". Vous rentrez un mot ou une phrase en romaji, et le programme vous la ressort en kana (attention cependant, il n'est pas entièrement fiable dès qu'il s'agit de charactères complexes ou de double voyelles/consonnes)</li>
  </ul>
</ul>

<br>
<ul>
  <b>Les "jeux"</b><br>
  <ul>
    "view" & "game" modes
    <li><em>jap_to_fr.py</em><br>Le programme vous donne un mot. À vous de le traduire</li>
    <li><em>numbers.py</em><br>Affiche un nombre entre 0 et 999. À vous de le deviner</li>
    <br><br>"game" mode only
    <li><em>guess_char_game.py</em><br>Affiche un nombre, à choisir, de kanas</li>
    <br><br>"view" mode only
    <li><em>kana_reconizing.py</em><br>Affiche un kana. Vous pouvez choisir "tous" ou un groupe, Par exemple, le groupe "k" contient les charactères "ka, ki, ku, ke, ko, ga, gi, gu, ge, go"</li>
    <li><em>kanas_generator.py</em><br>Affiche un nombre, à choisir, de kanas</li>
    <li><em>conversations.py</em><br>Simule une conversation avec l'ordinateur. Vous devez decider, dans un premier temps, si vous posez la question ou non. Si oui, vous devez choisir le sujet de la question. Quand vous donnez la réplique, les différentes manières d'écrire la question/réponses sont affichées</li>
  </ul>
</ul>
