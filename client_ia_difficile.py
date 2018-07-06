##Communiquer entre deux clients via un serveur, en gerant deux clients au maximum

from IA_aux import *
from aux import *
import numpy as np
import zmq
import time
from random import *
port=5559
context = zmq.Context()
joueur=context.socket(zmq.REQ)
humain = True
var = True
var2 = True
#connecting as player 1
joueur.connect("tcp://localhost:5559")
joueur.send(b'Hello i want to play')
msg=joueur.recv()
message=msg.decode()
print(message)  
if message=="Hello i want to play" : #if the message received is the message you just sent, it means that there are already two players (proxy has already been established)
    port=5561

elif message=="PLAY": #connexion as player 1 accepted 
    print("You are player one. Do you want to play against IA or another player ? Write C or P")
    message = input()
    if message == "P":
    	humain = True
    msg = message.encode()
    joueur.send(msg)
    port=5559

else : #connexion as player 1 denied, trying to connect as P2
    print("IA is connecting")
    port=5560
    joueur=context.socket(zmq.REP)
    joueur.connect("tcp://localhost:5560")
    msg=joueur.recv()
    message=msg.decode()
    print(message)
    if message=="player two : NAME" : #connexion as P2 accepted
        message=input()
        msg=message.encode()
        joueur.send(msg) 
        port=5560
        
    else : #connexion as P2 denied, there are already two players
        print("Already two players")
        port=5561

	
if port==5559 :
	while var:
		message = joueur.recv()
		msg = message.decode()
		print(msg)
		if msg == "NAME":
			message=input()
			msg=message.encode()
			joueur.send(msg)
			
			# Le joueur se place en attente d'un joueur 2#
			msg = joueur.recv()
			message=msg.decode()
			print(message)
			if message=='waiting for Player 2' or message == "Waiting for IA" :
				message="i'm waiting"
				msg=message.encode()
				joueur.send(msg)
				msg = joueur.recv()
				message=msg.decode() 
				print(message)
			if message=="Debut de la partie" :
				partie="CURRENT"
				print("BOATS")
				boats = input("Placez vos bateaux! Ex: porteAvion:E10J10,croiseur:J6J8,contre_torpilleur:F3H3,sousMarin:A1B1,torpilleur:A3A6 \n")

				dico_bateaux = get_dico(boats)
				plateau_joueur = get_plateau(dico_bateaux)
				plateau_attaque = np.zeros((10, 10))
				message = "Bateaux joueur 1 placés"
				msg = message.encode()
				joueur.send(msg)
				message = joueur.recv()
				msg = message.decode()
				if msg == "Bateaux joueur 2 placés":
					print("Le joueur 1 commence")
					while partie != "END" :
						print("Votre plateau est:", plateau_joueur)
						print("Le plateau d'attaque est :", plateau_attaque)
						message = input("CELL \n")
						msg = message.encode() 
						(x, y) = convertir_tir_letter_to_number(message)
						joueur.send(msg)
						number = joueur.recv()
						nb = number.decode()
						if (nb == "1"):
							plateau_attaque[x][y] = 1
							print("TOUCHE\n")
						elif (nb == "2"):
							plateau_attaque[x][y] = 2
							print("COULE\n")
						elif nb == "0":
							plateau_attaque[x][y] = -1
							print("RATE\n")
						else:
							partie = "END"
							print("Vous avez gagné !")
							break
						time.sleep(2)
						print("Waiting for player 2 to play")
						message = "i'm waiting"
						msg = message.encode()
						joueur.send(msg)
						message = joueur.recv()
						tir_recu = message.decode()
						(a, b) = convertir_tir_letter_to_number(tir_recu)
						res = touche_coule(plateau_joueur, a, b, dico_bateaux)
						print(1)
						plateau_joueur[a][b] = -1
						if res == "0":
							print("L'IA a raté !")
						elif res == "1":
							print("L'IA a touché un de vos bateaux !")
						elif res == "2":
							print("L'IA a coulé un de vos bateaux !")
						else:
							partie = "END"
							print("L'IA a gagné !")
							break
						resultat = res.encode()
						joueur.send(resultat)
						message = joueur.recv()
						msg = message.decode()
					var = False

time.sleep(2)

