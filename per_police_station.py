"""
Check if every police station has uploaded at least one FIR/3months.
Draw the list of police stations who have not done so.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, \
    TimeoutException, \
    WebDriverException, \
    ElementNotInteractableException
from urllib3.exceptions import MaxRetryError, NewConnectionError, ConnectionError
from builtins import ConnectionError, ConnectionRefusedError
from sys import argv
import time
import os
import pandas as pd

# constants
# define download directory
base_directory = r'/home/sangharsh/Documents/PoA/data/FIR'
download_directory = os.path.join(base_directory, "copies")
main_url = r'https://citizen.mahapolice.gov.in/Citizen/MH/PublishedFIRs.aspx'
# trying with firefox

# constants


# list for number of PoA FIRs & non PoA

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


# functions
# 1. open url

def open_page():
    """
    open page and refresh it. without refreshing it dose not work
    """
    driver.get(main_url)
    driver.refresh()


""" 
2. function for date to-from. same as in only details of one data will be collected.
this function needs ActionChains otherwise the dates are not getting entered. 
date will be entered through command line
"""


def enter_date(date1, date2):
    WebDriverWait(driver, 160).until(
        ec.presence_of_element_located((By.CSS_SELECTOR,
                                        '#ContentPlaceHolder1_txtDateOfRegistrationFrom')))
    from_date_field = driver.find_element_by_css_selector(
        '#ContentPlaceHolder1_txtDateOfRegistrationFrom')

    to_date_field = driver.find_element_by_css_selector(
        '#ContentPlaceHolder1_txtDateOfRegistrationTo')

    ActionChains(driver).click(from_date_field).send_keys(
        date1).move_to_element(to_date_field).click().send_keys(
        date2).perform()


# 3 select district and enter
def district_selection(dist_name):
    dist_list = Select(driver.find_element_by_css_selector(
        "#ContentPlaceHolder1_ddlDistrict"))

    dist_list.select_by_visible_text(dist_name)
    time.sleep(3)


# 4. List police station
def police_stations():
    WebDriverWait(driver, 160).until(
        ec.presence_of_element_located((By.CSS_SELECTOR,
                                        '#ContentPlaceHolder1_ddlPoliceStation')))
    select_box = driver.find_element_by_css_selector("#ContentPlaceHolder1_ddlPoliceStation")
    all_police_stations = [
        x.text for x in select_box.find_elements_by_tag_name("option") if x.text != "Select"]
    return all_police_stations


# select police station
def select_police_station(selected_police):
    # this will select police station as per there names listed in
    # list created by police_stations() function.
    police_list = Select(driver.find_element_by_css_selector(
        '#ContentPlaceHolder1_ddlPoliceStation'))
    police_list.select_by_visible_text(selected_police)


# 5. view 50 records at a time
def view_record():
    view = Select(driver.find_element_by_id('ContentPlaceHolder1_ucRecordView_ddlPageSize'))
    view.select_by_value("50")


# 4. function for click on search
def search():
    driver.find_element_by_css_selector('#ContentPlaceHolder1_btnSearch').click()
    time.sleep(4)


def number_of_records():
    total_number = driver.find_element_by_css_selector(
        '#ContentPlaceHolder1_lbltotalrecord').text
    return total_number


# 5 check if it has PoA if yes, create a list of how many cases
def check_the_act():
    poa_list = []
    non_poa = []
    # check for PoA in table.
    # identify table first
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((
            By.CSS_SELECTOR, "#ContentPlaceHolder1_gdvDeadBody")))
    table = driver.find_element(By.ID, "ContentPlaceHolder1_gdvDeadBody")
    rows = table.find_elements(By.TAG_NAME, "tr")
    # iterate over each row
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        # iterate over each cell
        for cell in cells:
            cell_text = cell.text
            # if the act is found, count it. and take details.
            if "अनुसूचीत जाती आणि अनुसूचीत" in cell_text:
                poa_list.append(row.text)
            else:
                non_poa.append(row.text)
    return poa_list, non_poa


def download_repeat(some_list):
    i = 0
    while i <= len(some_list) - 1:
        time.sleep(2)
        table = driver.find_element(By.ID, "ContentPlaceHolder1_gdvDeadBody")
        rows = table.find_elements(By.TAG_NAME, "tr")
        main_window = driver.current_window_handle
        new_list = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            # iterate over each cell
            for cell in cells:
                cell_text = cell.text
                # if the act is found, count it. and take details.
                if "अनुसूचीत जाती आणि अनुसूचीत" in cell_text:
                    download_link = row.find_element(By.TAG_NAME, "input")
                    new_list.append(download_link)
                else:
                    continue
        print('downloading...')
        time.sleep(2)
        new_list[i].click()
        time.sleep(8)
        for handle in driver.window_handles:
            if handle != main_window:
                download_window = handle
                # we are in main window, so go to next window
                driver.switch_to.window(download_window)
        driver.find_element_by_id(
            "ReportViewer1_ctl06_ctl04_ctl00_ButtonImgDown").click()
        down_load = driver.find_element_by_css_selector(
            "#ReportViewer1_ctl06_ctl04_ctl00_Menu > div:nth-child(4) > a:nth-child(1)"
        )
        time.sleep(2)
        down_load.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.close()
        print('finished')
        driver.switch_to.window(main_window)
        i += 1
    driver.quit()


# 6. main code
with open(os.path.join(
        download_directory, "bug", f'bug_report_0.txt'), 'w') as file:
    file.write('bug report \n\n')
    file.close()

for name in ALL_Districts:
    time.sleep(60)
    try:
        district_dictionary = {"Unite": '', "Police_Station": '',
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
        driver = webdriver.Firefox(firefox_profile=profile)
        open_page()
    except (NoSuchElementException,
            WebDriverException,
            TimeoutException, ConnectionRefusedError,
            MaxRetryError, ConnectionError, NewConnectionError):
        print(f'bug @ {name}')
        with open(os.path.join(download_directory, "bug" f'bug_report_0.txt'), 'a') as file:
            file.write(f'{name}, "-" \n')
        district_dictionary = {"Unite": name,
                               "Police_Station": "bug",
                               "Number of Records": "bug",
                               "PoA Cases": "BLANK",
                               "Other Cases": "BLANK"}
        df = pd.DataFrame(
            {key: pd.Series(value) for key, value in district_dictionary.items()})
        df.to_csv(
            os.path.join(base_directory, "summary", f'{name} _{argv[1]} to {argv[2]}.csv'))
        time.sleep(60)
        continue
    # call function for entering date, set the date through command line
    enter_date(date1=argv[1], date2=argv[2])
    # call function district, for now its Dhule. will change latter to command line
    district_selection(name)
    names_police = police_stations()
    driver.quit()
    # creation of list. This list will be converted to dictionary to write to csv
    police_dictionary = []
    total_records_dictionary = []
    poa_dictionary = []
    non_poa_dictionary = []
    status = []
    for police in names_police:
        time.sleep(20)
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
                                   "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) "
                                   "Gecko/20100101 Firefox/82.0")
            profile.set_preference("dom.webdriver.enabled", False)
            profile.set_preference('useAutomationExtension', False)
            profile.set_preference("pdfjs.disabled", True)
            profile.update_preferences()
            driver = webdriver.Firefox(firefox_profile=profile)
            open_page()
            # call function for entering date, set the date through command line
            enter_date(date1=argv[1], date2=argv[2])

            # call function district, for now its Dhule. will change latter to command line
            district_selection(name)

            select_police_station(police)
        except (NoSuchElementException,
            WebDriverException,
            TimeoutException, ConnectionRefusedError,
            MaxRetryError, ConnectionError, NewConnectionError):
            print(f' bug {name}, {police}')
            with open(os.path.join(
                    download_directory,
                    "bug", f'{police}_report_0.txt'), 'a') as file:
                file.write(f'{name}, {police} \n')
            police_dictionary.append(police)
            total_records_dictionary.append("bug")
            poa_dictionary.append("bug")
            non_poa_dictionary.append("bug")
            status.append("bug")
            driver.quit()
            time.sleep(70)
            continue
        # call the value of records to view @ 50
        view_record()
        # call search
        search()
        record = number_of_records()
        if record == '':
            print(f'page not loaded for \n'
                  f'{police} @ {name} \n\n\n')
            with open(
                    os.path.join(
                        download_directory, "bug" f'bug_report_0.txt'
                    ), 'a') as file:
                file.write(f'{name}, "-" \n')
            driver.quit()
            poa_cases, non_poa_cases = check_the_act()
            police_dictionary.append("REPEAT")
            total_records_dictionary.append("REPEAT")
            poa_dictionary.append("REPEAT")
            non_poa_dictionary.append("REPEAT")
            status.append("REPEAT")
            time.sleep(80)
            break
        print(f'{name} {police} {record}')
        if int(record) > 0:
            with open(os.path.join(
                    base_directory,
                    "police_station_table",
                    f'{police}_full page.txt'), 'w') as file:
                file.write(f'{driver.page_source} \n')
                file.close()
        else:
            police_dictionary.append(police)
            total_records_dictionary.append(record)
            poa_dictionary.append("Not Applicable")
            non_poa_dictionary.append("Not Applicable")
            status.append("Not Applicable")
            driver.quit()
            continue
        poa_cases, non_poa_cases = check_the_act()
        if not poa_cases:
            print('no poa')
            driver.quit()
            police_dictionary.append(police)
            total_records_dictionary.append(record)
            poa_dictionary.append(0)
            non_poa_dictionary.append(len(non_poa_cases))
            status.append("Not Applicable")
            continue
        else:
            print(f'download in {police} @ {name}')

            try:
                download_repeat(poa_cases)
                police_dictionary.append(police)
                total_records_dictionary.append(record)
                poa_dictionary.append(len(poa_cases))
                non_poa_dictionary.append(len(non_poa_cases))
                status.append("Done")
            except (WebDriverException, TimeoutException,
                    NoSuchElementException):
                print("download failed")
                police_dictionary.append(police)
                total_records_dictionary.append(record)
                poa_dictionary.append(len(poa_cases))
                non_poa_dictionary.append(len(non_poa_cases))
                status.append("failed")
                driver.quit()
                time.sleep(30)
                continue
            except ElementNotInteractableException:
                print("Element not interactable")
                police_dictionary.append(police)
                total_records_dictionary.append(record)
                poa_dictionary.append(len(poa_cases))
                non_poa_dictionary.append(len(non_poa_cases))
                status.append("failed")
                driver.quit()
                time.sleep(30)
                continue
    district_dictionary = {"Unite": name,
                           "Police_Station": police_dictionary,
                           "Number of Records": total_records_dictionary,
                           "PoA Cases": poa_dictionary,
                           "Other Cases": non_poa_dictionary,
                           "Downloaded": status}
    df = pd.DataFrame(
        {key: pd.Series(value) for key, value in district_dictionary.items()})
    df.to_csv(
        os.path.join(base_directory, "summary", f'{name} _{argv[1]} to {argv[2]}.csv'))
    driver.quit()
