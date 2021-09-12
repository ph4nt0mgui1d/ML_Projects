# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 14:27:30 2021

@author: Aryan Sharma
"""

import pandas as pd

df = pd.read_csv('Assets/Box_Office.csv')

features = df['Days'].values
lablesB = df['Bahu_collections'].values
labelsD = df['Dangal_collections'].values

features = features.reshape(9,1)

from sklearn.linear_model import LinearRegression
regressorB = LinearRegression()
regressorD = LinearRegression()
regressorB.fit(features, labelsB)
regressorD.fit(features, labelsD)

colB = regressorB.predict([[10]])
colD = regressorD.predict([[10]])

day = 10

if colB > colD:
 print ("Therefore, Bahubali 2 will earn more on the {0}th day".format(day))
else:
 print ("Therefore, Dangal will earn more on the {0}th day".format(day))
 

