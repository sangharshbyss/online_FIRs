import os


def poa_district_summary(poa_summary_list, district, police_station,date):
    """convert list of cases in csv file
    1. column headings are set with variables
    2. list generated from main function, to be used as parameter
    3. district is current district
    4. date is same as command line argument from main.
    """
    directory = '/home/sangharsh/Documents/data/FIR_Data/summary'
    with open(os.path.join(directory, f'{district}_{police_station}{date}.txt'), 'w') as f:
        f.write(f"{poa_summary_list}")
        f.close()

def non_poa_district_summary(non_poa_list, district, police_station, date):
    directory = '/home/sangharsh/Documents/data/FIR_Data/summary'
    with open(os.path.join(directory, f'alt_{district}_{police_station}{date}.txt'), 'w') as f:
        f.write(f"{non_poa_list}")
        f.close()

