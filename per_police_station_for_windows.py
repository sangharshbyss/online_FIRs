
""""""
1. All districts, all police stations,
2. seperate webdriver for each police station to hide
3. out put in two files. one district one entire state.
"""

import os
import time
from builtins import ConnectionError, ConnectionRefusedError
from sys import argv

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, \
    TimeoutException, \
    WebDriverException, \
    ElementNotInteractableException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from urllib3.exceptions import MaxRetryError, NewConnectionError

import FIR_modules
from proxies import list_of_proxies

# constants
# define download directory
base_directory = r'D:\sangharsh\FIR Download\december'
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


mha_unite_list = []
mha_police_station = []
mha_number_of_records = []
mha_poa_cases = []

mha_downloaded = []
for name in ALL_Districts[int(argv[3]):int(argv[4]):]:
    time.sleep(8)

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
    myProxy, fake = list_of_proxies()
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

        district_dictionary = {"Unit": name,
                               "Police_Station": "bug",
                               "Number of Records": "bug",
                               "PoA Cases": "BLANK",
                               }
        df = pd.DataFrame(
            {key: pd.Series(value) for key, value in district_dictionary.items()})
        df.to_csv(
            os.path.join(base_directory, "summary", f'{name} _{argv[1]} to {argv[2]}.csv'))
        time.sleep(20)

        continue
    # call function for entering date, set the date through command line
    FIR_modules.enter_date(date1=argv[1], date2=argv[2], driver=driver)
    # call function district, for now its Dhule. will change latter to command line
    FIR_modules.district_selection(name, driver=driver)
    try:
        names_police = FIR_modules.police_stations(driver=driver)
    except (NoSuchElementException,
            WebDriverException,
            TimeoutException, ConnectionRefusedError,
            MaxRetryError, ConnectionError, NewConnectionError):
        print(f'police stations not loaded @ {name}')

        district_dictionary = {"Unit": name,
                               "Police_Station": "bug",
                               "Number of Records": "bug",
                               "PoA Cases": "BLANK",
                               }
        df = pd.DataFrame(
            {key: pd.Series(value) for key, value in district_dictionary.items()})
        df.to_csv(
            os.path.join(base_directory, "summary", f'{name} _{argv[1]} to {argv[2]}.csv'))
        time.sleep(60)
        continue

    driver.quit()
    # creation of list. This list will be converted to dictionary to write to csv
    police_dictionary = []
    total_records_dictionary = []
    poa_dictionary = []
    for police in names_police:
        time.sleep(4)

        status = []
        try:
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
                                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 "
                                   "(KHTML, like Gecko) Version/11.1.2 Safari/605.1.15")
            profile.set_preference("dom.webdriver.enabled", False)
            profile.set_preference('useAutomationExtension', False)
            profile.set_preference("pdfjs.disabled", True)
            profile.update_preferences()
            myProxy, police_proxy = list_of_proxies()
            proxy = Proxy({
                'proxyType': ProxyType.MANUAL,
                'httpProxy': police_proxy[names_police.index(police)],
                'ftpProxy': police_proxy[names_police.index(police)],
                'sslProxy': police_proxy[names_police.index(police)],
                'noProxy': ''  # set this value as desired
            })
            driver = webdriver.Firefox(firefox_profile=profile)
            open_page()
            # call function for entering date, set the date through command line
            FIR_modules.enter_date(date1=argv[1], date2=argv[2], driver=driver)

            # call function district, for now its Dhule. will change latter to command line
            FIR_modules.district_selection(name, driver=driver)

            FIR_modules.select_police_station(police, driver=driver)
        except (NoSuchElementException,
                WebDriverException,
                TimeoutException, ConnectionRefusedError,
                MaxRetryError, ConnectionError, NewConnectionError):
            print(f' bug {name}, {police}')

            police_dictionary.append(police)
            total_records_dictionary.append("bug")
            poa_dictionary.append("bug")

            status.append("bug")
            driver.quit()
            time.sleep(70)
            continue
        # call the value of records to view @ 50
        FIR_modules.view_record(driver)
        # call search
        FIR_modules.search(driver=driver)
        record = FIR_modules.number_of_records(driver=driver)
        if record == '':
            print(f'page not loaded for \n'
                  f'{police} @ {name} \n\n\n')

            driver.quit()
            poa_cases, non_poa_cases = FIR_modules.check_the_act(driver)
            police_dictionary.append("REPEAT")
            total_records_dictionary.append("REPEAT")
            poa_dictionary.append("REPEAT")

            status.append("REPEAT")
            time.sleep(60)
            break
        print(f'{name} {police} {record}')
        if int(record) > 0:
            with open(os.path.join(
                    base_directory,
                    "police_station_table",
                    f'{police}_full page.txt'), 'w', encoding="utf-8") as file:
                file.write(f'{driver.page_source} \n')
                file.close()
        else:
            police_dictionary.append(police)
            total_records_dictionary.append(record)
            poa_dictionary.append("Not Applicable")

            status.append("Not Applicable")
            mha_unite_list.append(name)
            mha_police_station.append(police)
            mha_number_of_records.append(record)
            mha_poa_cases.append("not applicable")
            mha_downloaded.append("not applicable")
            driver.quit()
            continue
        poa_cases = FIR_modules.check_the_act(driver)
        if not poa_cases:
            print('no poa')
            driver.quit()
            police_dictionary.append(police)
            total_records_dictionary.append(record)
            poa_dictionary.append(0)
            status.append("Not Applicable")
            mha_unite_list.append(name)
            mha_police_station.append(police)
            mha_number_of_records.append(record)
            mha_poa_cases.append(0)
            mha_downloaded.append("not applicable")
            continue
        else:

            try:
                FIR_modules.download_repeat(poa_cases, driver)
                police_dictionary.append(police)
                total_records_dictionary.append(record)
                poa_dictionary.append(len(poa_cases))

                status.append("Done")
                mha_unite_list.append(name)
                mha_police_station.append(police)
                mha_number_of_records.append(record)
                mha_poa_cases.append(len(poa_cases))
                mha_downloaded.append("done")
            except (WebDriverException, TimeoutException,
                    NoSuchElementException):
                print("download failed")
                police_dictionary.append(police)
                total_records_dictionary.append(record)
                poa_dictionary.append(len(poa_cases))

                status.append("failed")
                driver.quit()
                time.sleep(30)
                continue
            except ElementNotInteractableException:
                print("Element not interactable")
                police_dictionary.append(police)
                total_records_dictionary.append(record)
                poa_dictionary.append(len(poa_cases))

                status.append("failed")
                driver.quit()
                time.sleep(30)
                continue
    district_dictionary = {"Unit": name,
                           "Police_Station": police_dictionary,
                           "Number of Records": total_records_dictionary,
                           "PoA Cases": poa_dictionary,

                           }

    df = pd.DataFrame(
        {key: pd.Series(value) for key, value in district_dictionary.items()})
    df.to_csv(
        os.path.join(base_directory, "summary", f'{name} _{argv[1]} to {argv[2]}.csv'))
    driver.quit()
mha_records = {"Unit": mha_unite_list,
               "Police_Station": mha_police_station,
               "Number of Records": mha_number_of_records,
               "PoA Cases": mha_poa_cases,

               }
df = pd.DataFrame(
    {key: pd.Series(value) for key, value in mha_records.items()})
df.to_csv(
    os.path.join(base_directory, "summary", f'{argv[5]}_{argv[1]} to {argv[2]}.csv')
