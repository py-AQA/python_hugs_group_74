from selenium.webdriver.common.by import By
import time
from locators import USERNAME_FIELD, LOGIN_BUTTON, PASSWORD_FIELD, LOGIN_BUTTON_CLASS
from data import LOGIN, LOGIN_ARRAY, LOGIN_ARRAY_NEGATIVE, PASSWORD, PASSWORD_NEGATIVE, MAIN_PAGE


def test_availability_form_username(driver):
    # is there user_name
    driver.get(MAIN_PAGE)
    try:
        user_field = driver.find_element(By.XPATH, USERNAME_FIELD)
    except:
        results = False

    if user_field:
        results = True

    assert results == True , 'The form don\'t have username_field'


def test_availability_form_username_placeholder(driver):
    # is there necessary  placeholder
    driver.get(MAIN_PAGE)
    # user_field = driver.find_element(By.XPATH, USERNAME_FIELD)
    placeholder = driver.find_element(By.XPATH, USERNAME_FIELD).get_attribute('placeholder')

    assert placeholder == "Username", 'The field don\'t have necessary  placeholder'



def test_availability_form_password(driver):
    # is there field_password
    driver.get(MAIN_PAGE)
    user_field = driver.find_element(By.XPATH, PASSWORD_FIELD)
    if user_field:
        results = True

    assert results == True , 'The form don\'t have password_field'
    driver.quit()

def test_availability_form_password_placeholder(driver):
    # is there necessary  placeholder
    driver.get(MAIN_PAGE)
    placeholder = driver.find_element(By.XPATH, PASSWORD_FIELD).get_attribute('placeholder')

    assert placeholder == "Password", 'The field don\'t have necessary  placeholder'

def test_availability_form_button_login(driver):
    # is there button_login
    driver.get(MAIN_PAGE)
    try:
        user_field = driver.find_element(By.CLASS_NAME, LOGIN_BUTTON_CLASS)
    except:
        user_field = False

    if user_field:
        results = True

    assert results == True , 'The form don\'t have field button LOGIN'

# <input type="submit" class="submit-button btn_action" data-test="login-button" id="login-button" name="login-button" value="Login">
# driver.quit()

