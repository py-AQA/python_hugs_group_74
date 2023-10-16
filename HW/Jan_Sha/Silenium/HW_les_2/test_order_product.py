from selenium.webdriver.common.by import By
import time
import re
from locators import USERNAME_FIELD, LOGIN_BUTTON, PASSWORD_FIELD, LOGIN_BUTTON_CLASS, BURGER_MENU, \
    LOGOUT_BUTTON, BLOCK_CSS_SELECTOR, IMG_CSS_SELECTOR, BUTTON_ORDER_CSS_SELECTOR, BUTTON_ORDER_USE_CSS_SELECTOR,\
    COST_FUILD_CSS_SELECTOR, SHORT_ARTICLE_CSS_SELECTOR, BUTTON_ORDER_FULL_CSS_SELECTOR, RECYCLED_ITEMS, RECYCLED

from data import LOGIN, LOGIN_ARRAY, LOGIN_ARRAY_NEGATIVE, PASSWORD, PASSWORD_NEGATIVE, MAIN_PAGE, ITEMS_PAGE

def test_check_recycler(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    time.sleep(2)

    button_field = driver.find_elements(By.CSS_SELECTOR, BUTTON_ORDER_CSS_SELECTOR)
    for button_field_local in button_field:
        button_field_local.click()

    count_button_field = len(button_field)
    time.sleep(1)

    count_index_recycled_string = driver.find_element(By.CSS_SELECTOR, RECYCLED).text
    if count_index_recycled_string:
        count_index_recycled = int(count_index_recycled_string)
    else:
        count_index_recycled = 0

    assert count_button_field == count_index_recycled, 'Number product not equal number items in index recycled images'

    driver.find_element(By.CSS_SELECTOR, RECYCLED).click()

    recycle_items = driver.find_elements(By.CSS_SELECTOR, RECYCLED_ITEMS)
    count_recycle_items = len(recycle_items)

    assert count_button_field == count_recycle_items, 'Number product not equal number items in recycled'
