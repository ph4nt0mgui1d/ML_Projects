
import pandas as pd
import numpy as np
df = pd.read_csv('Baltimore.csv')

df.sample(5)


df['AnnualSalary'] = df['AnnualSalary'].astype(str)
df['AnnualSalary'] = df['AnnualSalary'].apply(lambda x: x.replace('$',''))
df['AnnualSalary'] = df['AnnualSalary'].astype(float)


grouped = df.groupby(['JobTitle'])['AnnualSalary']
aggregated = grouped.agg([np.sum, np.mean])
print(aggregated)


df['JobTitle'].value_counts()[0:10].plot(kind = 'bar')


agency_name_id = df[['Agency','AgencyID']]
agency_name_id.drop_duplicates(inplace=True)
print(agency_name_id)


df['GrossPay'].isnull().sum()

