# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 14:27:30 2021

@author: Aryan Sharma
"""

from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv('Box_Office.csv')

regressorB = LinearRegression()
regressorD = LinearRegression()

days = df['Days'].values
Bcollection = df['Bahu_collections'].values
Dcollection = df['Dangal_collections'].values

days = days.reshape(9,1)

regressorB.fit(days, Bcollection)
regressorD.fit(days, Dcollection)

colB = regressorB.predict([[10]])
colD = regressorD.predict([[10]])

day = 10

if colB > colD:
 print ("Therefore, Bahubali 2 will earn more on the {0}th day".format(day))
else:
 print ("Therefore, Dangal will earn more on the {0}th day".format(day))
 

