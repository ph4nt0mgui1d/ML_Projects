# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 12:59:53 2021

@author: Aryan Sharma
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Assets/Foodtruck.csv')

features = df['Population'].values
labels = df['Profit'].values

features = features.reshape(97,1)
labels = labels.reshape(97,1)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features,labels)

plt.scatter(features, labels)
plt.plot(features, regressor.predict(features))

regressor.predict([[3.073]])

regressor.predict([[33.4]])
