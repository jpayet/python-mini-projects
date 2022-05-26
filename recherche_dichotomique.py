# -*- coding: utf-8 -*-
"""
Created on Tue May 18 11:22:07 2021

@author: jpayet
"""

#
# Fonction de recherche dichotomique sur un tableau
#

def dichotomie(tab,x):
    if tab == []:
        return False,1
    if (x < tab[0]):
        return False,2
    debut = 0
    fin = len(tab)-1
    while debut <= fin:
        m = (debut+fin)//2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m-1
    return False,3

#Tests
print(dichotomie([15,16,18,19,23,24,28,29,31,33],28))

print(dichotomie([15,16,18,19,23,24,28,29,31,33],27))

print(dichotomie([15,16,18,19,23,24,28,29,31,33],1))

print(dichotomie([],28))

#
# Fonctions recherche dichotomique récursives
#

def recherche(tab,v,g,d):
    if g > d:
        return None 
    m = (g+d)//2 
    if tab[m] == v:
        return m
    elif tab[m] < v:
      return recherche(tab, v ,m+1 , d )
    else :
        return recherche(tab, v, g, m-1)
    
tab1 = [1, 3, 5,7,8,9,15,38,79]
print(recherche(tab1, 38, 0, len(tab1)-1))
        

def recherche_dichotomique(tab,v):
    return recherche(tab,v ,0 , len(tab)-1)

print(recherche_dichotomique(tab1, 4))
    