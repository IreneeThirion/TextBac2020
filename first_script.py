#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:20:56 2020

@author: irenee
"""

# Importation de tous les modules nécéssaires
import glob
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Perceptron
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Crée la liste des auteurs présents dans le dossier "Corpus"
wildcard = 'Corpus/*'
authors =  [os.path.basename(x) for x in glob.glob(wildcard)]

# Récupère tous les fichiers .txt dans le dossier "Corpus"
wildcard = 'Corpus/*/*.txt'
paths = glob.glob(wildcard)


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

# Crée un dictionnaire avec tous ces chemins
database = dict([(author, []) for author in authors])
for path in paths:
    author_ = os.path.basename(os.path.dirname(path))
    database[author_].append(path)

# Get the opus name of each text to identify duplicates
opus =  []
for key in database.keys():
    for txt in database[key]:
        # basename contains the opus name
        basename = os.path.basename(txt)
        # first item in parts is author: skip it
        parts = basename.split('_')[1:]
        # make a string, not a list
        name = parts[0]
        for i in range(1, len(parts)):
            name += parts[i]
        name = name[:-4] # remove ending 4 CHARACTERS
        # remove final "2" or "3" except for "93"
        if name.endswith('2') or name.endswith('3'):
            if not name.endswith('93'):    
                name = name[:-1]

        opus.append(name)

# create the source text and target author variable
docs = [readfile(txt) for key in
        database.keys() for txt in database[key]]
y = [key for key in
        database.keys() for txt in database[key]]

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

#######################################################################
# Work on a single split of the data 

# Split the dataset in training and test set:
docs_train, docs_test, y_train, y_test = train_test_split(
    docs, y, test_size=0.5)

# TASK: Fit the pipeline on the training set
clf.fit(docs_train, y_train)

# L: Predict the outcome on the testing set in a variable named y_predicted
y_predicted = clf.predict(docs_test)

# Print the classification report
print(metrics.classification_report(y_test, y_predicted))

# Plot the confusion matrix
cm = metrics.confusion_matrix(y_test, y_predicted)
print(cm)

# Maybe be over-optimistic, because exerpts of the same opus can be 
# in train and test


#######################################################################
# Work on multiple splits of the data 
from sklearn.model_selection import GroupShuffleSplit, cross_val_score
import numpy as np

# Define the cross-validation object
gss = GroupShuffleSplit(n_splits=10, train_size=.7, random_state=42)

# Compute cross-validated scores
scores = cross_val_score(clf, docs, y, cv=gss, groups=opus)
print(scores)
print(np.mean(scores))

# evaluate the chance level
from sklearn.dummy import DummyClassifier
dummy = DummyClassifier()
dummy_scores = cross_val_score(dummy, docs, y, cv=gss, groups=opus)
print(np.mean(dummy_scores))


#######################################################################
# step-by step

vectorizer.fit(docs_train, y_train)
sample = docs[0]
print(vectorizer.transform(sample))