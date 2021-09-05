import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Automobile.csv')

df['price'].mean()      #to calculate mean

#replacing the nan values with mean
df['price'] = df['price'].fillna(df['price'].mean())

arr = np.array(df)
type(arr)

df['price'].max()
df['price'].min()
round(df['price'].mean(),2)
round(df['price'].std(),2)  #standard deviation

df1 = df['make'].value_counts()
topmakers = df1.index[0:10]	
number = df1.values[0:10]

#plotting the graph
plt.pie(number, labels=topmakers, autopct='%.2f%%')

plt.show()
