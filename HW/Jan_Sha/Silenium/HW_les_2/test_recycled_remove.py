from selenium.webdriver.common.by import By
import time
import re
from locators import USERNAME_FIELD, LOGIN_BUTTON, PASSWORD_FIELD, LOGIN_BUTTON_CLASS, BURGER_MENU, \
    LOGOUT_BUTTON, BLOCK_CSS_SELECTOR, IMG_CSS_SELECTOR, BUTTON_ORDER_CSS_SELECTOR, BUTTON_ORDER_USE_CSS_SELECTOR,\
    COST_FUILD_CSS_SELECTOR, SHORT_ARTICLE_CSS_SELECTOR, BUTTON_ORDER_FULL_CSS_SELECTOR, RECYCLED_ITEMS, RECYCLED

from data import LOGIN, LOGIN_ARRAY, LOGIN_ARRAY_NEGATIVE, PASSWORD, PASSWORD_NEGATIVE, MAIN_PAGE, ITEMS_PAGE

def test_recycled_remove(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    time.sleep(1)

    b = [0, 2, -1]

    button_field = driver.find_elements(By.CSS_SELECTOR, BUTTON_ORDER_CSS_SELECTOR)
    for i in b:

    for button_field_local in button_field[]:
        button_field_local.click()