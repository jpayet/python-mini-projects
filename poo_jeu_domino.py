# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:23:58 2020

@author: jpayet
"""

#
# Projet POO : Création d'un jeu de domino
#
    
class Domino:
    '''Classe domino'''
    def __init__(self,ptg,ptd):  # méthode constructeur avec deux attributs cote_gauche et cote_droit
        self.cote_gauche = ptg
        self.cote_droit = ptd
    
    def afficherDomino(self):   # méthode pour afficher les deux côtés d'un domino
        if self.estDouble():
            print("-----")
            print("|",self.cote_gauche,"|")
            print("|---|")
            print("|",self.cote_droit,"|")
            print(" -----")
        else:
            print("---------")
            print("|",self.cote_gauche,"|",self.cote_droit,"|")
            print("--------")
            
    def nbPoints(self):  # méthode qui retourne la somme des points présents sur les deux côtés
        return self.cote_gauche + self.cote_droit
    
    def estBlanc(self):   # méthode qui teste si le domino possède un blanc : 0 sur l'un des deux côtés
        if self.cote_gauche == 0 or self.cote_droit == 0:
            return True
        else:
            return False
    
    def estDouble(self):   # méthode qui teste si le domino est double : même nombre sur les deux côtés
        if self.cote_gauche == self.cote_droit:
            return True
        else:
            return False
    
import random         
class JeuDeDomino:
    '''Classe JeuDeDomino'''
    def creerJeu(self):
        jeu=[]
        for i in range (7):
            for j in range (i+1):
                jeu.append(Domino(i,j))
        return jeu
    
    def __init__(self):
        self.Jeu = self.creerJeu()
        self.NbPieces = 28
    
    def melanger(self):
        random.shuffle(self.Jeu)
        
    def afficherJeu(self):
        for element in self.Jeu:
            element.afficherDomino()
    
    def distribuerJeu(self,nb_joueur):
        jeu_joueur = []
        if nb_joueur == 2:
            nb_domino = 7
        else:
            nb_domino = 6
        for i in range(nb_domino):
            dom = self.Jeu.pop(0)
            jeu_joueur.append(dom)
            self.NbPieces = self.NbPieces - 1
        return jeu_joueur
