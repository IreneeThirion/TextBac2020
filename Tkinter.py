#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:59:14 2019

@author: irenee.thirion
"""

from tkinter import *

filename = ''
      
# Création du menu principal
fenetre = Tk()

# Fonction de test
def test():
    test = Tk()
    test.title('Test')
    Label(test, text = "Voici les instructions à suivre :").pack(padx = 10, pady = 10)

# Fonction d'entraînement
def entrainement():
    entrainement = Tk()
    entrainement.title('Entraînement')
    Label(entrainement, text = "Voici les instructions à suivre :").pack(padx = 10, pady = 10)
    # Frametest : on entre le chemin d'accès
    Frametest = Frame(entrainement, borderwidth = 2, relief = GROOVE)
    Frametest.pack(side = LEFT, padx = 30, pady = 30)
    Label(Frametest, text = "Notez le chemin d'accès d'un fichier .odt ou .txt que vous voulez analyser et entrez-le dans le champ de saisie ci-dessous").pack(padx = 10, pady = 10)
    reponse = Entry(Frametest)
    def analyse():
        filename = reponse.get()
    validation = Button(Frametest, text =' Valider', command = analyse())
    reponse.pack()
    validation.pack()
    entrainement.mainloop()

fenetre.title('Menu principal')
Label(fenetre, text = "Bonjour, quelle action souhaitez vous exécuter avec ce programme ?").pack()

# Espace blanc pour aérer l'interface
Canvas(fenetre, width = 500, height = 75, bg = 'white').pack(side = TOP, padx = 5, pady = 5)

# Frame 1 : là où on va tester le programme
Frame1 = Frame(fenetre, borderwidth = 2, relief = GROOVE)
Frame1.pack(side = LEFT, padx = 30, pady = 30)
Label(Frame1, text = "Testez si le programme reconnaît l'auteur d'un échantillon de texte").pack(padx = 10, pady = 10)
B1 = Button(Frame1, text = "Tester le programme",bg = 'green', command = test)
B1.pack()

# Frame 2 : là où on va entraîner le programme
Frame2 = Frame(fenetre, borderwidth = 2, relief = GROOVE)
Frame2.pack(side = LEFT, padx = 20, pady = 20)
Label(Frame2, text = "Entraînez le programme avec un texte dont vous connaissez l'auteur").pack(padx = 10, pady = 10)
B2 = Button(Frame2, text = "Entraîner le programme", bg = 'blue', command = entrainement)
B2.pack()


"""    
# Fait disparaître la fenêtre précédente
if (i == 1):
    entrainement.destroy
    analyse = Tk()
    analyse.title('Analyse')
    Label(analyse, text="Analyse en cours, veuillez patienter SVP").pack()
    analyse.mainloop() 
"""

# Frame 3 : là où on va fermer le programme
Frame3 = Frame(fenetre, borderwidth = 2, relief = GROOVE)
Frame3.pack(side = RIGHT, padx = 5, pady = 5)
Label(Frame3, text = "Quitter l'interface du programme").pack(padx = 10, pady = 10)
Button(Frame3, text = "Quitter le programme", bg = 'red', command = fenetre.destroy).pack()


 
fenetre.mainloop()