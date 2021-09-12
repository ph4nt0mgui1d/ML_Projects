# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 22:56:47 2021

@author: Aryan Sharma
"""

import pandas as pd

df = pd.read_csv('Assets/ign.csv')


filtered_reviews = df[(df["score"] > 7) & (df["platform"] == "Xbox One")]
games_list_xbox = filtered_reviews['title']
print (games_list_xbox)


xbox_df = df[df['platform'] == 'Xbox One']
xbox_reviews = xbox_df['score_phrase']
xbox_reviews.hist(bins=20, grid = False, xrot=90)


ps4 = df['platform']=="PlayStation 4"
ps4_only_df = df[ps4]
ps4_reviews = ps4_only_df['score_phrase']
ps4_reviews.hist(bins=20, grid=False, xrot=90)
