"""
1. All districts.
2. seperate webdriver for each district
3. improvement from per_dist_day.py for
4. separate summary of PoA cases.
5. Change download directory every month.
5. full proof.
including exact date in summary record.
"""

import os
import time
from builtins import ConnectionError, ConnectionRefusedError
from sys import argv

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, \
    TimeoutException, \
    WebDriverException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from urllib3.exceptions import MaxRetryError, NewConnectionError

import FIR_modules
from proxies4 import list_of_proxies

# constants
# define download directory
base_directory = r'/home/sangharsh/Documents/PoA/data/FIR/February'
download_directory = os.path.join(base_directory, "copies", f'{argv[1]} _ {argv[2]}')
if not download_directory:
    os.mkdir(download_directory)

main_url = r'https://citizen.mahapolice.gov.in/Citizen/MH/PublishedFIRs.aspx'

# list of districts
ALL_Districts = ['AHMEDNAGAR', 'AKOLA', 'AMRAVATI CITY', 'AMRAVATI RURAL', 'AURANGABAD CITY',
                 'AURANGABAD RURAL', 'BEED', 'BHANDARA', 'BRIHAN MUMBAI CITY', 'BULDHANA',
                 'CHANDRAPUR', 'DHULE', 'GADCHIROLI', 'GONDIA', 'HINGOLI', 'JALGAON', 'JALNA',
                 'KOLHAPUR', 'LATUR', 'NAGPUR CITY', 'NAGPUR RURAL', 'NANDED', 'NANDURBAR',
                 'NASHIK CITY', 'NASHIK RURAL', 'NAVI MUMBAI', 'OSMANABAD', 'PALGHAR', 'PARBHANI',
                 'PIMPRI-CHINCHWAD', 'PUNE CITY', 'PUNE RURAL', 'RAIGAD', 'RAILWAY AURANGABAD',
                 'RAILWAY MUMBAI', 'RAILWAY NAGPUR', 'RAILWAY PUNE', 'RATNAGIRI', 'SANGLI', 'SATARA',
                 'SINDHUDURG', 'SOLAPUR CITY', 'SOLAPUR RURAL', 'THANE CITY', 'THANE RURAL', 'WARDHA',
                 'WASHIM', 'YAVATMAL']

print(list(enumerate(ALL_Districts)))


def open_page():
    """
    open page and refresh it. without refreshing it dose not work
    """
    driver.get(main_url)
    driver.refresh()


# lists for taking cvs output
poa_dir_district = []
poa_dir_police = []
poa_dir_year = []
poa_dir_FIR = []
poa_dir_date = []
poa_dir_sec = []
mha_date = []
mha_unite_list = []
mha_number_of_records = []
mha_poa_cases = []
mha_downloaded = []
for name in ALL_Districts[int(argv[3]):int(argv[4]):]:

    district_dictionary = {"Unit": '', "Police_Station": '',
                           "Number of Records": '', "PoA Cases": '',
                           "Other Cases": ''}

    profile = webdriver.FirefoxProfile()
    # set profile for saving directly without pop-up ref -
    # https://stackoverflow.com/a/29777967
    profile.set_preference("browser.download.panel.shown", False)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    # profile.set_preference("browser.helperApps.neverAsk.openFile","application/pdf")
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.dir", download_directory)
    # to go undetected
    profile.set_preference("general.useragent.override",
                           "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) "
                           "Gecko/20100101 Firefox/82.0")
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.set_preference("pdfjs.disabled", True)
    profile.update_preferences()
    # change IP
    myProxy = list_of_proxies()
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': myProxy[ALL_Districts.index(name)],
        'ftpProxy': myProxy[ALL_Districts.index(name)],
        'sslProxy': myProxy[ALL_Districts.index(name)],
        'noProxy': ''  # set this value as desired
    })
    try:
        driver = webdriver.Firefox(firefox_profile=profile, proxy=proxy)
        open_page()
    except (NoSuchElementException,
            WebDriverException,
            TimeoutException, ConnectionRefusedError,
            MaxRetryError, ConnectionError, NewConnectionError):
        print(f'bug @ {name}, driver did not open')
        continue

    # call function for entering date, set the date through command line
    FIR_modules.enter_date(date1=argv[1], date2=argv[2], driver=driver)
    # call function district, for now its Dhule. will change latter to command line
    FIR_modules.district_selection(name, driver=driver)

    # creation of list. This list will be converted to dictionary to write to csv
    total_records_dictionary = []
    poa_dictionary = []
    # call the value of records to view @ 50
    time.sleep(2)
    FIR_modules.view_record(driver)
    # call search
    FIR_modules.search(driver=driver)
    record = FIR_modules.number_of_records(driver=driver)
    if record == '':
        print(f'page not loaded for \n'
              f'{name} @ {name} \n\n\n')

        driver.quit()
        poa_cases, non_poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                                             poa_dir_police,
                                                             poa_dir_year,
                                                             poa_dir_FIR,
                                                             poa_dir_date,
                                                             poa_dir_sec)

        total_records_dictionary.append("REPEAT")
        poa_dictionary.append("REPEAT")

        time.sleep(5)
        break
    print(f'{name}{record}')
    if int(record) > 0:
        print('scanning records...')
    else:
        mha_date.append(argv[1])
        mha_unite_list.append(name)
        mha_number_of_records.append(record)
        mha_poa_cases.append("0")
        mha_downloaded.append("0")
        driver.quit()
        print('no records')
        continue
    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)
    if not poa_cases:
        print('no poa. go to next page')

    else:
        FIR_modules.download_repeat(poa_cases, driver,
                                    )

    if int(record) > 50:
        FIR_modules.second_page(driver)
    else:
        driver.quit()
        continue
    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)
    if not poa_cases:
        print('no poa. go to next page')

    else:
        print("PoA")
        FIR_modules.download_repeat(poa_cases, driver,
                                    )

    if int(record) > 100:
        print('going to page 3')
        FIR_modules.third_page(driver)
    else:
        driver.quit()
        continue
    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)
    if not poa_cases:
        print('no poa')
    else:
        print("PoA")
        FIR_modules.download_repeat(poa_cases, driver,
                                    )

    if int(record) > 150:
        print('going to page 4')
        FIR_modules.forth_page(driver)
    else:
        driver.quit()
        continue
    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)
    if not poa_cases:
        print('no poa')
        driver.quit()
        continue
    else:
        print("PoA")
        FIR_modules.download_repeat(poa_cases, driver,
                                    )
        total_records_dictionary.append(record)
        poa_dictionary.append(len(poa_cases))

    driver.quit()
mha_records = {"Date": mha_date,
               "Unit": mha_unite_list,
               "Number of Records": mha_number_of_records,
               "PoA Cases": mha_poa_cases,
               "Downloaded": mha_downloaded,
               }
df = pd.DataFrame(
    {key: pd.Series(value) for key, value in mha_records.items()})
df.to_csv(
    os.path.join(base_directory, "summary", f'{argv[5]}_{argv[1]} to {argv[2]}.csv'))
poa_dir = {"District": poa_dir_district, "Police_Station": poa_dir_police,
           "FIR": poa_dir_FIR, "Date_&_Time": poa_dir_date, "Acts_&_Sections": poa_dir_sec}

df = pd.DataFrame(
    {key: pd.Series(value) for key, value in poa_dir.items()})
print(df)
df.to_csv(
    os.path.join(base_directory, "poa_summary", f'{argv[5]}_from_{argv[1]}_to_{argv[2]}.csv'))
