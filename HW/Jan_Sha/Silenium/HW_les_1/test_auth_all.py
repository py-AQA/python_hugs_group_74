from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Accepted usernames are:
#     standard_user
#     locked_out_user
#     problem_user
#     performance_glitch_user
#
# pass: secret_sauce
def test_auth_all_user_positive():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    user_name = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
    user_pass = 'secret_sauce'
    user_name_res = []

    for user_name_current in user_name:
        userfield = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        userfield.send_keys(user_name_current)

        userfield_pass = driver.find_element(By.XPATH, '//*[@id="password"]')
        userfield_pass.send_keys(user_pass)

        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()

        if driver.current_url == "https://www.saucedemo.com/inventory.html" and user_name_current != 'locked_out_user':
            user_name_res.append(True)
            button_menu = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
            button_menu.click()

            time.sleep(1)

            button_out = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
            button_out.click()
        else:
            if driver.current_url == 'https://www.saucedemo.com':
                user_name_res.append(True)

            userfield.clear()
            userfield_pass.clear()

        time.sleep(1)

    a = any(user_name_res)
    time.sleep(5)
    assert any(user_name_res) == True, f'We aren\'t login {user_name}'

    driver.quit()


def test_auth_user_negotive():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com')
    user_name = ['standards_user', 'lokked_out_user', 'problem_users', 'performnce_glitch_user']
    user_pass = ['secret_sauce', 'secret_sourse', 'secret-sourse', '123456', 'admin', 'qwerty', 'asdrty56-8_2']
    login_res = {}
    pass_res = []
    marker_bad = 0
    for user_name_res in user_name:
        for user_pass_res in user_pass:
            user_fuild = driver.find_element(By.XPATH, '//*[@id="user-name"]')
            user_fuild.send_keys(user_name_res)

            pass_fuild = driver.find_element(By.XPATH, '//*[@id="password"]')
            pass_fuild.send_keys(user_pass_res)

            log_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
            log_button.click()

            if driver.current_url != 'https://www.saucedemo.com/':
                pass_res.append(user_pass_res)
                marker_bad = 1

            user_fuild.clear()
            pass_fuild.clear()

        if marker_bad == 1:
            login_res[user_name_res] = pass_res
            marker_bad = 0

    driver.quit()

    assert login_res == {}, [f'Finded user {i} login with password {j}' for i, j in login_res.items()]
