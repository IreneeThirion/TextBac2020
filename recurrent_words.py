#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:47:49 2019

@author: irenee
"""
import numpy as np

# Quelques définitions de paramètres
filename = "/media/irenee/USB-IR/test.txt"
seuil_longueur = 5
seuil_comptage = 20

# Traitement initial du fichier
fichier = open(filename)
lignes = fichier.readlines()
fichier.close()

# Construction de tableaux pour le traitement de texte
texte = ''.join(lignes)
mots = np.array(texte.split())
longueur = np.array([len(mot) for mot in mots])
valide = longueur > seuil_longueur
mots = mots[valide]
      
mots_uniques, counts = np.unique(mots, return_counts=True)

mots_utiles = (mots_uniques[counts > seuil_comptage])
print(mots_utiles)

"""
repetitions = []

for mot in mots:
    dedans = 0
    #on regarde si le mot est déjà dans la listes des mots répétés (repetion)...
    for repet in repetitions:
        # ...si ce mot est déjà dans répétions, on augmente son nombre d’apparitions de 1
        if repet[0] == mot:
            repet[1] += 1
            dedans = 1
            break
    # ... et s'il n'est pas déjà dedans, on le rajoute et on règle son nombre d'apparitions à 1.
    if dedans == 0:
        if len(mot) >= 2:
            if repet[1] >= 2:
                repetitions.append([mot, 1])

print(repetitions)
"""