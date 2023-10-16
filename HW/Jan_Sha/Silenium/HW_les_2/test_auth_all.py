from selenium.webdriver.common.by import By
import time
from locators import USERNAME_FIELD, LOGIN_BUTTON, PASSWORD_FIELD, LOGIN_BUTTON_CLASS, BURGER_MENU, LOGOUT_BUTTON
from data import LOGIN, LOGIN_ARRAY, LOGIN_ARRAY_NEGATIVE, PASSWORD, PASSWORD_NEGATIVE, MAIN_PAGE, ITEMS_PAGE


def test_auth_all_user_positive(driver):
    driver.get(MAIN_PAGE)
    # user_name = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
    # user_pass = 'secret_sauce'
    user_name_res = []

    for user_name_current in LOGIN_ARRAY:
        userfield = driver.find_element(By.XPATH, USERNAME_FIELD)
        userfield.send_keys(user_name_current)

        userfield_pass = driver.find_element(By.XPATH, PASSWORD_FIELD)
        userfield_pass.send_keys(PASSWORD)

        login_button = driver.find_element(By.XPATH, LOGIN_BUTTON)
        login_button.click()

        if driver.current_url == ITEMS_PAGE and user_name_current != 'locked_out_user':
            user_name_res.append(True)

            # click on burger_menu
            driver.find_element(By.XPATH, BURGER_MENU).click()

            time.sleep(2)

            driver.find_element(By.XPATH, LOGOUT_BUTTON).click()
        else:
            if driver.current_url == MAIN_PAGE:
                user_name_res.append(True)

            userfield.clear()
            userfield_pass.clear()

        time.sleep(1)

    # a = any(user_name_res)
    time.sleep(1)
    assert any(user_name_res) == True, f'We aren\'t login {LOGIN_ARRAY}'

    print('\n\n All users are testing for entrance and exit')


def test_auth_user_negotive(driver):
    driver.get(MAIN_PAGE)
    # user_name = ['standards_user', 'lokked_out_user', 'problem_users', 'performnce_glitch_user']
    # user_pass = ['secret_sauce', 'secret_sourse', 'secret-sourse', '123456', 'admin', 'qwerty', 'asdrty56-8_2']
    login_res = {}
    pass_res = []
    marker_bad = 0
    for user_name_res in LOGIN_ARRAY_NEGATIVE:
        for user_pass_res in PASSWORD_NEGATIVE:
            user_fuild = driver.find_element(By.XPATH, USERNAME_FIELD)
            user_fuild.send_keys(user_name_res)

            pass_fuild = driver.find_element(By.XPATH, PASSWORD_FIELD)
            pass_fuild.send_keys(user_pass_res)

            driver.find_element(By.XPATH, LOGIN_BUTTON).click()

            if driver.current_url != MAIN_PAGE:
                pass_res.append(user_pass_res)
                marker_bad = 1

            user_fuild.clear()
            pass_fuild.clear()

        time.sleep(1)

        if marker_bad == 1:
            login_res[user_name_res] = pass_res
            marker_bad = 0

    assert login_res == {}, [f'Finded user {i} login with password {j}' for i, j in login_res.items()]

    print('\n\n All users in data are testing for entrance')