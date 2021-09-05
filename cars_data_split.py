# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 18:56:17 2021

@author: Aryan Sharma
"""

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('Assets/cars.csv')

train_data, test_data = train_test_split(df, train_size = 0.5, random_state = 0)

train_data.to_csv('train_data.csv', index = False)
test_data.to_csv('test_data.csv', index = False)
