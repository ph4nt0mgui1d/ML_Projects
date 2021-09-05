# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 14:19:14 2021

@author: Aryan Sharma
"""

import pandas as pd
df = pd.read_csv('Assets/movie.csv')

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []
for i in range(0, df.shape[0]):
    review = re.sub('[^a-zA-Z]', ' ', df['text'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(max_features = 4000)
features = vect.fit_transform(corpus).toarray()

labels = df.iloc[:, [0]]

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
labels = le.fit_transform(labels)

from sklearn.model_selection import train_test_split as tts
features_train, features_test, labels_train, labels_test = tts(features, labels, test_size = 0.2, random_state = 42)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(features_train, labels_train)

labels_pred = model.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

from sklearn.metrics import roc_auc_score
score = roc_auc_score(labels_test, labels_pred)


