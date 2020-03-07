#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 18:59:26 2020

@author: irenee
"""

from tkinter import *

question = Tk()


def retenir():
    auteur = str(reponseauteur.get())
    return(auteur)


question.title = ("L'auteur du texte")
Label(question, text = "Reste une dernière question : qui est l'auteur du texte analysé ?").pack(padx = 10, pady = 10)
Framequest = Frame(question, borderwidth = 2, relief = GROOVE)
Framequest.pack(side = LEFT, padx = 30, pady = 30)
Label(Framequest, text = "Veuillez entrer le nom de l'auteur du texte analysé dans le champ de saisie ci-dessous").pack(padx = 10, pady = 10)

reponseauteur = Entry(Framequest)
reponseauteur.pack()

validationauteur = Button(Framequest, text='Valider', command=retenir())
validationauteur.pack()

question.mainloop()