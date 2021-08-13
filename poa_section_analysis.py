import pandas as pd
import os

os.chdir('/home/sangharsh/Documents/PoA'
         '/data/FIR/January2/poa_summary')
df = pd.read_csv('combined_csv.csv')
print(df.columns)
