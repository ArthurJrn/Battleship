# Fonctions utiles à l'implémentation de l'IA 

import random
def placement_possible(longueur_bateau, plateau, coord_x, coord_y, direction):
	res = False
	if direction == 0:
		cpt = 0
		for i in range(longueur_bateau):
			if plateau[coord_x][coord_y + i] > 0:
				cpt += 1
		res = (cpt == 0)

	if direction == 1:
		cpt = 0
		for i in range(longueur_bateau):
			if plateau[coord_x][coord_y -i] >0:
				cpt += 1
		res = (cpt == 0)
	if direction == 2:
		cpt = 0
		for i in range(longueur_bateau):
			if plateau[coord_x - i][coord_y] > 0:
				cpt += 1
		res = (cpt == 0)
	if direction == 3:
		cpt = 0
		for i in range(longueur_bateau):
			if plateau[coord_x + i][coord_y] > 0:
				cpt += 1
		res = (cpt == 0)
	return res


def placement_porte_avion(plateau, dico):
	x = random.randint(0,9)
	y = random.randint(0, 9) # Coordonnees de la premiere extremite du batea
	if (y+4 < 10 and placement_possible(5, plateau, x, y, 0)):
		plateau[x][y] = 5
		plateau[x][y+1] = 5
		plateau[x][y+2] = 5
		plateau[x][y+3] = 5
		plateau[x][y+4] = 5
		coord1 = convertir_tir_number_to_letter(x, y)
		coord2 = convertir_tir_number_to_letter(x, y+4)
		dico["porteAvion"] = coord1+coord2
	elif (y-4 >= 0 and placement_possible(5, plateau,x, y, 1)):
		plateau[x][y] = 5
		plateau[x][y-1] = 5
		plateau[x][y-2] = 5
		plateau[x][y-3] = 5
		plateau[x][y-4] = 5
		coord1 = convertir_tir_number_to_letter(x, y-4)
		coord2 = convertir_tir_number_to_letter(x, y)
		dico["porteAvion"] = coord1+coord2
	elif (x-4 >= 0 and placement_possible(5, plateau, x, y, 2)):
		plateau[x][y] = 5
		plateau[x-1][y] = 5
		plateau[x-2][y] = 5
		plateau[x-3][y] = 5
		plateau[x-4][y] = 5
		coord1 = convertir_tir_number_to_letter(x-4, y)
		coord2 = convertir_tir_number_to_letter(x, y)
		dico["porteAvion"] = coord1+coord2
	elif (x+4 >= 0 and placement_possible(5, plateau, x, y, 3)):
		plateau[x][y] = 5
		plateau[x+1][y] = 5
		plateau[x+2][y] = 5
		plateau[x+3][y] = 5
		plateau[x+4][y] = 5
		coord1 = convertir_tir_number_to_letter(x, y)
		coord2 = convertir_tir_number_to_letter(x+4, y)
		dico["porteAvion"] = coord1+coord2
	else:
		placement_porte_avion(plateau, dico)

# Placement du croiseur : 4 cases #

def placement_croiseur(plateau, dico):
	x = random.randint(0,9)
	y = random.randint(0, 9) # Coordonnees de la premiere extremite du bateau #
	if (y+3 < 10 and placement_possible(4, plateau, x, y, 0)):
		plateau[x][y] = 4
		plateau[x][y+1] = 4
		plateau[x][y+2] = 4
		plateau[x][y+3] = 4
		coord1 = convertir_tir_number_to_letter(x, y)
		coord2 = convertir_tir_number_to_letter(x, y+3)
		dico["croiseur"] = coord1+coord2
	elif (y-3 >= 0 and placement_possible(4, plateau,x, y, 1)):
		plateau[x][y] = 4
		plateau[x][y-1] = 4
		plateau[x][y-2] = 4
		plateau[x][y-3] = 4
		coord1 = convertir_tir_number_to_letter(x, y-3)
		coord2 = convertir_tir_number_to_letter(x, y)
		dico["croiseur"] = coord1+coord2
	elif (x-3 >= 0 and placement_possible(4, plateau, x, y, 2)):
		plateau[x][y] = 4
		plateau[x-1][y] = 4
		plateau[x-2][y] = 4
		plateau[x-3][y] = 4
		coord1 = convertir_tir_number_to_letter(x-3, y)
		coord2 = convertir_tir_number_to_letter(x, y)
		dico["croiseur"] = coord1+coord2
	elif (x+3 >= 0 and placement_possible(4, plateau, x, y, 3)):
		plateau[x][y] = 4
		plateau[x+1][y] = 4
		plateau[x+2][y] = 4
		plateau[x+3][y] = 4
		coord1 = convertir_tir_number_to_letter(x, y)
		coord2 = convertir_tir_number_to_letter(x+3, y)
		dico["croiseur"] = coord1+coord2
	else:
		placement_croiseur(plateau, dico)

