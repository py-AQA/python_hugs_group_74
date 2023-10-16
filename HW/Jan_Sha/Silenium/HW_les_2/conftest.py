import pytest
from selenium import webdriver
from data import LOGIN, LOGIN_ARRAY, PASSWORD, MAIN_PAGE, ITEMS_PAGE

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    print('\nquit browser...')
    driver.quit()

