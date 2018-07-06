########README#########

Jeu de bataille navale sous python


Nécessite la librairie ZeroMQ

Deux modes de jeu : 

PvP
PvIA

###Comment jouer###

Lancer le fichier serveur.py

Lancer le fichier client.py
Choisir le mode (C : vs IA // P : vs Player) dans le terminal
Rentrer son pseudo dans le terminal

Si vous jouez contre l'IA, la partie commence

Si vous jouez contre un autre joueur, celui-ci doit lancer le fichier client.py, puis rentrer son nom dans le terminal. La partie commence après que le joueur 2 ait rentré son nom.

L'IA possède deux niveaux de difficulté. Le premier est un mode aléatoire, le second proppose (ou du moins tente de porposer) un méthode de pondération du plateau de jeu selon la probabilité d'un bateau soit sur la case. Nous avons fait ce choix pour voir si cette méthode était efficace, ainsi que pour eviter de coder "en dur" notre facon de jouer à la bataille navale.

Pour utiliser les IA, il faut lancer le serveur comme en PvP mais utiliser dans les deux autres terminaux les fichiers clients associés aux deux serveurs. L'IA est alors un joueur dont il faut rentrer le nom en debut de partie !




