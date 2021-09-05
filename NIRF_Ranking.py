# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 14:25:39 2021

@author: Aryan Sharma
"""

url = "https://www.embibe.com/exams/nirf-rankings/"

import requests
import pandas as pd

html_data = requests.get(url).text

from bs4 import BeautifulSoup
bs = BeautifulSoup(html_data, 'lxml')


all_tab = bs.find_all('table',class_="wp-block-table")
csv_list =["NIRF Rankings Of Overall Educational Institutes.csv","NIRF Rankings Of Engineering Colleges.csv","NIRF Rankings Of Medical Institutes.csv","NIRF Rankings Of Universities.csv"]
for i in range(len(all_tab)):
    A=[]
    B=[]
    C=[]
    D=[]
    for body in all_tab[i].find_all("tbody"):
        for row in body.find_all("tr"):
            col = row.find_all('td')
            A.append(col[0].text.strip())
            B.append(col[1].text.strip())
            C.append(col[2].text.strip())
            D.append(col[3].text.strip())
           

    df = pd.DataFrame()
    df["Rank & Name of the Institute"]= A
    df["City"]=B
    df["State"]=C
    df["NIRF Score"]=D
    df.to_csv(csv_list[i], index=False)