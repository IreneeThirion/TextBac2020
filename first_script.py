#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:20:56 2020

@author: irenee
"""

# Importation de tous les modules nécéssaires
import glob
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Perceptron
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Crée la liste des auteurs présents dans le dossier "Corpus"
wildcard = 'Corpus/*'
authors =  [os.path.basename(x) for x in glob.glob(wildcard)]

# Récupère tous les fichiers .txt dans le dossier "Corpus"
wildcard = 'Corpus/*/*.txt'
paths = glob.glob(wildcard)

# Crée un dictionnaire avec tous ces chemins
database = dict([(author, []) for author in authors])
for path in paths:
    author_ = os.path.basename(os.path.dirname(path))
    database[author_].append(path)

# Crée "docs" (textes) et y (auteurs) dans une base de données
def readfile(filename):
    """"Read the file in filename and return the content as a string"""
    fichier = open(filename)
    lignes = fichier.readlines()
    fichier.close()
    txt = ''
    for ligne in lignes:
        txt += ligne
    return txt


docs = [readfile(txt) for key in
        database.keys() for txt in database[key]]
y = [key for key in
        database.keys() for txt in database[key]]

# Split the dataset in training and test set:
docs_train, docs_test, y_train, y_test = train_test_split(
    docs, y, test_size=0.5)

# Build a vectorizer that splits strings into sequence of 1 to 3
# characters instead of word tokens
vectorizer = TfidfVectorizer(ngram_range=(1, 3), analyzer='char',
                             use_idf=False)

# TASK: Build a vectorizer / classifier pipeline using the previous analyzer
# the pipeline instance should stored in a variable named clf
clf = Pipeline([
    ('vec', vectorizer),
    ('clf', Perceptron()),
])

# TASK: Fit the pipeline on the training set
clf.fit(docs_train, y_train)

# L: Predict the outcome on the testing set in a variable named y_predicted
y_predicted = clf.predict(docs_test)

# Print the classification report
print(metrics.classification_report(y_test, y_predicted))

# Plot the confusion matrix
cm = metrics.confusion_matrix(y_test, y_predicted)
print(cm)
