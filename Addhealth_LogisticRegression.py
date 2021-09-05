# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 19:06:33 2021

@author: Aryan Sharma
"""

import pandas as pd
df = pd.read_csv('Assets/addhealth.csv')

for i in df:
    df[i] = df[i].fillna(df[i].mode()[0])


#Task -- 1
features = df[['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN', 'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail', 'DEP1','ESTEEM1']].values
labels = df["TREG1"].values

from sklearn.model_selection import train_test_split as TTS
features_train,features_test,labels_train,labels_test = TTS(features, labels, test_size = 0.25, random_state = 0)

from sklearn.linear_model import LogisticRegression
classification_treg1 = LogisticRegression(random_state=0)
classification_treg1.fit(features_train, labels_train)

pred = classification_treg1.predict(features_test)   # Prediction on test data   

# Confusion Matrix
from sklearn.metrics import confusion_matrix
classification_treg1_cm = confusion_matrix(labels_test, pred)

# check the accuracy on the Model
classification_treg1_score = classification_treg1.score(features_test, labels_test)



#Task -- 2
features_expel = df[["BIO_SEX","VIOL1"]].values
labels_expel = df["EXPEL1"].values
    
# Splitting the dataset into train and test
from sklearn.model_selection import train_test_split as TTS

f_train,f_test,l_train,l_test = TTS(features_expel, labels_expel, test_size = 0.25,
                                    random_state = 0)

# Logistic Regression Model
from sklearn.linear_model import LogisticRegression
classifier_expel = LogisticRegression(random_state=0)
classifier_expel.fit(f_train, l_train)

Pred1 = classifier_expel.predict(f_test)   # Prediction on test data   

# Confusion Matrix
from sklearn.metrics import confusion_matrix
CM1 = confusion_matrix(l_test, Pred1)

# check the accuracy on the Model
Score1 = classifier_expel.score(f_test, l_test)
