import pandas as pd
import os


def poa_district_summary(poa_summary_list, district, date):
    """convert list of cases in csv file
    1. column headings are set with variables
    2. list generated from main function, to be used as parameter
    3. district is current district
    4. date is same as command line argument from main.
    """
    COLUMNS = ['Sr.No.', 'State', 'District', 'Police Station', 'Year', 'FIR No.', 'Registration Date', 'FIR No',
           'Sections']
    directory = '/home/sangharsh/Documents/data/FIR_Data/summary'
    district_data = pd.DataFrame(poa_summary_list, columns=COLUMNS)
    with open(os.path.join(directory, f'{district}{date}.csv'), 'w') as f:
        district_data.to_csv(os.path.join(directory, f'{district}{date}.csv'))

