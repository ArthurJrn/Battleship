#Serveur de communication entre deux clients, doit pouvoir gérer uniquement deux clients en lien avec client.py


import zmq
import time

context=zmq.Context()

server1=context.socket(zmq.ROUTER) #Serveur pour le joueur 1
server1.bind("tcp://*:5559")

joueur1=False
joueur2=False

print("waiting for players...")

addr,empty,msg=server1.recv_multipart() 
message=msg.decode()

addresse_1=addr

server1.send_multipart([addr,b'',b"PLAY"])  
#First client ever who is talking will be P1, server asks him what he wants to do
joueur1=True
print("A new player is connected ! You're player 1.")

mode='0'

while mode=='0' : 
    addr,empty,msg=server1.recv_multipart()
    message=msg.decode()

    if message=='C' : 
        print("Player one will play against the IA")
        print("To start the IA, please open a new terminal and run python3 client_ia.py. Then enter IA as name")
        server1.send_multipart([addr,b'',b"NAME"]) 
        addr,empty,msg=server1.recv_multipart() 
        joueur1_name=msg.decode()
        server1.send_multipart([addr,b'',b'Waiting for IA'])
        print('Player 1 is '+joueur1_name)
        mode='player'

    elif message=='P' : 
        print("Player one will play against another player.")
        server1.send_multipart([addr,b'',b"NAME"])
        addr,empty,msg=server1.recv_multipart() 
        joueur1_name=msg.decode()
        server1.send_multipart([addr,b'',b'waiting for Player 2'])
        print('Player 1 is '+joueur1_name)
        mode='player'

    else : 
        print("Error : wrong answer")
        server1.send_multipart([addr,b'',b"server : please write 'IA' or 'Player'"])

server2=context.socket(zmq.DEALER) #Serveur pour le joueur 2
server2.bind("tcp://*:5560")

if mode=="player" :

    while joueur2==False :  #Waiting for the second player
        addr,empty,msg=server1.recv_multipart()
        message=msg.decode()
        if message=="Hello i want to play" : 
            server1.send_multipart([addr,b'',b"server : there is already a PONE, you will be PTWO"])
            time.sleep(3)#waiting for the client to connect as P2
            server2.send_multipart([b'',b"player two : NAME"])
            empty,msg=server2.recv_multipart()
            joueur2_name=msg.decode()
            message="Debut de la partie"
            msg=message.encode()
            server2.send_multipart([b'',msg])
            joueur2=True
            print("player two is connected, his name is "+joueur2_name)
        
    time.sleep(2)
    server1.send_multipart([addresse_1,b'',b"Debut de la partie"])

    print("establishing connexion between P1 and P2")
    print("connexion established")
    zmq.proxy(server1,server2)        