# Placement du contre_torpilleur : 3 cases #

def placement_contre_torpilleur(plateau, dico):
	x = random.randint(0,9)
	y = random.randint(0, 9) # Coordonnees de la premiere extremite du bateau
	if (y+2 < 10 and placement_possible(3, plateau, x, y, 0)):
		plateau[x][y] = 3
		plateau[x][y+1] = 3
		plateau[x][y+2] = 3
		coord1 = convertir_tir_number_to_letter(x, y)
		coord2 = convertir_tir_number_to_letter(x, y+2)
		dico["contreTorpilleur"] = coord1+coord2
	elif (x-2 >= 0 and placement_possible(3, plateau,x, y, 2)):
		plateau[x][y] = 3
		plateau[x][y-1] = 3
		plateau[x][y-2] = 3
		coord1 = convertir_tir_number_to_letter(x, y-2)
		coord2 = convertir_tir_number_to_letter(x, y)
		dico["contreTorpilleur"] = coord1+coord2
	elif (y-2 >= 0 and placement_possible(3, plateau, x, y, 1)):
		plateau[x][y] = 3
		plateau[x][y-1] = 3
		plateau[x][y-2] = 3
		coord1 = convertir_tir_number_to_letter(x-2, y)
		coord2 = convertir_tir_number_to_letter(x, y)
		dico["contreTorpilleur"] = coord1+coord2
	elif (x+2 >= 0 and placement_possible(3, plateau, x, y, 3)):
		plateau[x][y] = 3
		plateau[x+1][y] = 3
		plateau[x+2][y] = 3
		coord1 = convertir_tir_number_to_letter(x, y)
		coord2 = convertir_tir_number_to_letter(x+2, y)
		dico["contreTorpilleur"] = coord1+coord2
	else:
		placement_contre_torpilleur(plateau, dico)

# Placement du sous-marin : 3 cases #

def placement_sous_marin(plateau, dico):
	x = random.randint(0,9)
	y = random.randint(0, 9) # Coordonnees de la premiere extremite du bateau

	if (x+2 < 10 and placement_possible(3, plateau, x, y, 3)):
		plateau[x][y] = 2
		plateau[x+1][y] = 2
		plateau[x+2][y] = 2
		coord1 = convertir_tir_number_to_letter(x, y)
		coord2 = convertir_tir_number_to_letter(x, y+2)
		dico["sousMarin"] = coord1+coord2
	elif (y-2 >= 0 and placement_possible(3, plateau,x, y, 1)):
		plateau[x][y] = 2
		plateau[x][y-1] = 2
		plateau[x][y-2] = 2
		coord1 = convertir_tir_number_to_letter(x, y-2)
		coord2 = convertir_tir_number_to_letter(x, y)
		dico["sousMarin"] = coord1+coord2
	elif (x-2 >= 0 and placement_possible(3, plateau, x, y, 2)):
		plateau[x][y] = 2
		plateau[x-1][y] = 2
		plateau[x-2][y] = 2
		coord1 = convertir_tir_number_to_letter(x-2, y)
		coord2 = convertir_tir_number_to_letter(x, y)
		dico["sousMarin"] = coord1+coord2
	elif (y+2 < 10 and placement_possible(3, plateau, x, y, 0)):
		plateau[x][y] = 2
		plateau[x][y+1] = 2
		plateau[x][y+2] = 2
		coord1 = convertir_tir_number_to_letter(x, y)
		coord2 = convertir_tir_number_to_letter(x+2, y)
		dico["sousMarin"] = coord1+coord2
	else:
		placement_sous_marin(plateau, dico)

