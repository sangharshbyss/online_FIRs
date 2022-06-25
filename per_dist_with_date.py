"""
1. separate webdriver for each district
3. improvement from per_dist_day.py
4. Change download directory every month.
5. full proof.
6. headless
"""

import os
import time
from sys import argv

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

import FIR_modules
from proxies3 import list_of_proxies

# constants
# define download directory
base_directory = r'/home/sangharsh/Documents/PoA/data/FIR/April_22'
download_directory = os.path.join(base_directory, "copies", f'{argv[1]} _ {argv[2]}')

if not download_directory:
    os.mkdir(download_directory)

main_url = r'https://citizen.mahapolice.gov.in/Citizen/MH/PublishedFIRs.aspx'

# list of districts
ALL_Districts = ['AHMEDNAGAR', 'AKOLA', 'AMRAVATI CITY', 'AMRAVATI RURAL', 'AURANGABAD CITY',
                 'AURANGABAD RURAL', 'BEED', 'BHANDARA', 'BRIHAN MUMBAI CITY', 'BULDHANA',
                 'CHANDRAPUR', 'DHULE', 'GADCHIROLI', 'GONDIA', 'HINGOLI', 'JALGAON', 'JALNA',
                 'KOLHAPUR', 'LATUR', 'Mira-Bhayandar, Vasai-Virar Police Commissioner',
                 'NAGPUR CITY', 'NAGPUR RURAL', 'NANDED', 'NANDURBAR',
                 'NASHIK CITY', 'NASHIK RURAL', 'NAVI MUMBAI', 'OSMANABAD', 'PALGHAR', 'PARBHANI',
                 'PIMPRI-CHINCHWAD', 'PUNE CITY', 'PUNE RURAL', 'RAIGAD', 'RAILWAY AURANGABAD',
                 'RAILWAY MUMBAI', 'RAILWAY NAGPUR', 'RAILWAY PUNE', 'RATNAGIRI', 'SANGLI', 'SATARA',
                 'SINDHUDURG', 'SOLAPUR CITY', 'SOLAPUR RURAL', 'THANE CITY', 'THANE RURAL', 'WARDHA',
                 'WASHIM', 'YAVATMAL']


# print(list(enumerate(ALL_Districts)))

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

# list for terminal output
dist_name = []
dist_total = []
dist_poa = []

