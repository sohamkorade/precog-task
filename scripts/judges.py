import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read the csv file
df = pd.read_csv('csv/judges_clean.csv')

# strip rows where end_date is null
df = df[df['end_date'].notnull()]

# get tenure
df['tenure'] = (pd.to_datetime(df['end_date'], dayfirst=True) -
                pd.to_datetime(df['start_date'], dayfirst=True)).dt.days / 365

# print(df.head())

# plot the data

# male vs female
# count
sns.countplot(data=df, x='female_judge')
# tenure
sns.catplot(data=df, x='female_judge', y='tenure')

plt.show()