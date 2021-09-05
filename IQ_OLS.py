# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 17:37:34 2021

@author: Aryan Sharma
"""

import pandas as pd

dataset = pd.read_csv('IQ_Size.csv')

dataset.isnull().any(axis = 0)

features = dataset.iloc[:, 1:].values
labels = dataset.iloc[:, [0]].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, _labels_test = train_test_split(features, labels, test_size=0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

task1 = regressor.predict([[90, 70, 150]])

import statsmodels.api as sm

features = sm.add_constant(features)
features_optimal = features[:, [0,1,2,3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_optimal).fit()

regressor_OLS.summary()

#drop weight

features_optimal = features[:, [0,1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_optimal).fit()
regressor_OLS.summary()

#drop constant

features_optimal = features[:, [1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_optimal).fit()
regressor_OLS.summary()

#drop height

features_optimal = features[:, [1]]
regressor_OLS = sm.OLS(endog = labels, exog = features_optimal).fit()
regressor_OLS.summary()