for name in ALL_Districts:

    district_dictionary = {"Unit": '', "Police_Station": '',
                           "Number of Records": '', "PoA Cases": '',
                           "Other Cases": ''}

    # profile = webdriver.FirefoxProfile()
    # set profile for saving directly without pop-up ref -
    # https://stackoverflow.com/a/29777967
    options = Options()

    options.set_preference("browser.download.panel.shown", False)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    # profile.set_preference("browser.helperApps.neverAsk.openFile","application/pdf")
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", download_directory)
    # to go undetected
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) "
                           "Gecko/20100101 Firefox/82.0")
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference('useAutomationExtension', False)
    options.set_preference("pdfjs.disabled", True)
    service = Service('C:\\BrowserDrivers\\geckodriver.exe')
    options.headless = True

    # change IP
    myProxy = list_of_proxies()
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': myProxy[ALL_Districts.index(name)],
        'ftpProxy': myProxy[ALL_Districts.index(name)],
        'sslProxy': myProxy[ALL_Districts.index(name)],
        'noProxy': ''  # set this value as desired
    })

    driver = webdriver.Firefox(options=options, proxy=proxy)
    open_page()
    # for terminal output
    number_of_cases_on_all_pages = []
    print(f'\n {name} in progress...')
    FIR_modules.enter_date(date1=argv[1], date2=argv[2], driver=driver)

    FIR_modules.district_selection(name, driver=driver)

    # creation of lists. These lists will be converted to dictionary to write to csv
    dist_name.append(name)
    poa_dictionary = []
    # call the value of records to view @ 50
    time.sleep(1)
    FIR_modules.view_record(driver)
    # call search
    FIR_modules.search(driver=driver)
    time.sleep(2)
    record = FIR_modules.number_of_records(driver=driver)
    # for terminal output
    dist_total.append(record)
    if record == '':
        print(f'page not loaded for \n'
              f'{name} @ {name} \n\n\n')

        driver.quit()
        break
    print(f'total records {record}')

    if int(record) > 0:
        print('scanning records...')
    else:
        driver.quit()
        print(f'no records. {name} finished')
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
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        print(number_of_cases_on_page, number_of_cases_on_all_pages)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )

    if int(record) > 50:
        print('page 2')
        FIR_modules.second_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue
    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)

    if not poa_cases:
        print('no poa.')

    else:
        print("PoA")
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        print(number_of_cases_on_page, number_of_cases_on_all_pages)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )

    if int(record) > 100:
        print('going to page 3')
        FIR_modules.third_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
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
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )

    if int(record) > 150:
        print('going to page 4')
        FIR_modules.forth_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
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
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )
    if int(record) > 200:
        print('going to page 5')
        FIR_modules.fifth_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue
    time.sleep(3)
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
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        print(number_of_cases_on_page, number_of_cases_on_all_pages)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )
    if int(record) > 250:
        print('going to page 6')
        FIR_modules.sixth_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue
    time.sleep(3)
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
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )
    if int(record) > 300:
        print('going to page 7')
        FIR_modules.seventh_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
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
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )
    if int(record) > 350:
        print('going to page 8')
        FIR_modules.eightth_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue
    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)
    if poa_cases:
        print("PoA")
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )

    else:
        print('no poa')

    if int(record) > 400:
        print('going to page 9')
        FIR_modules.ninenth_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue
    time.sleep(3)
    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)
    if poa_cases:
        print("PoA")
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )
    else:
        print('no poa')
    if int(record) > 450:
        print('going to page 10')
        FIR_modules.tenth_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)
    if poa_cases:
        print("PoA")
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )

    else:
        print('no poa')

    if int(record) > 500:
        print('going to 11th page')
        FIR_modules.next_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
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
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )

    if int(record) > 550:
        print('going to 12th page')
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.twelth_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue
    time.sleep(3)
    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)
    if poa_cases:
        print("PoA")
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )
    else:
        print('no poa')

    if int(record) > 600:
        print('going to 13th page')
        FIR_modules.thirteen_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue
    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)
    if poa_cases:
        print("PoA")
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )

    else:
        print('no poa')

    if int(record) > 650:
        print('going to 14th page')
        FIR_modules.fourteen_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue
    time.sleep(3)
    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)
    if poa_cases:
        print("PoA")
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )
    else:
        print('no poa')

    if int(record) > 700:
        print('going to 15th page')
        FIR_modules.next_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue
    time.sleep(3)
    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)
    if poa_cases:
        print("PoA")
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )
    else:
        print('no poa')

    if int(record) > 750:
        print('going to 16th page')
        FIR_modules.sixteen_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue
    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)
    if poa_cases:
        print("PoA")
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )
    else:
        print('no poa')

    if int(record) > 800:
        print('going to 17th page')
        FIR_modules.seventeen_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue
    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)
    if poa_cases:
        print("PoA")
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )
    else:
        print('no poa')

    if int(record) > 850:
        print('going to 18th page')
        FIR_modules.eighteen_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue
    time.sleep(3)
    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)
    if poa_cases:
        print("PoA")
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )
    else:
        print('no poa')

    if int(record) > 900:
        print('going to 19th page')
        FIR_modules.ninteen_page(driver)
    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
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
        time.sleep(3)
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        FIR_modules.download_repeat(poa_cases, driver,
                                    )

    if int(record) > 950:
        print('going to 20th page')
        FIR_modules.twenty_page(driver)

    else:
        driver.quit()
        print(f'{name} finished')
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue
    poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                          poa_dir_police,
                                          poa_dir_year,
                                          poa_dir_FIR,
                                          poa_dir_date,
                                          poa_dir_sec)
    if not poa_cases:
        print('no poa')
        number_of_cases_on_page = int(len(poa_cases))
        number_of_cases_on_all_pages.append(number_of_cases_on_page)
        driver.quit()
        print(f'{name} finished')
        continue

    else:
        print("PoA")
        FIR_modules.download_repeat(poa_cases, driver,
                                    )
        poa_dictionary.append(len(poa_cases))
    dist_poa.append(sum(number_of_cases_on_all_pages))
    print(dist_poa)
    driver.quit()

terminal_dir = {"District": dist_name, "Total": dist_total, "PoA": dist_poa}
poa_dir = {"District": poa_dir_district, "Police_Station": poa_dir_police,
           "FIR": poa_dir_FIR, "Date_&_Time": poa_dir_date, "Acts_&_Sections": poa_dir_sec}
terminal_df = pd.DataFrame({key: pd.Series(value) for key, value in terminal_dir.items()})
df = pd.DataFrame(
    {key: pd.Series(value) for key, value in poa_dir.items()})
print(terminal_df)
terminal_df.to_csv(os.path.join(base_directory, f'statistical_summary_from_{argv[1]}_to_{argv[2]}.csv'))
df.to_csv(
    os.path.join(base_directory, "poa_summary", f'{argv[3]}_from_{argv[1]}_to_{argv[2]}.csv'))
