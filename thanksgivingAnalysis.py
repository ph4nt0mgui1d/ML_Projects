# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:50:09 2021

@author: Aryan Sharma
"""

import pandas as pd
import numpy as np
import re

thanksgiving_df = pd.read_csv('thanksgiving.csv', encoding = 'Windows 1252')

columns_names = thanksgiving_df.columns.tolist()

columns_code = [x for x in range(0,65)]

columns_names_code_mapping = dict(zip(columns_code, columns_names))

thanksgiving_df.columns = columns_code

thanksgiving_df = thanksgiving_df[thanksgiving_df[1] == "Yes"]

thanksgiving_df.isnull().any(axis = 0)

thanksgiving_df = thanksgiving_df.replace(np.nan, 'Missing')

region_based = thanksgiving_df.groupby(64)
print (region_based.groups)
print (region_based.size())

income_based = thanksgiving_df.groupby(63)
print (income_based.groups)
print (income_based.size())


area_type_based = thanksgiving_df.groupby(60)
print (area_type_based.groups)
print (area_type_based.size())


sauce_type_per_income_group = thanksgiving_df.groupby(8)[63].value_counts()

print (sauce_type_per_income_group)

def gender_filter(value):
    if value == "Male":
        value = 0
    elif value == "Female":
        value = 1

    return value

thanksgiving_df[62] = thanksgiving_df[62].apply(gender_filter)
print (thanksgiving_df[62].value_counts(dropna = False))


thanksgiving_df[63] = thanksgiving_df[63].replace(['Prefer not to answer', 'Missing'],['0','0'])

regex = re.compile("\d+\W*\d+")

def income_filter(value):
    value = regex.findall(value)
    value = [int(x.replace(",", "")) for x in value]
    return sum(value)/(len(value)+0.1)


thanksgiving_df[63] = thanksgiving_df[63].apply(income_filter)


 
income_by_sauce_type = thanksgiving_df.groupby(8)[63]

print (income_by_sauce_type.groups)

avg_income_by_sauce_type = income_by_sauce_type.mean()

print (avg_income_by_sauce_type)



avg_income_by_sauce_type.plot.bar()
