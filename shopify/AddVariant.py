import pandas as pd
import numpy as np
import itertools
from itertools import permutations

pd.set_option('display.max_columns', None)
products = pd.read_csv('/home/ariestootl/Documents/Python Practice/0. Python Projects/Data Exploration and Cleaning/shopify/15 shopify products without variants old file.csv')

list_1 = ['A5', 'A4','A3', 'A2', 'A1']
list_2 = ['Print in Black Frame', 'Print in White Frame', 'PRINT ONLY']
list_3 = list(products['Handle'])

unique_combinations = []


for g in range(len(list_3)):
    for i in range(len(list_1)):
        for c in range(len(list_2)):
            new_list = list_3[g] + " " + list_1[i] + " " + list_2[c]
            unique_combinations.append(new_list)


# len(unique_combinations)
cols = pd.DataFrame(unique_combinations)
cols = cols.rename(columns={0:'new'})
cols = cols['new'].str.split(" ", n=2, expand=True)
cols = cols.rename(columns={0:'Handle', 1:'Option1 Value', 2:'Option2 Value'})
cols

df1 = products[['Title', 'Body (HTML)', 'Vendor', 'Standardized Product Type', 'Custom Product Type', 'Tags', 'Published', 'Option1 Name','Option2 Name', 'Option3 Name', 'Option3 Value', 'Variant SKU', 'Variant Grams', 'Variant Inventory Tracker', 'Variant Inventory Policy', 'Variant Fulfillment Service', 'Variant Price', 'Variant Compare At Price', 'Variant Requires Shipping', 'Variant Taxable', 'Variant Barcode', 'Image Src', 'Image Position', 'Image Alt Text', 'Gift Card', 'SEO Title', 'SEO Description', 'Google Shopping / Google Product Category', 'Google Shopping / Gender', 'Google Shopping / Age Group', 'Google Shopping / MPN', 'Google Shopping / AdWords Grouping', 'Google Shopping / AdWords Labels', 'Google Shopping / Condition', 'Google Shopping / Custom Product', 'Google Shopping / Custom Label 0', 'Google Shopping / Custom Label 1', 'Google Shopping / Custom Label 2', 'Google Shopping / Custom Label 3', 'Google Shopping / Custom Label 4', 'Variant Image', 'Variant Weight Unit', 'Variant Tax Code', 'Cost per item', 'Status']]

df1 = pd.DataFrame(pd.concat([df1]*15).sort_index(ascending=True))
df1 = df1.reset_index()

frames = [df1, cols]
df_new = pd.concat(frames, axis=1, join="outer")

df_new

df_new = df_new[['Handle', 'Title', 'Body (HTML)', 'Vendor', 'Standardized Product Type', 'Custom Product Type', 'Tags', 'Published', 'Option1 Name', 'Option1 Value', 'Option2 Name', 'Option2 Value', 'Option3 Name', 'Option3 Value', 'Variant SKU', 'Variant Grams', 'Variant Inventory Tracker', 'Variant Inventory Policy', 'Variant Fulfillment Service', 'Variant Price', 'Variant Compare At Price', 'Variant Requires Shipping', 'Variant Taxable', 'Variant Barcode', 'Image Src', 'Image Position', 'Image Alt Text', 'Gift Card', 'SEO Title', 'SEO Description', 'Google Shopping / Google Product Category', 'Google Shopping / Gender', 'Google Shopping / Age Group', 'Google Shopping / MPN', 'Google Shopping / AdWords Grouping', 'Google Shopping / AdWords Labels', 'Google Shopping / Condition', 'Google Shopping / Custom Product', 'Google Shopping / Custom Label 0', 'Google Shopping / Custom Label 1', 'Google Shopping / Custom Label 2', 'Google Shopping / Custom Label 3', 'Google Shopping / Custom Label 4', 'Variant Image', 'Variant Weight Unit', 'Variant Tax Code', 'Cost per item', 'Status']]

