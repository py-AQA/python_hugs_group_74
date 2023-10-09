from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_check_recycler():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(2)
    # button_field = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    # button_field.click()

    button_field = driver.find_elements(By.CSS_SELECTOR, 'button[class="btn btn_primary btn_small btn_inventory"]')
    for button_field_local in button_field:
        button_field_local.click()

    count_button_field = len (button_field)
    recycle_field = driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    recycle_field.click()

    recycle_items = driver.find_elements(By.CSS_SELECTOR, 'div[class="cart_item_label"]')
    count_recycle_items = len(recycle_items)

    assert count_button_field == count_recycle_items, 'Number product not equal number items in recycled'



    time.sleep(2)