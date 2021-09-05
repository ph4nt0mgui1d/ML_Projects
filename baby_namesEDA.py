# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 12:28:15 2021

@author: Aryan Sharma
"""

from glob import glob
import pandas
import re



files = glob('baby_names/*.txt')

temp_list = []
for file in files:
    df = pandas.read_csv(file, names = ['name','gender','count'])
    year = int(re.findall(r'\d\d\d\d', file)[0])
    
    if year > 2010:
        break
    
    df['year'] = year
    
    temp_list.append(df)
    
finaldf = pandas.concat(temp_list, ignore_index = False, axis = 0)

df_2010 = finaldf[finaldf['year'] == 2010]
female = df_2010[df_2010['gender'] == 'F']
female_sort = female.sort_values('count',ascending = False, ignore_index = True)
female_sort['name'].head()

df_2010 = finaldf[finaldf['year'] == 2010]
male = df_2010[df_2010['gender'] == 'M']
male_sort = male.sort_values('count',ascending = False, ignore_index = True)
male_sort['name'].head()

grouped_multiple = finaldf.groupby(['year', 'gender']).agg({'count': ['sum']})
grouped_multiple

grouped_multiple.plot(kind='bar')
grouped_multiple[0:10].plot(kind='bar')
