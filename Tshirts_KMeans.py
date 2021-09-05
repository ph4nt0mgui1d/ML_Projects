# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 16:11:27 2021

@author: Aryan Sharma
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Assets/tshirts.csv')

features = df.iloc[:, [1,2]].values

plt.scatter(features[:, 0], features[:, 1])
plt.xlabel('height')
plt.ylabel('weight')
plt.show()


from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    clusterer = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    clusterer.fit(features)
    wcss.append(clusterer.inertia_)
    
plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred = kmeans.fit_predict(features)

plt.scatter(features[pred == 0, 0], features[pred == 0, 1], c='green', label = 'medium')
plt.scatter(features[pred == 1, 0], features[pred == 1, 1], c = 'blue', label = 'large')
plt.scatter(features[pred == 2, 0], features[pred == 2, 1], c = 'cyan', label = 'small')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],s = 100, c = 'yellow', label = 'Centroids')
plt.legend()
plt.title('Size Chart')
plt.show() 



