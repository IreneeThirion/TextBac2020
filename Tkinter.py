#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:59:14 2019

@author: irenee.thirion
"""

from tkinter import *

# Contenu de la fenêtre où on entre le texte
def FaireapparaitreZonedetexte():
    top=Toplevel(fenetre)

fenetre = Tk()
Label(fenetre, text="Bonjour, quelle action souhaitez vous exécuter avec ce programme ?").pack()

# Espace blanc pour aérer l'interface
Canvas(fenetre, width=500, height=75, bg='white').pack(side=TOP, padx=5, pady=5)

# Frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=30, pady=30)

# Frame 2
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=20, pady=20)

# Frame 3
Frame3 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT, padx=5, pady=5)

# Ajout de labels pour chaque frame
Label(Frame1, text="Testez si le programme reconnaît l'auteur d'un échantillon de texte").pack(padx=10, pady=10)
Label(Frame2, text="Entraînez le programme avec un texte dont vous connaissez l'auteur").pack(padx=10, pady=10)
Label(Frame3, text="Si vous pressez ce bouton, vous quitterez l'interface du programme").pack(padx=10, pady=10)


# Bouton de test du programme
Button(Frame1, text="Tester le programme",bg='green').pack()

# Bouton d'entraînement du programme : ouvre une fenêtre dans laquelle on entre du texte
Button(Frame2, text="Entraîner le programme", bg='blue', command=FaireapparaitreZonedetexte).pack()

# Bouton de fermeture du programme : ferme la fenêtre
Button(Frame3, text="Quitter le programme", bg='red', command=fenetre.destroy).pack()



fenetre.mainloop()