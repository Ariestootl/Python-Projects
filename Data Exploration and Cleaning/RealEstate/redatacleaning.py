import pandas as pd
import numpy as np
import re


df1 = pd.read_csv('/home/ariestootl/Documents/Python Practice/0. Python Projects/Data Exploration and Cleaning/Remove Duplicates/RealEstate.csv')

df1.isna().sum()

df1.columns


df1['PROPERTY ADDRESS'] = df1['PROPERTY ADDRESS'].fillna('None')
df1['PROPERTY ZIP'] = df1['PROPERTY ZIP'].fillna('None')

df2 = df1.loc[(df1['OWNER'] != "Not Available From The County") & (df1['PROPERTY ADDRESS'] != 'None')].copy()



# x = df2.loc[(df2['MAILING_ZIP'].isna())]

df2['MAILING_ZIP'] = df2['MAILING_ZIP'].fillna('NONE')
df2['MAILING_ADDRESS'] = df2['MAILING_ADDRESS'].fillna('NONE')
df2['MAILING_CITY'] = df2['MAILING_CITY'].fillna('NONE')
df2['MAILING_STATE'] = df2['MAILING_STATE'].fillna('NONE')


name = df2['OWNER'].str.split(expand=True)
df2['OWNER_FIRST_NAME'] = name[0]

df2

df2.to_csv('Documents/Python Practice/0. Python Projects/Data Exploration and Cleaning/Remove Duplicates/RealEstate_Cleaned.csv', index=False)
# name.columns
#
# names = name.rename(columns={6:'Col6', 0:'OWNER_FIRST_NAME'})
#
# names['OWNER_FIRST_NAME']
#
# names[names['Col6'].isna()]
