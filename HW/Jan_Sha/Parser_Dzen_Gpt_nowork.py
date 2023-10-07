'''
С сайта dzen news (https://dzen.ru/news) необходимо собрать краткий текст и названия всех статей за последний
месяц (на момент выполнения) с ключевым словом "игра".
Затем для полученных статей необходимо рассчитать топ-50 наиболее частотных слов и представить их
в виде word (tag) cloud.
Данное задание необходимо выполнить с помощью python.

Для представления в виде word cloud можно использовать уже существующие библиотеки. Пример word cloud можно
посмотреть по ссылке - https://altoona.psu.edu/sites/altoona/files/success-word-cloud.jpg
'''

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# URL страницы Dzen News
url = 'https://dzen.ru/news'

# Определение текущей даты и даты, которая была месяц назад
today = datetime.now()
one_month_ago = today - timedelta(days=30)

# Форматирование даты в строку, чтобы добавить ее в URL как параметр
date_string = one_month_ago.strftime('%Y-%m-%d')

# Параметры запроса
params = {'date': date_string}

# Отправка GET-запроса к странице Dzen News с параметрами даты
response = requests.get(url, params=params)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсинг HTML страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Нахождение всех заголовков статей
    article_titles = soup.find_all('h2', class_='b-simple-news__title')

    # Нахождение всех кратких текстов статей
    article_summaries = soup.find_all('div', class_='b-simple-news__summary')

    # Вывод названий и кратких текстов статей
    for title, summary in zip(article_titles, article_summaries):
        print("Заголовок статьи:", title.text.strip())
        print("Краткий текст:", summary.text.strip())
        print("\n")
else:
    print("Ошибка при запросе страницы:", response.status_code)