# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:28:20 2018

@author: rambaud5u
"""

def val(mot):
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    somme = 0
    for lettre in mot:
        indice=1
        for j in alphabet:
            if lettre == j:
                somme += indice
            else:
                indice += 1
    return somme
        
print(val('AB'))
    


f = open('p022_names.txt', 'r')
def solve(f):
    L = []
    for ligne in f:
        L += ligne
    L = L[0].split(',')
    L = sorted(L,key=str.lower)
    

    

    
    




