import os
import pandas as pd

os.chdir('/home/sangharsh/Documents/PoA/data/FIR/December/summary/01_06_Jan_all')
df = pd.read_csv("combined_csv.csv")
sorted_df = df.sort_values("Unit")
print(sorted_df)
sorted_df.loc[(df["Unit"].duplicated()), ["Unit"]]= " "

sorted_df.to_csv("solved.csv", index=False, encoding='utf-8-sig')
