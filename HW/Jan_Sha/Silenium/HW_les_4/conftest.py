import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def options():
    options = Options()
    options.add_argument('--window-size=1980,1080')
    return options

@pytest.fixture
def driver(options):
    driver = webdriver.Chrome(options= options)
    yield driver
    driver.quit()
