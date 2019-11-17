#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 15:06:26 2019

@author: irenee
"""

from tkinter import * #On importe l'ensemble du module Tkinter

def repondre():
 affichage['text'] = reponse.get()	# lecture du contenu du widget "reponse"

Fenetre = Tk()
Fenetre.title('Mon nom')

nom = Label(Fenetre, text = 'Votre nom :')
reponse = Entry(Fenetre)
valeur = Button(Fenetre, text =' Valider', command=repondre)
affichage = Label(Fenetre, width=30)
votre_nom=Label(Fenetre, text='Votre nom est :')
nom.pack()
reponse.pack()
valeur.pack()
votre_nom.pack()
affichage.pack()

Fenetre.mainloop()