if port==5560 : 
    while var2:
    	if humain: 
        	msg = joueur.recv()
        	message=msg.decode()

			# Gestion d'un eventuel troisieme joueur # 
        	if message=="Hello i want to play" : 
        		print('third player')
        		message=="Warning, third player"
        		print(message)
        		msg=message.encode()
        		joueur.send(msg) 
        	elif message=="Debut de la partie" : 
        		print(message)
        		print("le joueur 1 place ses bateaux")
        		message = "waiting for p1"
        		msg = message.encode()
        		joueur.send(msg)
        		message = joueur.recv()
        		msg = message.decode()
        		print(msg)
        		if msg == "Bateaux joueur 1 placés":
        			print("L'IA place ses bateaux aléatoirement")
        			# Placement aléatoire des bateaux de l'IA#
        			dico_bateaux = dict()
        			plateau_IA = np.zeros((10, 10))
        			placement_porte_avion(plateau_IA, dico_bateaux)
        			placement_croiseur(plateau_IA, dico_bateaux)
        			placement_contre_torpilleur(plateau_IA, dico_bateaux)
        			placement_sous_marin(plateau_IA, dico_bateaux)
        			placement_torpilleur(plateau_IA, dico_bateaux)
        			plateau_attaque = np.zeros((10, 10))
        			# Envoi de la notification de fin de placement #
        			message = "Bateaux joueur 2 placés"
        			msg = message.encode()
        			joueur.send(msg)
        			partie = "CURRENT"
        			print("Le joueur 1 commence")
        			directions_possibles = []
        			strategie = "Pas de direction favorisée"
        			k = 0
        			tir_precedent = (0, 0)
        			# Debut de la partie #
        			tir_alea = True
        			while partie != "END":
        				plateau_pondere= cree_mat()        			
        				print("Votre plateau est :", plateau_IA)
        				print("Plateau pondere", plateau_pondere)
        			#Reception du tir adversaire #
        				message = joueur.recv()
        				msg = message.decode()
        			#On rappelle les plateaux de jeu à chaque tour#

        				(x, y) = convertir_tir_letter_to_number(msg)
        				#Envoi du resultat du tir adverse#
        				res = touche_coule(plateau_IA, x, y, dico_bateaux)
        				plateau_IA[x][y] = -1
        				number = res.encode()
        				joueur.send(number)
        				message = joueur.recv()
        				msg = msg.encode()
        				#En mode difficile, l'IA avec une stratégie#

        				if tir_alea:
        					(x, y) = tir_random(plateau_attaque)
        					message = convertir_tir_number_to_letter(x, y)
        					msg = message.encode()
        					joueur.send(msg)
        					res = joueur.recv()
        					resultat = res.decode()
        					if resultat == "1":
        						print("Touché !")
        						tir_alea = False
        						plateau_attaque[x][y] = 1
        						plateau_pondere[x][y] = 100
        						if x-1 >=0 and plateau_pondere[x-1][y] < 0:
        							plateau_pondere[x-1][y] *= 1.2
        							repondere(x-1, y)
        						if x+1<10 and plateau_pondere[x+1][y] <0:
        							plateau_pondere[x-1][y] *= 1.3
        							repondere(x-1, y)
        						if y-1 >=0 and plateau_pondere[x][y-1] <0:
        							plateau_pondere[x-1][y-1] *= 1.4
        							repondere(x-1, y)
        						if y+2 <10 and plateau_pondere[x][y+1] <0:
        							plateau_pondere[x][y+1] *= 1.5
        							repondere(x-1, y)
        					elif resultat == "0":
        						print("Raté")
        						plateau_attaque[x][y] = -1
        						plateau_pondere[x][y] = -1
        					elif resultat == "2":
        						print("Coulé")
        						tir_alea = False
        						plateau_pondere[x][y] = 100
        						plateau_attaque[x][y] = 1
        						tir_alea
        				else:
        					(x, y) = maximum_mod(plateau_pondere)
        					print(x, y)
        					message = convertir_tir_number_to_letter(x, y)
        					msg = message.encode()
        					joueur.send(msg)
        					res = joueur.recv()
        					resultat = res.decode()
        					if resultat == "0":
        						print("Raté")
        						plateau_attaque[x][y] = -1
        						plateau_pondere[x][y] = -1
        					elif resultat == "1":
        						print("Touché")
        						if x-1 >=0 and plateau_pondere[x-1][y] < 0:
        							plateau_pondere[x-1][y] *= 1.2
        							repondere(x-1, y)
        						if x+1<10 and plateau_pondere[x+1][y] <0:
        							plateau_pondere[x-1][y] *= 1.3
        							repondere(x-1, y)
        						if y-1 >=0 and plateau_pondere[x][y-1] <0:
        							plateau_pondere[x-1][y-1] *= 1.4
        							repondere(x-1, y)
        						if y+2 <10 and plateau_pondere[x][y+1] <0:
        							plateau_pondere[x][y+1] *= 1.5
        							repondere(x-1, y)        						
        						plateau_attaque[x][y] = 100
        						plateau_pondere[x][y] = 100
        					elif resultat == "2":
        						print("Coulé")
        						plateau_attaque[x][y] = 100
        						plateau_pondere[x][y] = 100
        				message = "i'm waiting"
        				msg = message.encode()
        				joueur.send(msg)
        					
        				
        				
elif port==5561 : # Cas d'erreur : trop de joueur sur le serveur#
    print("Il y a deja deux joueurs, fin du programme")
