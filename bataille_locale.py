#Implémentation de la bataille navale en local

import numpy as np

listelettre=['A','B','C','D','E','F','G','H','I','J']

def convert(lettre) : #convertit la lettre en coordonnée
    i=0
    for k in listelettre
        if k==lettre :
            return i
        else :
            i=i+1


class coordonnees :
"""Classe définissant les coordonnées dans le jeu"""
    def __init__(self,hor,verti) :
        self.horizontal=hor
        self.vertical=verti


def getcoordonnees()

    hor=input('Entrez la coordonnée horizontale')
    verti=input('Entrez la coordonnée verticale')
    coord=coordonnées()
    coord.horizontal=hor
    coord.vertical=verti
    assert(type(hor)==char,"la coordonnée horizontale est une lettre comprise entre A et J !")
    assert(type(verti)==int,"la coordonnée verticale est un entier comprise entre 1 et 10 !")
    assert(hor in listelettre,"la coordonnée horizontale est une lettre comprise entre A et J !")
    assert(verti<=10,"la coordonnée verticale est un entier comprise entre 1 et 10 !")
    assert(verti>=1,"la coordonnée verticale est un entier comprise entre 1 et 10 !")
        

def main () :
    grille=np.zeros(10,10)

def tir () :
    tir=coordonnees()
    chiffre=input 
