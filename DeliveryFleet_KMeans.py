# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 14:06:27 2021

@author: Aryan Sharma
"""

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('Assets/deliveryfleet.csv')

features = df.iloc[:,[1,2]].values

plt.scatter(features[:,0], features[:,1])
plt.show()

#trying to find the right number of clusters using elbow method
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


#Urban And Rural
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
pred = kmeans.fit_predict(features)

plt.scatter(features[pred == 0, 0], features[pred == 0, 1], c = 'green', label = 'Rural')
plt.scatter(features[pred == 1, 0], features[pred == 1, 1], c = 'red', label = 'Urban')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'black', label = 'Centroid')
plt.xlabel('distance feature')
plt.ylabel('speeding feature')
plt.title('Urban and Rural')
plt.legend()
plt.show()

#task 2
kmeans2 = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
pred2 = kmeans2.fit_predict(features)

plt.scatter(features[pred2 == 0, 0], features[pred2 == 0, 1], c = 'blue', label = 'safe urban')
plt.scatter(features[pred2 == 1, 0], features[pred2 == 1, 1], c = 'green', label = 'safe rural')
plt.scatter(features[pred2 == 2, 0], features[pred2 == 2, 1], c = 'brown', label = 'rash urban')
plt.scatter(features[pred2 == 3, 0], features[pred2 == 3, 1], c = 'red', label = 'rash rural')
plt.legend()
plt.show()



