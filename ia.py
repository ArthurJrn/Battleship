### PROGRAMME IA POUR LA BATAILLE NAVALE ###

# Adaptation des algorithmes MiniMax et ALphaBeta pour la bataille navale

# Modélisation : - Plateau de jeu : array 10x10
#                - Chaque joueur joue à tour de rôle
#                - 3 niveaux d'IA sont implémentés : facile, moyen et difficile

import numpy as np
from math import *
import random
from IA_aux import *
import zmq 


def IA():

    plateau_IA = np.zeros(10, 10)  # Initialisation des plateaux de jeu
    plateau_adversaire = np.zeros(10, 10)*

# Placement aléatoire des bateaux de l'IA #

    placement_porte_avion(plateau)
    placement_croiseur(plateau)
    placement_contre_torpilleur(plateau)
    placement_sous_marin(plateau)
    placement_torpilleur(plateau)

    difficulte = input("Choisissez votre difficulté : facile, moyen, difficile")

    choix_possibles = ["facile", "moyen", "difficile"]

# Si erreur lors de la saisie de la difficulté #

    if (difficulte) not in choix_possibles:
        print("Erreur lors de la saisie de la difficulté \n")
        IA()

# Difficulté facile : l'IA joue en mode aléatoire #

    elif difficulte == "facile":
        tir_recu = socket.recv()
        tir_recu = tir_recu.decode()
        while(tir_recu != "STOP"):
            (x, y) = convertir_tir_letter_to_number(tir_recu)

            if (plateau[x][y] == 0):
                message = "Raté"
                socket.send(message.encode())
            elif (plateau[x][y] == 1):
                message = touche_coule(plateau, x, y)
                socket.send(message.encode)
            else:
                message = "Vous avez déjà attaqué cette coordonnée"
                socket.send(message.encode)

                (tir_x, tir_y) = tir_random(plateau_adversaire)
                tir_envoye = convertir_tir_number_to_letter(tir_x, tir_y)
                socket.send(tir_envoye.encode())
                message = socket.recv()
                message = message.decode()

                if (message == "Touché"):
                    plateau_adversaire[tir_x][tir_y] = 1
                elif (message == "Raté"):
                    plateau_adversaire[tir_x][tir_y] = -1

# Difficulté moyenne : programmation "en dur" de notre façon de jouer #



