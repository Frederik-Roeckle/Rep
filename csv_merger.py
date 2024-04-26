import os
import pandas as pd

# set directory of csv files
filedir = "data"

filenames = [
    "BPI_Challenge_2012_metrics.csv",
    "Sepsis_Cases_metrics.csv",
    "Hospital_Billing_metrics.csv"
]

combined_df = None

for filename in filenames:
    filepath = os.path.join(filedir, filename)
    filedf = pd.read_csv(filepath)

    filedf["File"] = filename

    if combined_df is None:
        combined_df = filedf
    else:
        combined_df = pd.merge(combined_df, filedf, how="outer")

# print(combined_df.head())
combined_df.to_csv("generated_merged.csv", index=False)
print('Saved merged.csv')
