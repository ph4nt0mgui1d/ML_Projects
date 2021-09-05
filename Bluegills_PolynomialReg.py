# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 21:00:17 2021

@author: Aryan Sharma
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Assets/bluegills.csv')
features = dataset.iloc[:, 0:1].values
labels = dataset.iloc[:, 1].values

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(features, labels)

features_grid = np.arange(min(features), max(features), 0.1)
features_grid = features_grid.reshape(len(features_grid), 1)
plt.scatter(features, labels, color = 'red')
plt.plot(features_grid, lin_reg.predict(features_grid), color = 'blue')
plt.title('Bluegill (Linear Regression)')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()



# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
higher_degree_gen = PolynomialFeatures(degree = 2)
features_poly = higher_degree_gen.fit_transform(features)
regressor_poly = LinearRegression()
regressor_poly.fit(features_poly, labels)


# Visualising the Polynomial Regression results (for higher resolution and smoother curve)

features_grid = np.arange(min(features), max(features), 0.1)
features_grid = features_grid.reshape(len(features_grid), 1)
plt.scatter(features, labels, color = 'red')
plt.plot(features_grid, regressor_poly.predict(higher_degree_gen.fit_transform(features_grid)), color = 'blue')
plt.title('Bluegill (Linear Regression)')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()



print ("Predicting result with Linear Regression :"+str(lin_reg.predict([[5]])))


print ("Predicting result with Polynomial Regression :"+str(regressor_poly.predict(higher_degree_gen.fit_transform([[5]]))))


