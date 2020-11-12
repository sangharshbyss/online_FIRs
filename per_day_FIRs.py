from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from sys import argv


# constants
main_url = r'https://citizen.mahapolice.gov.in/Citizen/MH/PublishedFIRs.aspx'
# trying with firefox
profile = webdriver.FirefoxProfile()
# set profile for saving directly without pop-up ref -
# https://stackoverflow.com/a/29777967


profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", '/home/sangharsh/Downloads')
# to go undetected
profile.set_preference("general.useragent.override",
                       "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) "
                       "Gecko/20100101 Firefox/82.0")
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile=profile)
# open the page
driver.get(main_url)

# functions
# 1 select district and enter
def district_selection(name):
    dist_list = Select(driver.find_element_by_css_selector(
        "#ContentPlaceHolder1_ddlDistrict"))

    # command line input
    dist_list.select_by_visible_text(name)
    time.sleep(6)


""" 
2. function for date to-from. same as in only details of one data will be collected.
this function needs ActionChains otherwise the dates are not getting entered. 
date will be entered through command line
"""


def enter_date(date):
    WebDriverWait(driver, 160).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        '#ContentPlaceHolder1_txtDateOfRegistrationFrom')))
    from_date_field = driver.find_element_by_css_selector(
        '#ContentPlaceHolder1_txtDateOfRegistrationFrom')

    to_date_field = driver.find_element_by_css_selector(
        '#ContentPlaceHolder1_txtDateOfRegistrationTo')

    ActionChains(driver).click(from_date_field).send_keys(
        date).move_to_element(to_date_field).click().send_keys(
        date).perform()


# 3. view 50 records at a time
def view_record():
    view = Select(driver.find_element_by_id('ContentPlaceHolder1_ucRecordView_ddlPageSize'))
    view.select_by_value("50")


# 4. function for click on search
def search():
    driver.find_element_by_css_selector('#ContentPlaceHolder1_btnSearch').click()


# 5 check if it has PoA if yes, download
def check_the_act():
    # check for PoA in table.
    #identify table first
    table = driver.find_element(By.ID, "ContentPlaceHolder1_gdvDeadBody")
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        for cell in cells:
            cell_text = cell.text
            if "अनुसूचीत जाती आणि अनुसूचीत" in cell_text:
                print(cell_text)
                
                row.find_element(By.TAG_NAME, "input").click()
                print("in here, can you now download")
                time.sleep(3)
                driver.close()
            else:
                print("no")

# 6. main code
driver.get(main_url)
# call function for entering date, set the date through command line
enter_date(date=argv[1])
# call function district, for now its Dhule. will change latter to command line
district_selection(name="DHULE")
# call the value of records to view @ 50
view_record()
# call search
search()
# wait for 5 sec
time.sleep(5)
# call function check the act and click download
check_the_act()

