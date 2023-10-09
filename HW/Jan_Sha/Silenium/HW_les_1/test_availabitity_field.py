from selenium import webdriver
from selenium.webdriver.common.by import By
# import time


def test_availability_form_username():
    # global results

    # is there user_name
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    try:
        user_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    except:
        results = False

    if user_field:
        results = True

    assert results == True , 'The form don\'t have username_field'
    driver.quit()

def test_availability_form_username_placeholder():
    # is there necessary  placeholder
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    user_field = driver.find_element(By.NAME, 'user-name')
    placeholder = user_field.get_attribute('placeholder')

    assert placeholder == "Username", 'The field don\'t have necessary  placeholder'
    driver.quit()


def test_availability_form_password():
    # is there field_password
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    user_field = driver.find_element(By.ID, 'password')
    if user_field:
        results = True

    assert results == True , 'The form don\'t have password_field'
    driver.quit()

def test_availability_form_password_placeholder():
    # is there necessary  placeholder
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    user_field = driver.find_element(By.XPATH, '//input[@type="password"]')
    placeholder = user_field.get_attribute('placeholder')

    assert placeholder == "Password", 'The field don\'t have necessary  placeholder'
    driver.quit()

def test_availability_form_button_login():
    # is there button_login
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    try:
        user_field = driver.find_element(By.CLASS_NAME, 'submit-button')
    except:
        user_field = False

    if user_field:
        results = True

    assert results == True , 'The form don\'t have field button LOGIN'
    driver.quit()
# <input type="submit" class="submit-button btn_action" data-test="login-button" id="login-button" name="login-button" value="Login">
# driver.quit()

