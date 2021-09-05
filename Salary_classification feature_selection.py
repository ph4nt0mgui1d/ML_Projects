# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 17:52:03 2021

@author: Aryan Sharma
"""

import pandas as pd

df = pd.read_csv('Salary_Classification.csv')

df.isnull().any(axis = 0)

features = df.iloc[:,:4].values
labels = df.iloc[:,4].values

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

cTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder = 'passthrough')

import numpy as np
features = np.array(cTransformer.fit_transform(features), dtype = np.float32)

features = features[:,1:]

#feature selection
#backward selection

import statsmodels.api as sm

features = sm.add_constant(features)

features_optimal = features[:,[0,1,2,3,4,5]]

# regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()

# regressor_ols.summary()

while(True):
    regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()    
    p_values = regressor_ols.pvalues
    if p_values.max() > 0.05:
        features_optimal = np.delete(features_optimal, p_values.argmax(), 1)
    else:
        break

features_optimal.shape