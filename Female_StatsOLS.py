# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 09:39:21 2021

@author: Aryan Sharma
"""

import pandas as pd
df = pd.read_csv('Assets/Female_Stats.csv')

df.isnull().any(axis = 0)

labels = df.iloc[:,0].values
features = df.iloc[:, [1,2]].values

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(features, labels)

#task 2
# regressor.coef_[0][0]

# #task 3
# regressor.coef_[0][1]

import statsmodels.api as sm

features = sm.add_constant(features)
regressor_OLS = sm.OLS(endog = labels, exog = features).fit()

regressor_OLS.summary()

