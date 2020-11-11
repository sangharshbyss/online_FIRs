from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, \
    TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from FIR_logging import logger
import os
import time
import pandas as pd

# base function


# Some constants:

URL = r'http://www.mhpolice.maharashtra.gov.in/Citizen/MH/PublishedFIRs.aspx'

Download_Directory = r'/home/sangharshmanuski/Documents/mha_FIRs/raw_footage/raw_footage_after_beed'

COLUMNS = ['Sr.No.', 'State', 'District', 'Police Station', 'Year', 'FIR No.', 'Registration Date', 'FIR No',
           'Sections']

ALL_Districts = ['NAGPUR RURAL']


# other functions


def district_selection(name):
    dist_list = Select(driver.find_element_by_css_selector(
        "#ContentPlaceHolder1_ddlDistrict"))

    names = [o.get_attribute("text")
             for o in dist_list.options if o.get_attribute("text") not in (
                 'Select')]
    if name not in names:
        logger.info(f"{name} is not in list")
        return False
    dist_list.select_by_visible_text(name)
    time.sleep(6)


def police_station(ps):
    # select particular police station
    police_station_list = Select(driver.find_element_by_css_selector(
        "#ContentPlaceHolder1_ddlPoliceStation"))

    name = ps
    police_station_list.select_by_visible_text(name)
    time.sleep(3)

def enter_date(date, date_plus_one):
    # enters start as well as end dates with "action chains."
    WebDriverWait(driver, 160).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        '#ContentPlaceHolder1_txtDateOfRegistrationFrom')))
    from_date_field = driver.find_element_by_css_selector(
        '#ContentPlaceHolder1_txtDateOfRegistrationFrom')

    to_date_field = driver.find_element_by_css_selector(
        '#ContentPlaceHolder1_txtDateOfRegistrationTo')

    ActionChains(driver).click(from_date_field).send_keys(
        date).move_to_element(to_date_field).click().send_keys(
        date_plus_one).perform()

    logger.info(f'date entered: {date}')


def search():
    driver.find_element_by_css_selector('#ContentPlaceHolder1_btnSearch').click()


def number_of_records():
    """captures the text indicating number of records.
    converts it to integer. if 0 returns and appends name of district to the list
    if page is not loaded. it tries one more time for 15 secs."""
    if driver.find_elements_by_css_selector("#ContentPlaceHolder1_gdvDeadBody_lblNoRowsFound").is_displayed:
        return False

    time_counter = 1
    while time_counter < 8:
        try:
            records_number = driver.find_element_by_css_selector(
                '#ContentPlaceHolder1_lbltotalrecord').text

            if records_number == '':
                time.sleep(1)
                continue
            else:
                records_number = int(records_number)
            if records_number != 0:
                logger.info(f"{district}: {records_number}")

                return records_number
            else:
                logger.info(f"no records @ {district}")
                return False
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
            logger.info("page is not loaded")
            time_counter += 1
            continue


def extract_table_current(name, single):
    # entire table of record to be taken to the list.
    soup = BS(driver.page_source, 'html.parser')
    main_table = soup.find("table", {"id": "ContentPlaceHolder1_gdvDeadBody"})
    time_counter = 1
    while main_table is None:
        if time_counter < 6:
            logger.info(f"the table did not load @ {name}")
            time.sleep(1)
            time_counter += 1
        else:
            logger.info(f"the table did not load @ {name}."
                        f"stopped trying")
            return
    links_for_pages = driver.find_elements_by_css_selector('.gridPager a')
    rows = main_table.find_all("tr")
    if links_for_pages is None:

        for row in rows:
            time.sleep(8)
            if '...' not in row.text:
                cells = row.find_all('td')
                cells = cells[0:9]  # drop the last column
                # store data in list
                single.append([cell.text for cell in cells])
    else:
        for row in rows[0:(len(rows)) - 2]:
            time.sleep(6)
            cells = row.find_all('td')
            cells = cells[0:9]  # drop the last column

            # store data in list
            single.append([cell.text for cell in cells])


def check_the_act(page):
    # check for PoA in table.
    soup = BS(page, 'html')
    rows = soup.find_all('//*[@id="ContentPlaceHolder1_gdvDeadBody"]//tr')
    for row in rows:
        cell = row.find_all("td")
        text = cell[0].text
        if "मुंबई दारूबंदी अधिनियम" in text:
            submit = driver.find_elements_by_tag_name("input")
            submit.click()


def next_page(name, data):
    # check if any link to next page is available
    # iterate every page.
    try:
        driver.find_element_by_css_selector('.gridPager a')
    except NoSuchElementException:
        return False
    links_for_pages = driver.find_elements_by_css_selector('.gridPager a')
    for page in range(len(links_for_pages)):
        # new list, to by pass stale element exception
        links_for_pages_new = driver.find_elements_by_css_selector('.gridPager a')
        # do not click on link for new page slot
        if links_for_pages_new[page].text != '...':
            links_for_pages_new[page].click()
            # if this can be replaced with some other wait method to save the time
            time.sleep(5)
            extract_table_current(name, data)


def second_page_slot():
    # find specific link for going to page 11 and click.
    try:
        link_for_page_slot = driver.find_element_by_link_text('...')
        link_for_page_slot.click()
    except NoSuchElementException:
        return False


# main code

page_data = []

for district in ALL_Districts:

    b = "07"
    c = "2020"
    district_directory = os.path.join(Download_Directory, f'{district}{b}{c}')
    if not os.path.exists(district_directory):
        os.mkdir(district_directory)
    for i in range(1, 30):

        options = FirefoxOptions()
        #options.add_argument("--headless")
        options.add_argument("--private-window")
        driver = webdriver.Firefox(options=options)
        driver.get(URL)
        driver.refresh()
        view = Select(driver.find_element_by_css_selector(
            '#ContentPlaceHolder1_ucRecordView_ddlPageSize'))
        view.select_by_value('50')
        # entering date and assuring that 01 to 09 is entered correctly
        if i < 10:
            i_i = i + 1
            i = f'{str("0")}{str(i)}'
            if i_i < 10:
                i_i = f'{str("0")}{str(i_i)}'
        else:
            i_i = i + 1
        date_from = str(i) + b + c
        date_to = str(i_i) + b + c
        enter_date(date_from, date_to)
        # select district
        district_selection(district)
        time.sleep(3)
        police_station("NARKHED")
        # start the search
        search()
        time.sleep(5)
        if not number_of_records():
            continue
        extract_table_current(district, page_data)

        if not next_page(district, page_data):
            district_data = pd.DataFrame(page_data, columns=COLUMNS)
            district_data.to_csv(os.path.join(district_directory, f'{district}{i}{b}{c}.csv'))
            continue
        extract_table_current(district, page_data)
        district_data = pd.DataFrame(page_data, columns=COLUMNS)
        district_data.to_csv(os.path.join(district_directory, f'{district}{i}{b}{c}.csv'))
        driver.close()
