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
#connecting as player 1
joueur.connect("tcp://localhost:5559")
joueur.send(b'Hello i want to play')
msg=joueur.recv()
message=msg.decode()
print(message)  
if message=="Hello i want to play" : #if the message received is the message you just sent, it means that there are already two players (proxy has already been established)
    port=5561

elif message=="PLAY": #connexion as player 1 accepted 
    print("You are player one. Do you want to play against IA or another player ? Write C or P \n")
    message = input()
    if message == "P":
    	humain = True
    msg = message.encode()
    joueur.send(msg)
    port=5559

else : #connexion as player 1 denied, trying to connect as P2
    print("connecting as Player 2")
    port=5560
    joueur=context.socket(zmq.REP)
    joueur.connect("tcp://localhost:5560")
    msg=joueur.recv()
    message=msg.decode()
    print(message)
    if message=="player two : NAME" : #connexion as P2 accepted
        message=input("Entrez votre nom \n")
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
			message=input("Entrez votre nom \n")
			msg=message.encode()
			joueur.send(msg)
			
			# Le joueur se place en attente d'un joueur 2#
			msg = joueur.recv()
			message=msg.decode()
			print(message)
			if message=='waiting for Player 2' or message == 'Waiting for IA':
				message="i'm waiting"
				msg=message.encode()
				joueur.send(msg)
				msg = joueur.recv()
				message=msg.decode() 
				print(message)
			if message=="Debut de la partie" :
				partie="CURRENT"
				print("BOATS")
				boats = input("Placez vos bateaux! Ex: porteAvion:E10I10,croiseur:J6J8,contreTorpilleur:F3H3,sousMarin:A1B1,torpilleur:A3A6 \n")

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
						print("CELL")
						message = input("Attaquez !\n")
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
						if test_fin(plateau_attaque):
							print("WINNER:joueur1")
							partie="END"
							var = False
							break
						print("Waiting for player 2 to play")
						message = "i'm waiting"
						msg = message.encode()
						joueur.send(msg)
						message = joueur.recv()
						tir_recu = message.decode()
						print(tir_recu)
						(a, b) = convertir_tir_letter_to_number(tir_recu)
						print(a, b)
						res = touche_coule(plateau_joueur, a, b, dico_bateaux)
						print(res)
						plateau_joueur[a][b] = -1
						resultat = res.encode()
						joueur.send(resultat)
						message = joueur.recv()
						msg = message.decode()
        			
 
                


time.sleep(2)
var2 = True
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
        			print("BOATS")
        			boats = input("Placez vos bateaux! Ex: porteAvion:E10I10,croiseur:J6J8,contreTorpilleur:F3H3,sousMarin:A1B1,torpilleur:A3A6 \n")
        			# Placement des bateaux du joueur 2 #
        			dico_bateaux = get_dico(boats)
        			plateau_joueur = get_plateau(dico_bateaux)
        			plateau_attaque = np.zeros((10, 10))
        			# Envoi de la notification de fin de placement #
        			message = "Bateaux joueur 2 placés"
        			msg = message.encode()
        			joueur.send(msg)
        			partie = "CURRENT"
        			print("Le joueur 1 commence")
        			
        			# Debut de la partie #
        			while partie != "END":
        			
        			#Reception du tir adversaire #
        				message = joueur.recv()
        				msg = message.decode()
        			#On rappelle les plateaux de jeu à chaque tour#
        				print("Votre plateau est :", plateau_joueur)
        				print("PLateau d'attaque:", plateau_attaque)
        				(x, y) = convertir_tir_letter_to_number(msg)
        				#Envoi du resultat du tir adverse#
        				res = touche_coule(plateau_joueur, x, y, dico_bateaux)
        				plateau_joueur[x][y] = -1
        				number = res.encode()
        				joueur.send(number)
        				message = joueur.recv()
        				msg = msg.encode()
        				#Le joueur 2 tire à son tour#
        				message = input("CELL \n")
        				msg = message.encode()
        				(a, b) = convertir_tir_letter_to_number(message)
        				joueur.send(msg)
        				#Reception du resultat du tir#
        				res = joueur.recv()
        				resultat = res.decode()
        				if resultat == "1":
        					plateau_attaque[a][b] = 1
        					print("Touché !")
        				elif resultat == "0":
        					plateau_attaque[a][b] = -1
        					print("Raté")
        				elif resultat == "2":
        					plateau_attaque[a][b] = 2
        					print("Coulé")
        				if test_fin(plateau_attaque):
        					print("WINNER:joueur1")
        					partie = "END"
        					var = False
        				#Joueur 2 se place en attente de son tour#
        				print("Waiting for player 1 to play")
        				message = "i'm waiting"
        				msg = message.encode()
        				joueur.send(msg)
        			var = False

elif port==5561 : # Cas d'erreur : trop de joueur sur le serveur#
    print("il y a deja deux joueurs, fin du programme")
