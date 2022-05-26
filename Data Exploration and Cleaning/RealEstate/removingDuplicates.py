# I have attached a file that needs some work
#
#
# 1.) Removing the duplicate Owners via using the Mailing address and then transferring all these duplicates to another sheet.
# 2.) We can remove duplicated mailing addresses but a mailing address is unique if it has a different mailing ZIP code.
# 3.) Showing proof that there is no duplicated Owner.
# 4.) Adding 2 columns that will format the "Owner" column into separated first names, middle initial/name, last names.
# 5.) No need to mind the Owner2.
# 6.) Explain how you did it

import pandas as pd
import numpy as np
import re


# df_raw = pd.read_csv(input("Enter Full Path of the File: "))
df_raw = pd.read_csv('/home/ariestootl/Documents/Python Practice/0. Python Projects/Data Exploration and Cleaning/Remove Duplicates/RealEstate_Cleaned.csv')
# df_raw.MAILING_ADDRESS = df_raw.MAILING_ADDRESS.fillna('NONE')
# df_raw['PROPERTY ADDRESS'] = df_raw['PROPERTY ADDRESS'].fillna('NONE')
# df_raw['PROPERTY ZIP'] = df_raw['PROPERTY ZIP'].fillna('NONE')
# df_raw['MAILING_ZIP'] = df_raw['MAILING_ZIP'].fillna('NONE')

# df_raw.duplicated(subset=['OWNER', 'MAILING_ADDRESS']).value_counts()
print(df_raw.shape)
# cols = df_raw.columns
# columns = list(cols)
# print(columns)

empty_add = df_raw.loc[(df_raw['MAILING_ADDRESS'] == "NONE")].copy()
empty_add['UID'] = empty_add['OWNER'].astype(str).str.casefold().str.replace(" ","_") + "_" + empty_add['PROPERTY ADDRESS'].astype(str).str.casefold().str.replace(" ","_")
empty_add['UID2'] = empty_add['PROPERTY ADDRESS'].astype(str).str.casefold().str.replace(" ","_") + "_" + empty_add['PROPERTY ZIP'].astype(str).str.casefold().str.replace(" ","_")

notempty_add = df_raw.loc[(df_raw['MAILING_ADDRESS'] != "NONE")].copy()
notempty_add['UID'] = df_raw['OWNER'].astype(str).str.casefold().str.replace(" ","_") + "_" + df_raw['MAILING_ADDRESS'].astype(str).str.casefold().str.replace(" ","_")
notempty_add['UID2'] = notempty_add['MAILING_ADDRESS'].astype(str).str.casefold().str.replace(" ","_") + "_" + notempty_add['MAILING_ZIP'].astype(str).str.casefold().str.replace(" ","_")

frames = [empty_add, notempty_add]
df_new = pd.concat(frames).sort_index(ascending=True)


# df_new[['UID', 'UID2']]
# df_new.duplicated(subset=['UID'], keep='first').value_counts()



#Countif() with Python -----------------------------------------------------
COUNT = []
COUNT2 = []
i = 0
for i in range(len(df_raw)):
    UID = df_new['UID'].iloc[i]
    UID_2 = df_new['UID2'].iloc[i]
    count = df_new.query("UID == @UID")['UID'].count()
    count2 = df_new.query("UID2 == @UID_2")['UID2'].count()
    COUNT.append(count)
    COUNT2.append(count2)
    i = i + 1
## ---------------------------------------------------------------------------

df_new['UID_COUNT1'] = COUNT
df_new['UID_COUNT2'] = COUNT2

cols = df_new.columns
columns = list(cols)
# print(columns)

df_new[:]

raw_cleaned = df_new.drop(columns=['UID', 'UID2'])

no_dupes2 = df_new.drop_duplicates(subset=['UID'], keep='first').copy()
no_dupes3 = no_dupes2.drop_duplicates(subset=['UID2'], keep='first').copy()

Unique1 = no_dupes2.drop(columns=['UID', 'UID2'])
Unique2 = no_dupes3.drop(columns=['UID', 'UID2'])

first_dupes = df_new.query("UID_COUNT1 > 1")
sec_dupes = df_new.loc[(df_new["UID_COUNT1"] > 1) & (df_new["UID_COUNT2"] > 1)]
no_dupes = df_new.loc[(df_new["UID_COUNT1"] == 1) & (df_new["UID_COUNT2"] == 1)]

xlwriter = pd.ExcelWriter('Documents/Python Practice/0. Python Projects/Data Exploration and Cleaning/Remove Duplicates/Output Folder/OUTPUT.xlsx')
raw_cleaned.to_excel(xlwriter, sheet_name = "raw_data", index=False)
first_dupes.to_excel(xlwriter, sheet_name="First_Duplicates", index=False)
sec_dupes.to_excel(xlwriter, sheet_name="Second_Duplicates", index=False)
no_dupes.to_excel(xlwriter, sheet_name="No Dupes 1", index=False)
Unique1.to_excel(xlwriter, sheet_name="All Unique1", index=False)
Unique2.to_excel(xlwriter, sheet_name="All Unique2", index=False)
xlwriter.close()
