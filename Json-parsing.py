import pandas as pd
import json

table = pd.read_json('data.json')
print(table)
transposed = table.transpose().reset_index()
transposed.columns = ['Fullname', 'Age', 'Address', 'Occupation']
print(transposed)
transposed.to_csv("data.csv", index=False)
new = transposed["Fullname"].str.split(" ", n=1, expand=True)
new.columns = ['Firstname', 'Lastname']
split = transposed.drop(['Fullname'], axis=1)
newtable = new.join(split)
print(newtable)
Lastnames = newtable['Lastname'].unique()
LastnameAmounts = newtable.groupby(['Lastname'], sort=False).count()
Ages = newtable.groupby(['Lastname', 'Age'], sort=False).count()
print(LastnameAmounts)
i=0
while i < len(Lastnames):
    
    i += 1
counts = pd.DataFrame()