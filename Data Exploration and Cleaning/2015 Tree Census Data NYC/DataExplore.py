# Data Exploration for 2015 Tree Census Data
# source: https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh

import pandas as pd
import numpy as np
# pd.show_versions()
pd.set_option('display.max_columns', None)

df1 = pd.read_csv("/home/ariestootl/Documents/Python Practice/0. Python Projects/Data Exploration and Cleaning/Data Exploration/Tree_Data.csv")

df1

df1.columns

df2 = df1[['tree_id', 'tree_dbh', 'stump_diam',\
       'curb_loc', 'status', 'health', 'spc_latin', 'spc_common', 'steward',\
       'guards', 'sidewalk', 'user_type', 'problems', 'root_stone',\
       'root_grate', 'root_other', 'trunk_wire', 'trnk_light', 'trnk_other',\
       'brch_light', 'brch_shoe', 'brch_other']].copy()
df2


df2.isna().sum()


df2[df2['health'].isna()]


df2.dtypes

df2.describe()


df2.hist(bins=60, figsize=(20,10))

big_trees = df2[df2['tree_dbh']>50]
big_trees[['tree_id', 'tree_dbh']].plot(kind='scatter', x='tree_id', y='tree_dbh', figsize=(20,10))


big_trees2 = df2[df2['stump_diam']>50]
big_trees2[['tree_id', 'stump_diam']].plot(kind='scatter', x='tree_id', y='stump_diam', figsize=(20,10))


pd.DataFrame(df2['spc_latin'].value_counts()).plot(kind='bar', figsize=(20,10))


df2['steward'].value_counts()
df2['sidewalk'].value_counts()
df2['status'].value_counts()
df2['curb_loc'].value_counts()
df2['health'].value_counts()

stumps = df2[df2['status'] == "Stump"]
stumps

alive = df2[df2['status'] == "Alive"]
alive


dead = df2[df2['status'] == "Dead"]
dead

# len(dead) + len(stumps) + len(alive)

df2.columns

df3 = df2[['root_stone', 'root_grate', 'root_other', 'trunk_wire',\
       'trnk_light', 'trnk_other', 'brch_light', 'brch_shoe', 'brch_other']]

df3

df3.apply(pd.Series.value_counts)


# Data Cleaning

df2.isna().sum()
mask = df2.loc[(df2['status'] == "Dead") | (df2['status'] == "Stump")]

df4 = mask.fillna('Not Applicable')
df4

df4.isna().sum()


df5 = df2.loc[(df2['status'] == 'Alive')].copy()
df5

df5[df5['health'].isna()]

df5.isna().sum()

df5[df5['spc_latin'].isna()]
df5[df5['problems'].isna()]


df5['problems'] = df5['problems'].fillna('None')
df5['health'] = df5['health'].fillna('None')
df5['spc_latin'] = df5['spc_latin'].fillna('No Observation')
df5['spc_common'] = df5['spc_common'].fillna('No Name')
df5['sidewalk'] = df5['sidewalk'].fillna('No Damage')
df5['guards'] = df5['guards'].fillna('No guard')


df5



frames = [df4 ,df5]
df_clean = pd.concat(frames).sort_index(ascending=True)

df_clean


df_clean.to_csv('Documents/Python Practice/0. Python Projects/Data Exploration and Cleaning/Data Exploration/Tree_Data_Clean.csv', index=False)
