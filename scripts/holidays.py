import pandas as pd

# read csv
df = pd.read_csv('../data/holidays.csv')

# convert to datetime
df['date'] = pd.to_datetime(df['date'])


def is_holiday(day, month, year):
    """Check if date is a holiday"""
    date = pd.to_datetime(f'{year}-{month}-{int(day)}')
    return date in df['date'].values


def get_holiday(day, month, year):
    """Get holiday name"""
    date = pd.to_datetime(f'{year}-{month}-{int(day)}')
    return df[df['date'] == date]['holiday'].values[0]