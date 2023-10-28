from os import environ

from selenium import webdriver


# Базовые настройки для запуска Chrome
def chrome_options() -> webdriver.ChromeOptions:
    options = webdriver.ChromeOptions()
    if environ.get('GITLAB_CI') or environ.get('GITHUB_ACTIONS') == 'true':
        # Если мы запускаем в CI: GitLab или GitHub
        options.add_argument('--headless')  # Не показывать окно браузера
        # Для ускорения тестов отключаем безопасность Chrome
        options.add_argument('--no-sandbox')
        # Для ускорения тестов отключаем ещё одну защиту Chrome
        options.add_argument('--disable-dev-shm-usage')
    return options
