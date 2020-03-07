#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 14:00:55 2020

@author: irenee
"""

from tkinter import *
    
analyse = Tk()
Label(analyse, text="Analyse en cours, veuillez patienter SVP").pack()

# Espace blanc pour aérer l'interface
Canvas(analyse, width=500, height=75, bg='white').pack(side=TOP, padx=5, pady=5)

analyse.mainloop()