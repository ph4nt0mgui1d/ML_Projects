# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 00:42:25 2021

@author: Aryan Sharma
"""

import pandas as pd
df = pd.read_csv('Assets/crime_data.csv')

df.isnull().any(axis = 0)

features = df.iloc[:, [1,2,4]].values

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)

features = pca.fit_transform(features)

variance = pca.explained_variance_ratio_
print(variance)


from sklearn.cluster import KMeans

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)  
    wcss.append(kmeans.inertia_)     
    
print(wcss)
      
import matplotlib.pyplot as plt
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)

pred_cluster = kmeans.fit_predict(features) 

print(pred_cluster)
