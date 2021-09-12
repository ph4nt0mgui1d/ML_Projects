# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:50:09 2021

@author: Aryan Sharma
"""

import pandas as pd
import numpy as np
import re

df = pd.read_csv('Assets/thanksgiving.csv', encoding = 'Windows 1252')

columns_names = df.columns.tolist()

columns_code = [x for x in range(0,65)]

columns_names_code_mapping = dict(zip(columns_code, columns_names))

df.columns = columns_code

df = df[df[1] == "Yes"]

df.isnull().any(axis = 0)
df = df.replace(np.nan, 'Missing')


region_based = df.groupby(64)
region_based.groups
region_based.size()

income_based = df.groupby(63)
income_based.groups
income_based.size()

area_type_based = df.groupby(60)
area_type_based.groups
area_type_based.size()


sauce_type_per_income_group = df.groupby(8)[63].value_counts()
sauce_type_per_income_group


def gender_filter(value):
    if value == "Male":
        value = 0
    elif value == "Female":
        value = 1

    return value

df[62] = df[62].apply(gender_filter)
df[62].value_counts()


df[63] = df[63].replace(['Prefer not to answer', 'Missing'],['0','0'])

regex = re.compile("\d+\W*\d+")

def income_filter(value):
    value = regex.findall(value)
    value = [int(x.replace(",", "")) for x in value]
    return sum(value)/(len(value)+0.1)


df[63] = df[63].apply(income_filter)


income_by_sauce_type = df.groupby(8)[63]
income_by_sauce_type.groups

avg_income_by_sauce_type = income_by_sauce_type.mean()
avg_income_by_sauce_type
avg_income_by_sauce_type.plot.bar()
