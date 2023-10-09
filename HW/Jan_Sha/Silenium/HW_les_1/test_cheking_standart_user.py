from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re


def test_check_product_page():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(2)

    block = driver.find_elements(By.CSS_SELECTOR,'div[class="inventory_item"]')
    count_block = len(block)

    img_field = driver.find_elements(By.CSS_SELECTOR, 'img[class="inventory_item_img"]')
    count_img = len([re.findall('jpg$|png$|jpeg$',img_field_point.get_attribute('src')) for img_field_point in img_field])

    button_field = driver.find_elements(By.CSS_SELECTOR, 'button[class="btn btn_primary btn_small btn_inventory"]')
    count_button = len(button_field)

    cost_field = driver.find_elements(By.CSS_SELECTOR, 'div[class="inventory_item_price"]')
    count_cost = len(cost_field)

    short_article_field = driver.find_elements(By.CSS_SELECTOR, 'div[class="inventory_item_desc"]')
    count_short_article = len(short_article_field)

    assert count_block == count_img, 'Numbers of block not equal numbers of image'
    assert count_block == count_button, 'Numbers of block not equal numbers of button "Add to card"'
    assert count_block == count_cost, 'Numbers of block not equal numbers of cost products'
    assert count_block == count_short_article, 'Numbers of block not equal numbers of short articles by product'

    time.sleep(2)