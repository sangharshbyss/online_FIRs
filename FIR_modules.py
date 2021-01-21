import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

""" 
2. function for date to-from. 
date will be entered through command line
"""


def enter_date(date1, date2, driver):
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
def district_selection(dist_name, driver):
    dist_list = Select(driver.find_element_by_css_selector(
        "#ContentPlaceHolder1_ddlDistrict"))

    dist_list.select_by_visible_text(dist_name)


# 4. List police station
def police_stations(driver):
    WebDriverWait(driver, 160).until(
        ec.presence_of_element_located((By.CSS_SELECTOR,
                                        '#ContentPlaceHolder1_ddlPoliceStation')))
    select_box = driver.find_element_by_css_selector("#ContentPlaceHolder1_ddlPoliceStation")
    all_police_stations = [
        x.text for x in select_box.find_elements_by_tag_name("option") if x.text != "Select"]
    return all_police_stations


# select police station
def select_police_station(selected_police, driver):
    # this will select police station as per there names listed in
    # list created by police_stations() function.
    police_list = Select(driver.find_element_by_css_selector(
        '#ContentPlaceHolder1_ddlPoliceStation'))
    police_list.select_by_visible_text(selected_police)


# 5. view 50 records at a time
def view_record(driver):
    view = Select(driver.find_element_by_id('ContentPlaceHolder1_ucRecordView_ddlPageSize'))
    view.select_by_value("50")


# 4. function for click on search
def search(driver):
    driver.find_element_by_css_selector('#ContentPlaceHolder1_btnSearch').click()
    time.sleep(4)


def number_of_records(driver):
    total_number = driver.find_element_by_css_selector(
        '#ContentPlaceHolder1_lbltotalrecord').text
    return total_number


# 5 check if it has PoA if yes, create a list of how many cases
def check_the_act(driver, poa_dir_district,
                  poa_dir_police,
                  poa_dir_year,
                  poa_dir_FIR,
                  poa_dir_date,
                  poa_dir_sec):
    poa_list = []

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
                poa_dir_district.append(cells[2].text)
                poa_dir_police.append(cells[3].text)
                poa_dir_year.append(cells[4].text)
                poa_dir_FIR.append(cells[5].text)
                poa_dir_date.append(cells[6].text)
                poa_dir_sec.append(cells[8].text)

    return poa_list


def download_repeat(some_list, driver,
                    ):
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
            "#ReportViewer1_ctl06_ctl04_ctl00_Menu > div:nth-child(4) "
            "> a:nth-child(1)"
        )
        time.sleep(2)
        down_load.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.close()
        print('finished')
        driver.switch_to.window(main_window)
        i += 1


def second_page(driver):
    p2 = driver.find_element_by_xpath(
        '/html/body/form/div[4]/table/tbody/tr[4]/td/div[2]/div/table/'
        'tbody/tr/td/table[2]/tbody/tr/td/div[3]/div[1]/table/tbody/tr[52]'
        '/td/table/tbody/tr/td[2]/a')
    p2.click()


def third_page(driver):
    p3 = driver.find_element_by_xpath(
        "/html/body/form/div[4]/table/tbody/tr[4]/td/div[2]/div/"
        "table/tbody/tr/td/table[2]/tbody/tr/td/div[3]/div[1]/table"
        "/tbody/tr[52]/td/table/tbody/tr/td[3]/a"
    )
    p3.click()
