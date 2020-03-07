#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 13:06:50 2020

@author: irenee
"""

from tkinter import *

fin = Tk()

def toutquitter():
    fin.destroy()
    fenetre.destroy()

Label(fin, text="Merci d'avoir participé ! Que souhaitez vous faire maintenant ?").pack()

# Frame retour
Frameretour = Frame(fin, borderwidth=2, relief=GROOVE)
Frameretour.pack(side=LEFT, padx=30, pady=30)

# Frame fin
Framefin = Frame(fin, borderwidth=2, relief=GROOVE)
Framefin.pack(side=LEFT, padx=20, pady=20)

# Ajout de labels pour chaque frame
Label(Frameretour, text="Retour au menu principal").pack(padx=10, pady=10)
Label(Framefin, text="Quitter l'interface du programme").pack(padx=10, pady=10)

# Bouton de retour au menu principal
Button(Frameretour, text="Retour vers le menu", bg='violet', command=fin.destroy).pack()

# Bouton de fermeture du programme : ferme tout
Button(Framefin, text="Quitter le programme", bg='red', command=toutquitter).pack()
    
fin.mainloop()
