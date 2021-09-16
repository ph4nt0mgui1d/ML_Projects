# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 23:24:47 2021

@author: Aryan Sharma
"""

import pandas as pd
df = pd.read_csv('Assets/banknotes.csv')

features = df.iloc[:, 1:-1].values
labels = df.iloc[:, -1].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size = 0.25, random_state = 0)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

print(cm)

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = features_train, y = labels_train, cv = 10)
print ("mean accuracy is : "+str(round(accuracies.mean()*100,2))+"%")
print ("standard deviation : "+str(accuracies.std()))