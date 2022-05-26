# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 08:30:58 2021

@author: jpayet
"""

# 
# Projet création d'un arbre : Crétion de l'arbre - Test sur les noeuds (feuille) - Récupération de ses noeuds enfants ou parents 
#

def creation_arbre(r, hauteur): #fonction pour créer l'arbre. Elle prend 2 arguments: la racine "r" et la hauteur
    Arbre = [r]+[None for i in range(2**(hauteur+1)-2)] # on créer une liste avec la racine de l'arbre puis on la rempli avec des "None" selon sa hauteur
    return Arbre #on retourne l'arbre

def insertion_noeud(arbre,n,fg,fd): #fonction pour insérer les noeuds et leurs enfants dans l'abre. Elle prend 4 arguments: l'arbre, un noeud , son enfant gauche et son enfant droit
    indice = arbre.index(n) #on défini l'indice pour pouvoir par la suite travailler avec 
    arbre[2*indice+1] = fg #on donne la position de l'enfant gauche dans le tableau
    arbre[2*indice+2] = fd #on donne la position de l'enfant droit dans le tableau
    
arbre_1 = creation_arbre("10", 5) #on créer l'arbre "arbre_1" en insérant sa racine et en donnant sa hauteur

#On insère tous les noeuds de cet arbre 
insertion_noeud(arbre_1,"10","20","30")
insertion_noeud(arbre_1,"20","40","50")
insertion_noeud(arbre_1,"30","60","70")
insertion_noeud(arbre_1,"40", "None", "80")
insertion_noeud(arbre_1,"50","90","100")
insertion_noeud(arbre_1,"60","110","None")
insertion_noeud(arbre_1,"70","None","None")
insertion_noeud(arbre_1,"80","None","None")
insertion_noeud(arbre_1,"90","None","None")
insertion_noeud(arbre_1,"100","120","None")
insertion_noeud(arbre_1,"110","None","None")
insertion_noeud(arbre_1,"120","None","None")

print(arbre_1)#on affiche l'arbre 

def est_feuille(arbre,noeud): #fonction pour savoir si le noeud est une feuille
    if noeud in arbre: #on vérifie d'abord si le noeud entré est dans l'arbre
        indice = arbre.index(noeud) #on défini l'indice
        if arbre[2*indice+1] == "None" and arbre[2*indice+2] == "None": #On vérifie si l'enfant droit et l'enfant gauche sont nul
            return True # la fonction renvoie vrai car les deux sont nul ainsi le noeud est une feuille
        else:
            return False #elle renvoie faux dans le cas échéant
  
def frere(arbre, noeud): #fonction pour savoir si le noeud à un frère 
    if noeud in arbre: #on vérifie  si le noeud entré est dans l'arbre
        indice = arbre.index(noeud) #on défini l'indice à partir du noeud
        if indice % 2 == 0: #condition pour trouver le parent du noeud
            parent = arbre[(indice - 2)//2] #si le résultat de la division est égale à 0 alors son parent se trouve à l'indice arbre[(indice - 2)//2] et on l'assigne
        else:
            parent = arbre[(indice - 1)//2] #sinon le parent se trouve à l'indice arbre[(indice - 1)//2], on l'assigne 
        indice = arbre.index(parent) #on change l'indice, on le met à partir du parent pour pouvoir avoir ses enfants par la suite 
        if arbre[2*indice+1] != "None" and arbre[2*indice+1] != noeud: #si son premier enfant n'est pas nul et n'est pas égal au noeud lui-même alors...
            return True #...le noeud à un frère(gauche), la fonction renvoie donc vrai
        elif arbre[2*indice+2] != "None" and arbre[2*indice+2] != noeud: #si son deuxième enfant n'est pas nul et n'est pas égal au noeud lui-même alors...
            return True #...le noeud à un frère(droit), la fonction renvoie donc vrai
        else: #les deux conditions prcédentes ne sont pas respectée, donc...
            return False #...la fonction renvoie faux car le neoud n'a pas de frère
 
def enfants(arbre,noeud): #fonction pour savoir si un noeud à des enfants
    if noeud in arbre: #on vérifie  si le noeud entré est dans l'arbre
        indice = arbre.index(noeud) #on défini l'indice    
        n = int(input("Voulez-vous savoir l'enfant gauche ? (dans ce cas tapez 1) ou bien l'enfant droit ? (dans ce cas tapez 2). Si vous voulez les deux tapez 3: "))#on propose un choix à l'utilisateur
        assert n==1 or n==2 or n==3, "veuillez entrer 1, 2 ou 3" #on vérifie que l'utilisateur à bien entré une des trois propositions et non autre chose; dans ce cas un message d'erreur lui est envoyé
        if n == 1: #si l'utilisateur à tapé 1 alors faire le programme suivant
            if arbre[2*indice+1] != "None": #on regarde si l'enfant si l'enfant gauche n'est pas nul
                print("L'enfant gauche du noeud" ,noeud, "est" ,arbre[2*indice+1],) #si c'est la cas, ce message donnnant l'enfant gauche du noeud va être affiché
            else: #dans le cas contraire 
                print("Le noeud" ,noeud, "n'a pas d'enfant gauche") #ce message ci
        elif n==2:  #si l'utilisateur à tapé 2 alors faire le programme suivant
             if arbre[2*indice+2] != "None": #on regarde si l'enfant si l'enfant droit n'est pas nul
                 print("L'enfant droit du noeud" ,noeud, "est" ,arbre[2*indice+2],) #si c'est la cas, ce message donnnant l'enfant droit du noeud va être affiché
             else: #la conditin précédente n'est pas bonne donc...
                 print("Le noeud" ,noeud, "n'a pas d'enfant droit") #...le noeud n'a as d'enfant droit, ce message va alors être affiché
        else: #Cette partie est juste la compilation des deux parties précédentes
            if arbre[2*indice+1] != "None" and arbre[2*indice+2] != "None":
                print("L'enfant gauche du noeud", noeud, "est" ,arbre[2*indice+1], "et son enfant droit est" , arbre[2*indice+2],)
            elif arbre[2*indice+1] != "None":
                print("L'enfant gauche du noeud" ,noeud, "est" ,arbre[2*indice+1], "et il ne possède pas d'enfant droit")
            elif arbre[2*indice+2] != "None":
                print("L'enfant droit du noeud" ,noeud, "est" , arbre[2*indice+2] , "et il ne possède pas d'enfant gauche")
            else:
                print("Le noeud" , noeud, "ne possède aucun enfants")
     
def parent(arbre,noeud): #fonction qui renvoie le parent d'un noeud
    assert noeud in arbre, "Le noeud entré n'est pas dans l'arbre" #on vérifie que l'utilisateur à bien entré un noeud dans l'arbre, un message d'erreur est envoyé si ce n'est pas le cas.
    indice = arbre.index(noeud) #on défini l'indice à partir du noeud
    if indice % 2 == 0: #si le reste de la division euclidienne de l'indice par 2 est égal à 0 alors cela signifie que...
        print("le parent du noeud", noeud,"est" ,arbre[(indice - 2)//2],) #...son parent se trouve à arbre[(indice - 2)//2], un message est donc affiché
    else: #dans le cas contraire
        print("le parent du noeud", noeud,"est" ,arbre[(indice - 1)//2],)#...son parent se trouve à arbre[(indice - 1)//2], un message est donc affiché

    