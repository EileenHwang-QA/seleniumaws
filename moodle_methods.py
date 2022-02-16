import datetime
import pytest
import sys
import moodle_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(options=options)

#driver = webdriver.Chrome('C:/Users/eilee/PycharmProjects/python_cctb/chromedriver.exe')

# Fixture method - to open web browser
def setUp():
    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser respond in general
    driver.implicitly_wait(10)

    # navigating to Moodle app website
    driver.get(locators.moodle_url)

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.moodle_url and driver.title == 'Software Quality Assurance Testing':
        print(f' we are at Moodle homepage --{driver.current_url}')
        print(f'we\'re seeing title message -- {driver.title}')
        # sleep(5)
        # driver.close()

    else:
        print(f'we\'re not at the Moodle homepage, Check your code!')
        driver.close()
        driver.quit()

def tearDown():
    if driver is not None:
        print(f'------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()
        sleep(1)
        # Make a log file with dynamic fake values
        # old_instance = sys.stdout
        # log_file = open('message.log', 'w')
        # sys.stdout = log_file
        # print(f'Email: {locators.email}\nUsername: {locators.new_username}\nPassword: {locators.new_password}\n'
        #       f'Full Name: {locators.full_name}')
        # sys.stdout = old_instance
        # log_file.close()



def log_in(username, password):
    if driver.current_url == locators.moodle_url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == locators.moodle_login_url:
            driver.find_element(By.ID, "username").send_keys(username)
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(password)
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()
            if driver.title == 'Dashboard' and driver.current_url == locators.moodle_dashboard_url:
                assert driver.current_url == locators.moodle_dashboard_url
                print(f'Log in successfully.Dash board is present.\n'
                      f'We logged in with Username"{username}" and Password"{password}"')

            else:
                print(f'We\'re not at the Dashboard.Try again!')

def log_out():
     driver.find_element(By.CLASS_NAME, 'userpicture').click()
     sleep(0.25)
     driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
     sleep(0.25)
     if driver.current_url == locators.moodle_url:
         print(f'Log out successfully at: {datetime.datetime.now()}')


def create_new_user():

    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    sleep(0.25)

    # Enter fake data into username open fields
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    driver.find_element(By.ID,'id_newpassword').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    print(locators.email)

    # select 'Allow everyone tp see my email address'
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID,'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(0.25)
    driver.find_element(By.ID,"id_city").send_keys(locators.city)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text('Canada')
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_visible_text('America/Vancouver')
    sleep(0.25)
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    sleep(0.25)
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    sleep(0.25)

    # upload picture to the User picture section
    # click by "You can drag and drop files here to add them" section
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    sleep(0.25)

    # driver.find_element(By.XPATH,'//span[contain(.,',"Server files").click()
    driver.find_element(By.PARTIAL_LINK_TEXT,'Server files').click()
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT,'Cosmetics').click()
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT,'Biotherm 2021 fall school').click()
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT,'Course image').click()
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT,'BT2021fall.png').click()
    sleep(0.25)

    # Click by 'Select this file' button
    driver.find_element(By.XPATH,'//button[contains(.,"Select this file")]').click()
    sleep(0.25)

    # Enter picture
    driver.find_element(By.NAME,'imagealt').send_keys(locators.pic_desc)
    sleep(0.25)

    # Click by 'additional names' dropdown name
    driver.find_element(By.XPATH, '//a[contains(.,"Additional names")]').click()
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.phonetic_name)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.phonetic_name)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.phonetic_name)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.phonetic_name)
    sleep(0.25)

    # click by 'Interests' dropdown menu
    driver.find_element(By.XPATH, '//a[contains(., "Interests")]').click()
    sleep(0.25)

    # Using for loop, take all items from the list and populate data
    for tag in locators.list_of_interests:
        driver.find_element(By.XPATH, '//div[3]/input').click()
        sleep(0.25)
        driver.find_element(By.XPATH, '//div[3]/input').send_keys(tag)
        sleep(0.25)
        driver.find_element(By.XPATH, '//div[3]/input').send_keys(Keys.ENTER)
    sleep(0.25)

    # Fill optional section
    #Click by Optional link to open that section
    driver.find_element(By.XPATH,"//a[text() = 'Optional']").click()

    # Fill out web_page_url input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_url").send_keys(locators.web_page_url)
    sleep(0.25)

    # Fill out icq_number input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_icq").send_keys(locators.icq_number)
    sleep(0.25)

    # Fill out skype_id input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_skype").send_keys(locators.new_username)
    sleep(0.25)

    # Fill out d_aim input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_aim").send_keys(locators.new_username)
    sleep(0.25)

    # Fill out id_yahoo input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_yahoo").send_keys(locators.new_username)
    sleep(0.25)

    # Fill out id_msn input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_msn").send_keys(locators.new_username)
    sleep(0.25)

    # Fill out id_number input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_idnumber").send_keys(locators.icq_number)
    sleep(0.25)

    # Fill out institution input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_institution").send_keys(locators.institution)
    sleep(0.25)

    # Fill out department input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_department").send_keys(locators.department)
    sleep(0.25)

    #  Fill out phone input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_phone1").send_keys(locators.phone)
    sleep(0.25)

    # Fill out phone2 input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_phone2").send_keys(locators.mobile_phone)
    sleep(0.25)

    # Fill out address input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_address").send_keys(locators.address)
    sleep(0.25)
    # Click by submit
    driver.find_element(By.CSS_SELECTOR, "input#id_submitbutton").click()
    sleep(0.25)
    print(f'Test scenario: Create a new user "{locators.new_username}" -------is passed')

