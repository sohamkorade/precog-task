csv_path = "csv/cases/cases/"

import glob
import pandas as pd
from pandas_profiling import ProfileReport

files = glob.glob(csv_path + "*.csv")
files = ["csv/keys/keys/cases_district_key.csv"]

for file in files:
    # if "small" not in file:
    #     continue
    print(file)
    df = pd.read_csv(file)
    profile = ProfileReport(df)
    profile.to_file(file[:-3] + "html")
