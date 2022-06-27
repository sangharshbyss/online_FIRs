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
                 'AURANGABAD RURAL', 'BEED', 'BHANDARA', 'BULDHANA',
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
# list for generating separate output to the file.
# further this list will be converted to dictionary and then to pandas dataFrame.
dist_name = []
dist_total = []
dist_poa = []

# terminal output
print(f'{argv[1]}\n')

for name in ALL_Districts:

    # variables
    number_of_cases_on_all_pages = []
    poa_dictionary = []
    district_dictionary = {"Unit": '', "Police_Station": '',
                           "Number of Records": '', "PoA Cases": '',
                           "Other Cases": ''}

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
    # enter the date through terminal argument
    FIR_modules.enter_date(date1=argv[1], date2=argv[2], driver=driver)
    # enter the name of the district. select one from the list
    FIR_modules.district_selection(name, driver=driver)
    # creation of list. These lists will be converted to dictionary to write to csv
    dist_name.append(name)
    # call the value of records to view @ 50
    time.sleep(1)
    FIR_modules.view_record(driver)
    # call search
    FIR_modules.search(driver=driver)
    record = FIR_modules.number_of_records(driver=driver)
    # for terminal output and separate file output
    dist_total.append(record)

    if int(record) > 0:
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        # this is very rare
        # no records on page so the PoA cases on page will be 0.
        # this 0 needs to be added as the list will be converted to dictionary
        dist_poa.append(0)
        continue

    if int(record) > 50:
        FIR_modules.second_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)

        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        # append the list of dist PoAs with total sum of number of cases on all pages
        # for records up to 50 it will be only one record
        # - that is from 0 to 50, if at all available
        dist_poa.append(sum(number_of_cases_on_all_pages))
        driver.quit()
        continue

    if int(record) > 100:
        FIR_modules.third_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )

    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 150:
        FIR_modules.forth_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 200:
        FIR_modules.fifth_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 250:
        FIR_modules.sixth_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 300:
        FIR_modules.seventh_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 350:
        FIR_modules.eightth_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 400:
        FIR_modules.ninenth_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 450:
        FIR_modules.tenth_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 500:
        FIR_modules.next_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 550:
        FIR_modules.twelth_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 600:
        FIR_modules.thirteen_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 650:
        FIR_modules.fourteen_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 700:
        FIR_modules.next_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 750:
        FIR_modules.sixteen_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 800:
        FIR_modules.seventeen_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 850:
        FIR_modules.eighteen_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 900:
        FIR_modules.ninteen_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))
        continue

    if int(record) > 950:
        FIR_modules.twenty_page(driver)
        poa_cases = FIR_modules.check_the_act(driver, poa_dir_district,
                                              poa_dir_police,
                                              poa_dir_year,
                                              poa_dir_FIR,
                                              poa_dir_date,
                                              poa_dir_sec)
        if not poa_cases:
            number_of_cases_on_all_pages.append(0)
        else:
            number_of_cases_on_page = int(len(poa_cases))
            number_of_cases_on_all_pages.append(number_of_cases_on_page)
            FIR_modules.download_repeat(poa_cases, driver,
                                        )
    else:
        driver.quit()
        dist_poa.append(sum(number_of_cases_on_all_pages))

terminal_dir = {"District": dist_name, "Total": dist_total, "PoA": dist_poa}
poa_dir = {"District": poa_dir_district, "Police_Station": poa_dir_police,
           "FIR": poa_dir_FIR, "Date_&_Time": poa_dir_date, "Acts_&_Sections": poa_dir_sec}
terminal_df = pd.DataFrame({key: pd.Series(value) for key, value in terminal_dir.items()})
df = pd.DataFrame(
    {key: pd.Series(value) for key, value in poa_dir.items()})
terminal_df.to_csv(os.path.join(base_directory, f'statistical_summary_from_{argv[1]}_to_{argv[2]}.csv'))
df.to_csv(
    os.path.join(base_directory, "poa_summary", f'{argv[3]}_from_{argv[1]}_to_{argv[2]}.csv'))
print(f'Highest records in District:'
      f'\n {terminal_df[terminal_df.Total == terminal_df.Total.max()]}'
      f'\n Highest number of PoA cases in District:'
      f'\n {terminal_df[terminal_df.PoA == terminal_df.PoA.max()]}')
