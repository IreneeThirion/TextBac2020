#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:47:49 2019

@author: irenee
"""

fichier=open("/home/irenee/Documents/test.txt") )
lignes = fichier.readlines()
texte = ''.join(lignes)
mots = texte.split()
repetitions = []
for mot in mots:
    dedans = 0
    for repet in repetitions: 
	#on regarde si le mot est déjà dans la listes des mots répétés (repetion)...
        if repet[0] == mot: 
	    # ...si ce mot est déjà dans répétions, on augmente son nombre d’apparitions de 1
            repet[1] += 1
            dedans = 1
            break
    if dedans == 0: 
	# ... et s'il n'est pas déjà dedans, on le rajoute et on règle son nombre d'apparitions à 1.
        repetitions.append([mot,1])
print(repetitions)
fichier.close()