# Placement du torpilleur : 2 cases #

def placement_torpilleur(plateau,dico):
	x = random.randint(0,9)
	y = random.randint(0, 9) # Coordonnees de la premiere extremite du bateau

	if (x-1 >= 0 and placement_possible(2, plateau, x, y, 2)):
		plateau[x][y] = 1
		plateau[x-1][y] = 1
		coord1 = convertir_tir_number_to_letter(x, y)
		coord2 = convertir_tir_number_to_letter(x, y+1)
		dico["torpilleur"] = coord1+coord2
	elif (y-1 >= 0 and placement_possible(2, plateau,x, y, 1)):
		plateau[x][y] = 1
		plateau[x][y-1] = 1
		coord1 = convertir_tir_number_to_letter(x, y-1)
		coord2 = convertir_tir_number_to_letter(x, y)
		dico["torpilleur"] = coord1+coord2
	elif (y+1<10 and placement_possible(2, plateau, x, y, 0)):
		plateau[x][y] = 1
		plateau[x][y+1] = 1
		coord1 = convertir_tir_number_to_letter(x-1, y)
		coord2 = convertir_tir_number_to_letter(x, y)
		dico["torpilleur"] = coord1+coord2
	elif (x+1 >= 0 and placement_possible(2, plateau, x, y, 3)):
		plateau[x][y] = 1
		plateau[x+1][y] = 1
		coord1 = convertir_tir_number_to_letter(x, y)
		coord2 = convertir_tir_number_to_letter(x+1, y)
		dico["torpilleur"] = coord1+coord2
	else:
		placement_torpilleur(plateau, dico)

# Convertisseur de A2 en (0, 1) par exemple #
def convertir_tir_letter_to_number(tir):
	n = len(tir)
	liste = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
	i = 0
	res = 0
	while(tir[0] != liste[i]):
		i += 1
		res += 1

	if n == 2:
		y = int(tir[1])
	else:
		y = 10

	return (y-1,res)
	# Convertisseur de (0, 1) en "B1" par exemple #

def convertir_tir_number_to_letter(x, y):

	liste = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
	car = liste[0]
	for i in range(10):
		if (y == i+1):
			car = liste[i]
	return(car +str(x+1))

# Module de tir aléatoire parmi les cases non déjà tirées #

def tir_random(plateau):
	l = []
	for i in range(10):
		for j in range(10):
			if (plateau[i][j] == 1 or plateau[i][j] == -1):
				l.append((i, j))
	
	test = True
	while(test):
		x = random.randint(0, 9)
		y = random.randint(0, 9)
		if (x, y) not in l:
			test = False
	return(int(x), int(y))

def touche_coule(plateau, x, y, dico_bateaux):
	chaine = "0"
	if plateau[x][y] == 0:
		chaine == "0"
		return(chaine)
	elif (plateau[x][y] >= 1):
		k = plateau[x][y]
		cpt = 0
		cpt2 = 0
		for i in range(10):
			for j in range(10):
				if plateau[i][j] == k:
					cpt += 1
		for i in range(10):
			for j in range(10):
				if plateau[i][j] == 2:
					cpt2 +=1
		if cpt == 1:
			chaine = "2"
			return(chaine)
		elif cpt > 1:
			chaine = "1"
			return(chaine)
		elif cpt2 == 5:
			return("STOP")
		
def maximum_mod(plateau):
	maxi = (0, 0)
	l = []
	for i in range(10):
		for j in range(10):
			(a, b) = maxi
			if plateau[i][j] >= plateau[a][b]:
				maxi = (i, j)
	return maxi

def repondere(plateau, x, y):
	plateau[x][y] +=1
	if x+1 <10 and plateau[x+1][y] > 1:
		plateau[x][y] += 1
	if y-1 > 0 and plateau[x][y-1] > 1:
		plateau[x][y] += 1
	if y+1 < 10 and plateau[x][y+1] >1:
		plateau[x][y] += 1
		
