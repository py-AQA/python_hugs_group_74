from selenium.webdriver.common.by import By


class MainPageLocators:
    SIGN_IN_LINK = (By.CSS_SELECTOR, 'div.panel.header .authorization-link')
    WELCOME = (By.CSS_SELECTOR, 'div.panel.header .logged-in')


class SignInPageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='login[username]']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='login[password]']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '.action.login.primary')