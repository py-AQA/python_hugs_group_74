'''
парсин хабр новостей

С сайта dzen news (https://dzen.ru/news) необходимо собрать краткий текст и названия всех статей за последний
месяц (на момент выполнения) с ключевым словом "игра".
Затем для полученных статей необходимо рассчитать топ-50 наиболее частотных слов и представить их
в виде word (tag) cloud.
Данное задание необходимо выполнить с помощью python.

Для представления в виде word cloud можно использовать уже существующие библиотеки. Пример word cloud можно
посмотреть по ссылке - https://altoona.psu.edu/sites/altoona/files/success-word-cloud.jpg
'''

from bs4 import BeautifulSoup
import random
import json
import requests
import datetime
from fake_useragent import UserAgent

# Создаем переменную с модулем fake_useragent, чтобы мы могли потом использовать для генерации user-agent:
ua = UserAgent()

# Определяем заголовки (для того чтобы сервер сайта мог понять, как он должен отправить ответ,
# а также помогает серверу определить отправителя запроса)
headers = {
    'accept': 'application/json, text/plain, */*',
    'user-Agent': ua.google,
}

#словарь, где будут храниться название и ссылка на каждую статью:
article_dict = {}

# Создаем цикл для сбора со всех страниц, а не с одной (с 1 по 3, т.к. страниц с ссылками в день, как я понимаю всего 3).
# Указываем url c форматирование кода, где i - номер страницы, которое вставляться при каждом проходе цикла.
for i in range(1, 4):
    url = f'https://habr.com/ru/top/daily/page{i}/'

    # Отправляем get запрос на сайт, указывая в первом аргументе - переменную с url сайта, во-втором заголовки.
    # Атрибут text, нужен чтобы получить текстовое содержанием html страницы
    req = requests.get(url, headers=headers).text
    # soup = BeautifulSoup(req, 'html.parser') # с помощью BeautifulSoup соберем весь html код страницы.
    # print(soup)
    soup = BeautifulSoup(req, 'lxml') # с помощью BeautifulSoup соберем весь html код страницы.

    # all_hrefs_articles = soup.find_all('a', class_='tm-title__link')
    # for article in all_hrefs_articles:
    #     article_name = article.find('span').text  # собираем названия статей
    #     article_link = f'https://habr.com{article.get("href")}' # их ссылки
    #     article_dict[article_name] = [article_link, ] #собираем в словарь
    #
    # all_small_text_articles = soup.find_all('div', class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
    # for article_small_text in all_small_text_articles:
    #     article_small_text_full = article_small_text.find('p').text
    #     # print(article_small_text_full)

    all_block_articles = soup.find_all('div', class_='tm-article-snippet tm-article-snippet')
    for block_article in all_block_articles:
        c_block_articles = soup.find_all('a', class_='tm-title__link')
        for article in c_block_articles:
            article_name = article.find('span').text  # собираем названия статей
            article_link = f'https://habr.com{article.get("href")}'  # их ссылки
            article_dict[article_name] = [article_link, ]  # собираем в словарь

        article_name = article.find('span').text
        article_link = f'https://habr.com{article.get("href")}'  # их ссылки

    # nextFileName = './docs/pagination/{}.json'.format(len(os.listdir('./docs/pagination')))
with open(f"./docs/articles_{datetime.datetime.now().strftime('%d_%m_%Y')}.json", "w", encoding='utf-8') as f:
    try:
        json.dump(article_dict, f, indent=4, ensure_ascii=False)
        print('Статьи были успешно получены')
    except:
        print('Статьи не удалось получить')