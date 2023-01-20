"""
This script creates a json file with state codes and names.
also for districts.
"""

import pandas as pd
import json

# for states

# read the csv file
df = pd.read_csv('csv/keys/keys/cases_state_key.csv')

# only keep the columns we need
df = df[['state_code', 'state_name']]

# drop duplicates and sort by state code
df = df.drop_duplicates().sort_values('state_code')
# print(df)

states = {}
# create a dictionary from the dataframe
for index, row in df.iterrows():
    states[row['state_code']] = row['state_name']
# print(states)

# save as a json file
with open('json/state_codes.json', 'w') as f:
    json.dump(states, f, indent=4)

# for districts

# read the csv file
df = pd.read_csv('csv/keys/keys/cases_district_key.csv')

# only keep the columns we need
df = df[['state_code', 'dist_code', 'district_name']]
# print(df)

# drop duplicates and sort by state code and district code
df = df.drop_duplicates().sort_values(['state_code', 'dist_code'])
# print(df)

# create a dictionary from the dataframe

# ensure each state is covered
districts = {i: {} for i in states.keys()}
# print(districts)

for index, row in df.iterrows():
    if row['state_code'] not in districts:
        districts[row['state_code']] = {}
    districts[row['state_code']][row['dist_code']] = row['district_name']
# print(districts)

# save as a json file
with open('json/district_codes.json', 'w') as f:
    json.dump(districts, f, indent=4)