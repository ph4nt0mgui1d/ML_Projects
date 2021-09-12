# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 17:56:31 2021

@author: Aryan Sharma
"""


import pandas as pd
import numpy as np

df = pd.read_json('Assets/bitly.json', lines = True)

df.isnull().any(axis = 0)
df = df.replace([np.nan, 'Missing'], [' ', 'Unknown'] )


df_tz = df['tz'].value_counts().head(10)
tz_count = df['tz'].value_counts()
json_df_tz.plot.bar()


tokens_df = df['a'].str.split(n = 1, expand = True).add_prefix("Token_")
tokens_frequency = tokens_df['Token_0'].value_counts()


tokens_frequency.head().plot.bar()
tokens_df = tokens_df.replace(np.nan, 'Missing')


tokens_df["os"] = 'Not Windows'
tokens_df["os"][tokens_df["Token_1"].str.find("Windows") != -1] = "Windows"