df_new.loc[(df_new['Option1 Value'] == 'A5') & (df_new['Option2 Value'] == 'Print in Black Frame'), 'Variant Price'] = 12.99
df_new.loc[(df_new['Option1 Value'] == 'A5') & (df_new['Option2 Value'] == 'Print in White Frame'), 'Variant Price'] = 12.99
df_new.loc[(df_new['Option1 Value'] == 'A5') & (df_new['Option2 Value'] == 'PRINT ONLY '), 'Variant Price'] = 8.99

df_new.loc[(df_new['Option1 Value'] == 'A4') & (df_new['Option2 Value'] == 'Print in Black Frame'), 'Variant Price'] = 22.99
df_new.loc[(df_new['Option1 Value'] == 'A4') & (df_new['Option2 Value'] == 'Print in White Frame'), 'Variant Price'] = 22.99
df_new.loc[(df_new['Option1 Value'] == 'A4') & (df_new['Option2 Value'] == 'PRINT ONLY '), 'Variant Price'] = 12.99

df_new.loc[(df_new['Option1 Value'] == 'A3') & (df_new['Option2 Value'] == 'Print in Black Frame'), 'Variant Price'] = 29.99
df_new.loc[(df_new['Option1 Value'] == 'A3') & (df_new['Option2 Value'] == 'Print in White Frame'), 'Variant Price'] = 29.99
df_new.loc[(df_new['Option1 Value'] == 'A3') & (df_new['Option2 Value'] == 'PRINT ONLY '), 'Variant Price'] = 22.99

df_new.loc[(df_new['Option1 Value'] == 'A2') & (df_new['Option2 Value'] == 'Print in Black Frame'), 'Variant Price'] = 44.99
df_new.loc[(df_new['Option1 Value'] == 'A2') & (df_new['Option2 Value'] == 'Print in White Frame'), 'Variant Price'] = 44.99
df_new.loc[(df_new['Option1 Value'] == 'A2') & (df_new['Option2 Value'] == 'PRINT ONLY '), 'Variant Price'] = 34.99

df_new.loc[(df_new['Option1 Value'] == 'A1') & (df_new['Option2 Value'] == 'Print in Black Frame'), 'Variant Price'] = 59.99
df_new.loc[(df_new['Option1 Value'] == 'A1') & (df_new['Option2 Value'] == 'Print in White Frame'), 'Variant Price'] = 59.99
df_new.loc[(df_new['Option1 Value'] == 'A1') & (df_new['Option2 Value'] == 'PRINT ONLY '), 'Variant Price'] = 44.99


df_new['Cost per item'] = df_new['Cost per item'].replace(9.99, " ")
df_new.loc[(df_new['Option1 Value'] == 'A5') & (df_new['Option2 Value'] == 'Print in Black Frame'), 'Cost per item'] = 12.99
df_new.to_csv('Documents/Python Practice/0. Python Projects/Data Exploration and Cleaning/shopify/Sample.csv', index=False)

# products.columns

# new_prods = pd.read_csv('/home/ariestootl/Documents/Python Practice/0. Python Projects/Data Exploration and Cleaning/shopify/15 shopify products with variants new file.csv', encoding='cp1252')
#
# values = list(new_prods['Option1 Value'])
# print(values)


# option1_value = {'Option1 Value' : ['A5', 'A4','A3', 'A2', 'A1']}
# option1_value = pd.DataFrame(option1_value)
# LOL = pd.concat([option1_value['Option1 Value']]*3).sort_index(ascending=True)
# LOL = pd.DataFrame(LOL)
# option1_value = pd.concat([LOL]*15).copy()
# option1_value = option1_value.reset_index()
# # option1_value
#
# option2_value = {'Option2 Value' : ['Print in Black Frame', 'Print in White Frame', 'PRINT ONLY']}
# option2_value = pd.DataFrame(option2_value)
# option2_value['Option2 Value'].iloc[0]
# option2_value = pd.concat([option2_value['Option2 Value']]*3)
# option2_value = pd.DataFrame(option2_value)
# option2_value = pd.concat([option2_value['Option2 Value']]*15).copy()
# option2_value = option2_value.reset_index()

# df_new[['Option1 Value', 'Option2 Value', 'Variant Price']][0:10]
