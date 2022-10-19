import pandas as pd

my_data = pd.read_csv('pokemon_data.csv')

# print(my_data.tail(5))
# print(my_data.head(5))
# print(my_data.columns)

## Read each column
# print(my_data.Name)
# print(my_data[['Name', 'Type 1']])

## Read each row
# print(my_data.iloc[3])
# print(my_data.iloc[1:8])

## Read specific row
# print(my_data.iloc[3, 2])  # row=3 , and 2nd position


## Prints each index and data of the row
# for index, row in my_data.iterrows():
#     print("index=" ,index, row)


## Prints specific column of each index
# for index, row in my_data.iterrows():
#     print("index=", index, row['Name'])


##find some data with specific values
# print(my_data.loc[my_data.Name == 'Jynx'])


## Sort
##Show 3 cols, and sort it by two values, first sort by Type1 Ascending and then sort by HP Descending
# print(my_data[['Name', 'Type 1', 'HP']].sort_values(['Type 1', 'HP'], ascending=[1, 0]))

## Create a new column which its value is adding two column
# my_data['Total'] = my_data.HP + my_data.Attack
# print(my_data.head(10))


## to save as csv:
# new_data  = my_data[['Name', 'Type 1' , 'HP']]
# new_data.to_csv('new_data.csv', index=False)
#
# ##To save as excel file:
# new_data.to_excel('new_data.xlsx', index=False)
#
# ## To save as a text:
# new_data.to_csv('new_data.txt', sep='\t')


## Filtering

# new_my_data = my_data.loc[(my_data['Type 1'] == 'Grass') & (my_data['HP'] > 70)]
# new_my_data.reset_index(drop=True, inplace=True)

## To select rows which names NOT contains MEGA:

# new_my_data = my_data.loc[~my_data['Name'].str.contains('a')]
# print(new_my_data)


## To use regex in filtering

# import re
#
# new_my_data = my_data.loc[my_data['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
# print(new_my_data)


## Conditional Changes

# my_data.loc[my_data['Speed'] > 100, ['Name', 'Type 1']] = ['Test1', 'Test2']
# print(my_data[['Name', 'Type 1']])


## Aggregate statistic Using Groupby




# my_data['count'] = 1
# new_my_data = my_data.groupby(['Type 1', 'Type 2']).count()['count']
# print(new_my_data)
# new_my_data.to_csv('new_my_data.csv')
