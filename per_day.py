"""
iteration over pages fails. shiting to new file"""

import os
import time
from contextlib import contextmanager
import state_FIRs
import pandas as pd
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from FIR_logging import logger

# constants
URL = r'https://www.mhpolice.maharashtra.gov.in/Citizen/MH/PublishedFIRs.aspx'

# base dir path for downloading files:
Download_Directory = r'/home/sangharshmanuski/Documents/mha_FIRs/raw_footage'
# lists and files
# 1. empty list to store name of police stations where records were not found
record_not_found = []
# 2. empty list to store name of police stations where records were found
record_found = []
# 3. to get data of entire state
state_dataframes = []
# 3. empty file in append mode to write the summary.
summary_file = open(os.path.join(Download_Directory, 'records_summary.txt'), 'a')
# columns for the data frame
COLUMNS = ['Sr.No.', 'State', 'District', 'Police Station', 'Year', 'FIR No.', 'Registration Date', 'FIR No',
           'Sections']


# functions:
def enter_date(driver, three_months_back, yesterday):
    WebDriverWait(driver, 160).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                     '#ContentPlaceHolder1_txtDateOfRegistrationFrom')))
    datefield = driver.find_element_by_css_selector('#ContentPlaceHolder1_txtDateOfRegistrationFrom')

    end_datefield = driver.find_element_by_css_selector('#ContentPlaceHolder1_txtDateOfRegistrationTo')

    ActionChains(driver).click(datefield).send_keys(
        three_months_back).move_to_element(end_datefield).click().send_keys(yesterday).perform()

    logger.info('date entered')


def toggle_and_extract(district, district_dataframe):
    time.sleep(6)

    wait_for_page_load(driver, 50)
    number_of_records_found = driver.find_element_by_css_selector(
        '#ContentPlaceHolder1_lbltotalrecord').text
    if number_of_records_found != 0:
        logger.info(f'{district}: {number_of_records_found}')
        record_found.append(f'{district}: {number_of_records_found}')
    else:
        logger.info(f'no records @ {district}')
        record_not_found.append(district)
        return False
    # extract the record at current page.

    get_data(driver, district_dataframe)
    # go to other pages, if avalilable
    try:
        link_for_page = driver.find_element_by_css_selector('.gridPager a')

    except NoSuchElementException:
        logger.info("single page to record")
        district_data = pd.DataFrame(district_dataframe)
        district_data.to_csv(os.path.join(Download_Directory, f'{district}_24_06_to_25_06.csv'))

        return
    # iterate on each page but with new 'list' to avoid stale element exception
    links_for_page = driver.find_elements_by_css_selector('.gridPager a')
    for page in range(len(links_for_page)):
        # currently this wait is not helping in any way so has to add implicit wait.
        time.sleep(7)
        wait_for_page_load(driver, 50)
        # new list
        links_for_page_new = driver.find_elements_by_css_selector('.gridPager a')
        # do not click on link for new page
        if links_for_page_new[page].text != '...':
            links_for_page_new[page].click()
            logger.info(f'page {links_for_page_new.index(links_for_page_new[page])}')
            wait_for_page_load(driver, 50)
            get_data(driver, district_dataframe)

    district_data = pd.concat(district_dataframe)
    district_data.to_csv(os.path.join(Download_Directory, f'{district}_24_06_to_25_06.csv'))


def get_data(driver, frame_list):
    page_data = []
    time.sleep(10)
    soup = BS(driver.page_source, 'html.parser')
    main_table = soup.find("table", {"id": "ContentPlaceHolder1_gdvDeadBody"})
    # identify rows with links to pages
    skip_rows = main_table.find_all('tr', {"class": "gridPager"})
    # skip those rows and itarate over rest.
    rows = main_table.find_all("tr")
    if type(skip_rows) is None:

        for row in rows:
            cells = row.find_all('td')
            cells = cells[0:9]  # drop the last column

            # store data in list
            page_data.append([cell.text for cell in cells])
        frame_list.append(pd.DataFrame(page_data, columns=COLUMNS).drop(0, axis=0))


    else:
        for row in rows[0:(len(rows))]:
            page_data = []
            cells = row.find_all('td')
            cells = cells[0:9]  # drop the last column

            # store data in list
            page_data.append([cell.text for cell in cells])

        frame_list.append(pd.DataFrame(page_data, columns=COLUMNS).drop(0, axis=0))


@contextmanager
def wait_for_page_load(driver, timeout=10):
    """Wait till the old page is stale and old references are not working."""
    logger.debug("Waiting for page to load at {}.".format(driver.current_url))
    old_page = driver.find_element_by_id('lnkDisclaimers')
    yield
    WebDriverWait(driver, timeout).until(staleness_of(old_page))


# main code

# Start with a variable created as integer for looping
counter = 38

while counter < 49:
    try:
        district_dataframe = []
        options = FirefoxOptions()
        # options.add_argument("--headless")
        options.add_argument("--private-window")
        driver = webdriver.Firefox(options=options)
        driver.get(URL)
        driver.refresh()
        time.sleep(3)
        view = Select(driver.find_element_by_css_selector(
            '#ContentPlaceHolder1_ucRecordView_ddlPageSize'))
        view.select_by_value('50')
        enter_date(driver=driver, three_months_back='24062020', yesterday='25062020')
        unit_list = Select(driver.find_element_by_css_selector("#ContentPlaceHolder1_ddlDistrict"))
        unit_names = [o.get_attribute("text")
                      for o in unit_list.options]
        unit_values = [o.get_attribute("text")
                       for o in unit_list.options if o.get_attribute("value") != 'Select']
        unit_list.select_by_index(counter)
        # check - old page is stale and new page is loaded.
        try:
            wait_for_page_load(driver=driver, timeout=60)
        except TimeoutException:
            logger.debug(f'the page is not stale yet @ {unit_names[counter]}')
            logger.info(f'the page was not loaded @ {unit_names[counter]}')
            continue
        # click the search button
        driver.find_element_by_css_selector('#ContentPlaceHolder1_btnSearch').click()
        # check - old page is stale and new page is loaded.
        try:
            wait_for_page_load(driver=driver, timeout=60)
        except TimeoutException:
            logger.debug("wait with wait_for_page_load function.")
            logger.info('page was not loaded. trying again')
            continue
        try:
            toggle_and_extract(unit_names[counter], district_dataframe)
        except:
            raise
        counter += 1
        driver.close()
        logger.info(f'record found in: {record_found}, \nRecord not found in: {record_not_found}')
    except (NoSuchElementException, TimeoutException):
        logger.debug(f"some error retrying with same district")
        continue

# append summary file with short summary.
summary_file.write(f'Time Period: 24/06/2020 to 25/06/2020'
                   f'\n FIRs filed in Maharashtra. (Based on published FIRs by Maharashtra Police'
                   f'\n {record_not_found} \n\n\nRecords were found in '
                   f'\n totoal number of districts/unit where record was not found: {len(record_not_found)}'
                   f'\n {record_found} \n\n No records were found in following districts '
                   f'\n total number of districts/unit where record was not found: {len(record_not_found)}')

state_FIRs.state_file()
