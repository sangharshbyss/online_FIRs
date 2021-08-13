"""
Module to divide acts and create separate column for
PoA, IPC and PCR.
Also converts Marathi names in English short forms.
"""
import pandas as pd
import os
import re


os.chdir('/home/sangharsh/Documents/PoA'
         '/data/FIR/January2/poa_summary')
pd.options.display.width = 0
df = pd.read_csv('combined_csv.csv')
# taking IPC, PCR and PoA seperately. And creating seperate columns.
df["IPC"] = df['Acts_&_Sections'].str.extract(".*?(भारतीय दंड संहिता १८६०.*?);")
df["PoA"] = df['Acts_&_Sections'].str.extract(".*?(अनुसूचीत जाती आणि अनुसूचीत जमाती.*?);")
df["PCR"] = df['Acts_&_Sections'].str.extract(".*?(नागरी हक्‍.*?);")
df["IPC"] = df["IPC"].str.replace(r"(भारतीय दंड संहिता.*?१८६०,)", "IPC")
df["PoA"] = df["PoA"].str.replace(r"(अनुसूचीत जाती आणि अनुसूचीत जमाती.*?१९८९)", "PoA")
df["PCR"] = df["PCR"].str.replace(r"(नागरी हक्‍क संरक्षण अधिनियम,.*?१९५५)", "PCR")

#from here onwards create a separate module afterwards
# translate sections to English (IPC)

# copy the cell
# open selnium driver
# open google translate
# click in search box for input language
# tyape marathi
# in input box paste the copied content
# copy content in translated box
# paste the copied content back in to the cell.
for row in df['IPC']:

"""for ind in df.index:
    
    df.at[ind, 'IPC'] = 'some value'
    break"""
print(df['IPC'])

