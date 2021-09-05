# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:47:36 2021

@author: Aryan Sharma
"""

import pandas as pd
import numpy as np
df = pd.read_csv('affairs.csv')

df.isnull().any(axis = 0)

df.dtypes
df.sample(10)

features = df.iloc[:, :8].values
labels = df.iloc[:, [8]].values

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
cTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [6,7])], remainder = 'passthrough')
features = cTransformer.fit_transform(features)

col_to_ohe = [6,7]
total_col, indexes = 0, []
for col in col_to_ohe:
    unique_val_count = len(df.iloc[:,col].value_counts())
    total_col += unique_val_count
    indexes.append(total_col - unique_val_count)
features = np.delete(features, indexes, axis=1)

from sklearn.model_selection import train_test_split as TTS
features_train, features_test, labels_train, labels_test = TTS(features, labels, test_size = 0.25, random_state = 0)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

prediction = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, prediction)

mod_score = classifier.score(features_test, labels_test)



val = np.array([3, 25, 3, 1, 4, 16, 4, 2]).reshape(1,-1)
val = cTransformer.transform(val)
val = np.delete(val, indexes, axis=1)
   
val_pred = classifier.predict_proba(val) 


    
