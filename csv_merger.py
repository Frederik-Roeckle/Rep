import os
import pandas as pd

# set directory of csv files
filedir = "D:\APMProject\process-complexity"

filenames = [
    "2020_DomesticDeclarations_metrics.csv",
    "2020_InternationalDeclarations_metrics.csv",
    "2020_PermitLog_metrics.csv",
    "2020_PrepaidTravelCost_metrics.csv",
    "2020_RequestForPayment_metrics.csv",
    "BPIC15_1_metrics.csv",
    "BPIC15_2_metrics.csv",
    "BPIC15_3_metrics.csv",
    "BPIC15_4_metrics.csv",
    "BPIC15_5_metrics.csv",
    "BPI_Challenge2017_metrics.csv",
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
combined_df.to_csv("merged.csv", index=False)
print('Saved merged.csv')