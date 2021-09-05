# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 12:42:51 2021

@author: Aryan Sharma
"""

import pandas as pd
data = pd.read_table('amazon_cells_labelled.txt', names = ["Review", "Liked"])

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

corpus = []
 
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', data['Review'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    
    review = ' '.join(review)
    
    corpus.append(review)

print(corpus)
print(len(corpus))


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features =1500)

# it is known as sparse matrix of the features ND Array
features = cv.fit_transform(corpus).toarray() # 1500 columns
labels = data.iloc[:, 1].values

print(features.shape)
print(labels.shape)

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = \
train_test_split(features, labels, test_size = 0.20, random_state = 0)



#applying knn on this text dataset
# Fitting Knn to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_knn = confusion_matrix(labels_test, labels_pred)
print(cm_knn) 

print( (cm_knn[0][0] + cm_knn[1][1]) / (cm_knn[0][0] + cm_knn[1][1] + cm_knn[0][1] + cm_knn[1][0]))

# for better NLP results we need lot of data


# or

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix

cm_nb = confusion_matrix(labels_test, labels_pred)
print(cm_nb)

print( (cm_nb[0][0] + cm_nb[1][1]) / (cm_nb[0][0] + cm_nb[1][1] + cm_nb[0][1] + cm_nb[1][0]))

