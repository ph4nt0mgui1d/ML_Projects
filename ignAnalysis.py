# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 22:56:47 2021

@author: Aryan Sharma
"""

import pandas as pd

df = pd.read_csv('ign.csv')


xbox_one_filter = (df["score"] > 7) & (df["platform"] == "Xbox One")
filtered_reviews = df[xbox_one_filter]
games_list_xbox_one = filtered_reviews['title']
print (games_list_xbox_one)


xbox_one = df['platform']=="Xbox One"
xbox_one_only_df = df[xbox_one]
xbox_one_reviews = xbox_one_only_df['score_phrase']
xbox_one_reviews.hist(bins=20, grid = False, xrot=90)


ps4 = df['platform']=="PlayStation 4"
ps4_only_df = df[ps4]
ps4_reviews = ps4_only_df['score_phrase']
ps4_reviews.hist(bins=20, grid=False, xrot=90)


