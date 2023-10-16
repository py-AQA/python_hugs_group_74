from selenium.webdriver.common.by import By
import time
import re
from locators import USERNAME_FIELD, LOGIN_BUTTON, PASSWORD_FIELD, LOGIN_BUTTON_CLASS, BURGER_MENU, \
    LOGOUT_BUTTON, BLOCK_CSS_SELECTOR, IMG_CSS_SELECTOR, BUTTON_ORDER_CSS_SELECTOR, BUTTON_ORDER_USE_CSS_SELECTOR,\
    COST_FUILD_CSS_SELECTOR, SHORT_ARTICLE_CSS_SELECTOR

from data import LOGIN, LOGIN_ARRAY, LOGIN_ARRAY_NEGATIVE, PASSWORD, PASSWORD_NEGATIVE, MAIN_PAGE, ITEMS_PAGE


def test_check_product_page(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    time.sleep(2)

    block = driver.find_elements(By.CSS_SELECTOR, BLOCK_CSS_SELECTOR)
    count_block = len(block)

    img_field = driver.find_elements(By.CSS_SELECTOR, IMG_CSS_SELECTOR)
    count_img = len([re.findall('jpg$|png$|jpeg$', img_field_point.get_attribute('src')) for img_field_point in img_field])

    button_field = driver.find_elements(By.CSS_SELECTOR, BUTTON_ORDER_CSS_SELECTOR)
    count_button = len(button_field)

    cost_field = driver.find_elements(By.CSS_SELECTOR, COST_FUILD_CSS_SELECTOR)
    count_cost = len([cost.text for cost in cost_field if cost.text])

    short_article_field = driver.find_elements(By.CSS_SELECTOR, SHORT_ARTICLE_CSS_SELECTOR)
    count_short_article = len([short_article.text for short_article in short_article_field if short_article.text])

    assert count_block == count_img, 'Numbers of block not equal numbers of image'
    assert count_block == count_button, 'Numbers of block not equal numbers of button "Add to card"'
    assert count_block == count_cost, 'Numbers of block not equal numbers of cost products'
    assert count_block == count_short_article, 'Numbers of block not equal numbers of short articles by product'

    time.sleep(2)