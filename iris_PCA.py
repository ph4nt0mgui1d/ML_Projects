# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:39:47 2021

@author: Aryan Sharma
"""

import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()

iris.data
iris.feature_names

iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)

features = iris_df.iloc[:, 0:].values

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Elbow method
wcss = []
for i in range(1,11):
    kmean = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmean.fit(features)
    wcss.append(kmean.inertia_)
    
print(wcss)

plt.plot(range(1,11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
kmeans.fit(features)

pred_cluster = kmeans.fit_predict(features)

print(pred_cluster)
