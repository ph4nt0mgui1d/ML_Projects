# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 10:32:54 2021

@author: Aryan Sharma
"""

import pandas as pd
df = pd.read_csv('mushrooms.csv')

labels = df.iloc[:, [0]].values
features = df.iloc[:, [5,-2,-1]].values

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

#for binary type categorical data use lableencoder()
le = LabelEncoder()
labels = le.fit_transform(labels)

cTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0,1,2])], remainder='passthrough')
features = cTransformer.fit_transform(features).toarray()

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size = 0.2)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2)
classifier.fit(features_train, labels_train)
pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, pred)


print ("Model Score : "+str(round(classifier.score(features_test,labels_test),3)*100)+"%")

