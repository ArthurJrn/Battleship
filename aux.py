# FONCTIONS AUXILIAIRES #

import numpy as np
from IA_aux import *

def next_virgule(chaine, i):
	n = len(chaine)
	j = 0
	while (i+j < n and chaine[i+j] != ","):
		j+=1
	return(i+j)
	
def get_coord(chaine):
	liste = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
	i = 1
	while (chaine[i] not in liste and i<3):
		i += 1
	return (chaine[0:i], chaine[i::])

def get_dico(chaine):
	""" Transforme la chaine de caracteres des coordonnées des bateaux en un dictionnaire"""
	
	n =  len(chaine)
	dico = dict()
	i = 0
	l = []
	while i<n:
		if chaine[i] == ":":
			j = next_virgule(chaine, i)
			l = l+ [chaine[i+1:j]]
		i += 1
	dico["porteAvion"] = l[0]
	dico["croiseur"] = l[1]
	dico["contreTorpilleur"] = l[2]
	dico["sousMarin"] = l[3]
	dico["torpilleur"] = l[4]
	print(dico)
	return(dico)
			
def get_plateau(dico):
	plateau = np.zeros((10, 10))
	for bateau in dico.values():
		(bateau1, bateau2) = get_coord(bateau)
		(x1, y1) = convertir_tir_letter_to_number(bateau1)
		(x2, y2) = convertir_tir_letter_to_number(bateau2)
		if x1 == x2:
			j = 0
			y = max(y1, y2)
			y_min = min(y1, y2)
			while (y_min+j <= y):
				if bateau == dico["porteAvion"]:
					plateau[x2][y_min+j] = 5
					j += 1
				elif bateau == dico["croiseur"]:
					plateau[x2][y_min+j] = 4
					j += 1
				elif bateau == dico["torpilleur"]:
					plateau[x2][y_min+j] = 3
					j+=1
				elif bateau == dico["contreTorpilleur"]:
					plateau[x2][y_min+j] = 2
					j+=1
				else:
					plateau[x2][y_min+j] = 1
					j+=1
		
		else:
			i = 0
			x = max(x1, x2)
			x_min = min(x1, x2)
			while (x_min+i <= x):
				if bateau == dico["porteAvion"]:
					plateau[x_min+i][y2] == 5
					i += 1
				elif bateau == dico["croiseur"]:
					plateau[x_min+i][y2] = 4
					i+=1
				elif bateau == dico["torpilleur"]:
					plateau[x_min+i][y2] = 3
					print(x_min+i)
					i+=1
				elif bateau == dico["contreTorpilleur"]:
					plateau[x_min+i][y2] = 2
					i+=1
				else:
					plateau[x_min+i][y2] = 1
					i+=1
	print(plateau)
	return(plateau)
	
def cree_mat():
	mat = np.zeros((10, 10))
	for i in range(10):
		for j in range(10):
			mat[i][j] = 1
	return mat
	
def test_fin(plateau):
	cpt = 0
	for i in range(10):
		for j in range(10):
			if plateau[i][j] ==2:
				cpt += 1
	return (cpt == 5)
			
				
			
		
	
