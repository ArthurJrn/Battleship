# Implementation d'un jeu de bataille navale en local #

import numpy as np
from random import *


class Coordonnee:
"""Classe definissant les coordonées des batiments"""
	def __init__(self, hor, vert):
		self.horizontale = horizontale
		self.verticale = verticale
		
	def get_coordonnees(self)
		printf("Coordonnée :")
		chaine = input()
		assert (len(chaine)==2), "Erreur : vous devez rentrer 2 coordonnées : de 1 a 10 horizontalement et de A a J verticalement"
		liste1 = [i for i in range(1, 11)]
		liste2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		assert(chaine[0] in liste2), "Erreur : la coordonnée verticale doit etre comprise entre A et J"
		assert(chaine[1] in liste1), "Erreur : la coordonnée horizontale doit etre comprise entre 1 et 10"
		self.horizontale = int(chaine[1])
		self.verticale = str(chaine[0])

def main():
	grille = np.zeros(10, 10)
	print("Joueur 1 : placez vos bateaux ! Indiquez les coordonnées des extrémités")

	# Placement des bateaux #

	print("Placez le porte-avion : 5 cases")
	porte_avion1_j1 = Coordonnee(A, 0)
	porte_avion2_j1  = Coordonnee(A, 0)
	porte_avion1_j1.get_coordonnees()
	porte_avion2_j1.get_coordonnees()
	
	print("Placez le croiseur : 4 cases")
	croiseur1_j1  = Coordonnee(A, 0)
	croiseur2_j1 = Coordonnee(A, 0)
	croiseur1_j1.get_coordonnees()
	croiseur2_j1.get_coordonnees()
	
	print("Placez le ccontre-torpilleur : 3 cases")
	contre_torpilleur1_j1  = Coordonnee(A, 0)
	contre_torpilleur2_j1  = Coordonnee(A, 0)
	contre_torpilleur1_j1.get_coordonnees()
	contre_torpilleur2_j1.get_coordonnees()
	
	print("Placez le sous-marin : 3 cases")
	sous_marin1_j1  = Coordonnee(A, 0)
	sous_marin2_j1  = Coordonnee(A, 0)
	sous_marin1_j1.get_coordonnees()
	sous_marin2_j1.get_coordonnees()
	
	print("Placez le torpilleur : 2 cases")
	torpilleur1_j1  = Coordonnee(A, 0)
	torpilleur2_j1  = Coordonnee(A, 0)
	torpilleur1_j1.get_coordonnees()
	torpilleur2_j1.get_coordonnees()
	
	print("Joueur 1 : placez vos bateaux !)
	
	print("Placez le porte-avion : 5 cases")
	porte_avion1_j2 = Coordonnee(A, 0)
	porte_avion2_j2  = Coordonnee(A, 0)
	porte_avion1_j2.get_coordonnees()
	porte_avion2_j2.get_coordonnees()
	
	print("Placez le croiseur : 4 cases")
	croiseur1_j2  = Coordonnee(A, 0)
	croiseur2_j2 = Coordonnee(A, 0)
	croiseur1_j2.get_coordonnees()
	croiseur2_j2.get_coordonnees()
	
	print("Placez le ccontre-torpilleur : 3 cases")
	contre_torpilleur1_j2  = Coordonnee(A, 0)
	contre_torpilleur2_j2  = Coordonnee(A, 0)
	contre_torpilleur1_j2.get_coordonnees()
	contre_torpilleur2_j2.get_coordonnees()
	
	print("Placez le sous-marin : 3 cases")
	sous_marin1_j2  = Coordonnee(A, 0)
	sous_marin2_j2  = Coordonnee(A, 0)
	sous_marin1_j2.get_coordonnees()
	sous_marin2_j2.get_coordonnees()
	
	print("Placez le torpilleur : 2 cases")
	torpilleur1_j2  = Coordonnee(A, 0)
	torpilleur2_j2  = Coordonnee(A, 0)
	torpilleur1_j2.get_coordonnees()
	torpilleur2_j2.get_coordonnees()
	
	# Fin du placement des bateaux #
	
	print("C'est parti !")
	joueur = 1
	fin_du_jeu = test_fin_du_jeu(grille)
	while(not(fin_du_jeu))
		print("C'est au joueur %d de jouer" % joueur)
		tir(joueur)
		if test_fin_du_jeu:
			break
			fin_du_jeu = True
			print("Le joueur %d a gagné", % joueur)
		joueur = 2
		tir(joueur)
		
		if test_fin_du_jeu:
			break 
			fin_du_jeu = True
			print("Le joueur %d a gagné !", % joueur)
	print("Fin du jeu !")
			
		
		
		
	 
	
	

