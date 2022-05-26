# -*- coding: utf-8 -*-
"""
Created on Wed May 26 08:03:29 2021

@author: jpayet
"""

#-----------------------#
# Les listes de données #
#-----------------------#

# Fonction de création d'une liste de type File 
class File:
    '''Classe file'''
    
    def __init__(self):
        '''Constructeur de la classe'''
        self.__file = []
        
    def enfiler(self,x):
        '''enfile l'élément x en queue de la file'''
        self.__file.append(x)
            
    def defiler(self):
        '''défile l'elément de tete de la file et le retrourne'''
        return self. __file.pop(0)
            
    def est_vide(self):
        '''test si la file est vide'''
        if len(self.__file) != 0:
            return False
        else: 
            return True

# Fonction de création d'une liste de type Pile   
class Pile:
    '''Classe Pile'''
    def __init__(self):
        self.contenu = []

    def empiler(self, valeur):
        self.contenu.append(valeur)
        
    def depiler(self):
        return self.contenu.pop()
        
    def est_vide(self):
        if len(self.contenu) == 0:
            return True
        else:
            return False
        
    def getPile(self):
        return(self.element)

# Fonction qui vérifie s'il y a un cycle dans la Pile  
    def PresenceCycle(self, cle_depart, lst=[]):
        pile = Pile()
        S = self.GetSommet(cle_depart)
        pile.empiler(S)
        
        while pile.est_Vide()==False:
            Som = pile.depiler()
            for i in self.ListeAdj[Som.cle]:
                Sv = self.GetSommet(i)
                if Sv.couleur == 'Blanc':
                    pile.empiler(Sv)
                    
                if Som.couleur == 'Noir':
                    return True 
                else:
                    Som.couleur = 'Noir'
        return False

#-----------------------#
#      Les Graphes      #
#-----------------------#

# Fonction de création des sommets d'un graphe
class Sommet:
    '''classe sommet'''
    def __init__(self, cle):
        '''constructeur de la classe'''
        self.cle = cle
        self.couleur = 'Blanc'

# Fonction de création du graphe
class Graphe:
    '''classe Graphe à l'aide de la liste d'adjacence'''
    
    def __init__(self):
        '''constructeur de la classe'''
        self.ListeS = []
        #créer un dictionnaire pr stocker la liste d'adjacence
        self.ListeAdj = {}
        
    def AjouterSommet(self, s):
        '''Ajoute s à la liste des sommets et prépare la liste d'adj
        vide pour ce sommet'''
        self.ListeS.append(s)
        self.ListeAdj[s.cle] = []
        
    def ajouterArete(self, cle1, cle2):
        '''Ajoute le sommmet de cle cle2 à la liste d'adj de cle cle1'''
        self.ListeAdj[cle1].append(cle2)
        
    def GetSommet(self, cle):
        '''retourne le smmet de clé cle'''
        for i in range (len(self.ListeS)):
            if self.ListeS[i].cle == cle:
                return self.ListeS[i]
            
    def ResetCouleur(self):
        '''reinitialisate tous les sommets du graphe a la couleur blanche'''
        for i in range (len(self.ListeS)):
            self.ListeS[i].couleur = 'Blanc'
        
# Fonction pour parcourir en largeur le graphe
    def ParcoursLargeur(self,cle):
        Liste_resultat = []
        
        file = File()
        S = self.GetSommet(cle)
        file.enfiler(S)
        
        while file.est_vide() == False:
            S = file.defiler()
            if S.couleur == 'Blanc':
                Liste_resultat.append(S.cle)
                S.couleur = 'Noir'
                
        for i in self.ListeAdj[S.cle]:
            som = self.GetSommet(i)
            if som.couleur == 'Blanc':
                Liste_resultat.append(som.cle)
                file.enfiler(som)
                som.couleur = 'Noir'
        return Liste_resultat
    
# Fonction qui parcoure le graphe en profondeur
        def ParcoursProfondeur(self, lst, graphe , cle):
            S = graphe.GetSommet(cle)
            S.couleur = "Noir"
            lst.append(S.cle)
        
            for i in graphe.ListeAdj[S.cle]:
                Som = graphe.GetSommet(i)
                if Som.couleur == 'Blanc':
                    self.ParcoursProfondeur(lst, graphe, Som.cle)

#Fonction qui retourne le chemin des deux valeurs recherchées dans le graphe
    def RechercheChaine(self, graphe ,cle_depart, cle_arrivee, lst_chemin = []):
        lst_chemin += [cle_depart]
        if cle_depart == cle_arrivee:
            return lst_chemin
        
        S = graphe.GetSommet(cle_depart)
        for i in graphe.ListeAdj[S.cle]:
            Sv = graphe.GetSommet(i)
            if Sv.cle not in lst_chemin:
                Newchaine = self.RechercheChaine(graphe, Sv.cle, cle_arrivee, lst_chemin)
                if len(Newchaine) != 0:
                    return Newchaine
        return []

#Création du graphe
g = Graphe()
g.AjouterSommet('A')
g.AjouterSommet('B')
g.AjouterSommet('C')
g.AjouterSommet('D')
g.AjouterSommet('E')
g.AjouterSommet('F')
g.AjouterSommet('G')
g.AjouterSommet('H')
g.AjouterSommet('I')
g.ajouterArete('A', 'B')
g.ajouterArete('A', 'F')
g.ajouterArete('B', 'A')
g.ajouterArete('B', 'C')
g.ajouterArete('B', 'D')
g.ajouterArete('B', 'G')
g.ajouterArete('C', 'B')
g.ajouterArete('C', 'E')
g.ajouterArete('D', 'B')
g.ajouterArete('D', 'I')
g.ajouterArete('E', 'C')
g.ajouterArete('E', 'I')
g.ajouterArete('F', 'A')
g.ajouterArete('F', 'G')
g.ajouterArete('F', 'H')
g.ajouterArete('G', 'B')
g.ajouterArete('G', 'F')
g.ajouterArete('G', 'I')
g.ajouterArete('H', 'F')
g.ajouterArete('H', 'I')
g.ajouterArete('I', 'D')
g.ajouterArete('I', 'E')
g.ajouterArete('I', 'G')
g.ajouterArete('I', 'H')

#Appel des fonctions
print(g.ListeAdj)
print(g.ParcoursLargeur('B'))
print(g.ParcoursProfondeur([],g,'C'))

print(g.PresenceCycle('A'))
print(g.RechercheChaine(g,'E','H'))