def check_user_created():
    # check that we are on the user's Main page
    if driver.current_url == locators.moodle_main_page:
        assert driver.find_element(By.XPATH, "//h1[text() = 'Software Quality Assurance Testing']").is_displayed()
        # assert driver.find_element(By.XPATH, "//h1[text() = '769 Users']").is_displayed
        if driver.find_element(By.ID, "fgroup_id_email_grp_label") and \
            driver.find_element(By.CSS_SELECTOR, "input#id_email"):
            sleep(0.25)
            driver.find_element(By.CSS_SELECTOR, "input#id_email").send_keys(locators.email)
            sleep(0.25)
            driver.find_element(By.CSS_SELECTOR, "input#id_addfilter").click()
            sleep(0.25)
            if driver.find_element(By.XPATH, f'//td[contains(.,"{locators.email}")]'):
              print('Test scenario: Check user created -------is passed')


def check_we_logged_in_with_new_cred():
    if driver.current_url == locators.moodle_dashboard_url:
        if driver.find_element(By.XPATH, f'//span[contains(., "{locators.full_name}")]').is_displayed():
            print(f'--- User with the name {locators.full_name} is displayed. Test Passed ---')

def delete_new_user():
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Browse list of users').is_displayed()
    sleep(0.25)
    if driver.find_element(By.ID, "fgroup_id_email_grp_label") and \
            driver.find_element(By.CSS_SELECTOR, "input#id_email"):
        sleep(0.25)
        driver.find_element(By.CSS_SELECTOR, "input#id_email").send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.CSS_SELECTOR, "input#id_addfilter").click()
        sleep(0.25)
        if driver.find_element(By.XPATH, f'//td[contains(.,"{locators.email}")]'):
            driver.find_element(By.XPATH, '//i[@title="Delete"]').click()
            sleep(0.25)
            driver.find_element(By.XPATH,'//button[contains(.,"Delete")]').click()
            sleep(0.25)
            print(f'Test scenario: Deleted a new user -------is passed')


# def logger():
#     old_instance = sys.stdout
#     log_file = open('message.log', 'w')
#     sys.stdout = log_file
#     print(f'Email:{locators.email}\nUsername:{locators.new_username}\nPassword: {locators.new_password}')
#     sys.stdout = old_instance
#     log_file.close()

# ### Create a new user Test case ####
# # Open web browser
# setUp()
# # Log in
# log_in(locators.moodle_username,locators.moodle_password)
# # Create a new user
# create_new_user()
# # check user has been added
# check_user_created()
# # Close web browser
# # tearDown()
#
#
# ### Log in with New User Credential Test Case ###
# # Open web browser
# # setUp()
# # Log in
# log_in(locators.new_username, locators.new_password)
# # Check we logged in with the new credential
# check_we_logged_in_with_new_cred()
# log_out()
# log_in(locators.moodle_username,locators.moodle_password)
# delete_new_user()
# log_out()
# # Close web browser
# tearDown()

