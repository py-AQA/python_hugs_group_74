from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from datetime import timedelta, datetime
import time
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

driver = wd.Chrome()
# https://dzen.ru/news/search?issue_tld=ru&text=игра+date%3A20230929..20231005&filter_date=1696013457000%2C1696531857000
# https://dzen.ru/news/search?issue_tld=ru&text=игра+date%3A20230905..20231005&filter_date=1693864800000%2C1696456800000
# https://dzen.ru/news/search?issue_tld=ru&text=игра+date%3A20230901..20231003&filter_date=1693864800000%2C1696456800000
# https://dzen.ru/news/search?issue_tld=ru&text=игра+date%3A20230905..20231005&filter_date=1693864800000%2C1696456800000
# https://dzen.ru/news/search?issue_tld=ru&text=игра+date%3A20230929..20231005&filter_date=1696013457000%2C1696531857000

url_sait = 'https://dzen.ru/news/search?issue_tld=ru'
text_url = 'игра'
date_url = datetime.now()
date_url_befor = datetime.now() - timedelta(30)

date_url_text = date_url_befor.strftime('%Y%m%d') + '..' + date_url.strftime('%Y%m%d')

url_sait = url_sait + '&text='+ text_url + '+date%3A' + date_url_text + '&filter_date=1696013457000%2C1696531857000'

driver.get(url_sait)
driver.implicitly_wait(2)
# time.sleep(2)

# находим кнопку Больше результатов
# share = driver.find_element(By.CLASS_NAME,  'Button2 Button2_view_action Button2_size_m mg-button mg-load-more__button')
# while share:
#     share.click()

title_article = driver.find_element(By.CLASS_NAME, "mg-snippet__title")
# load_content_button = driver.find_element(By.XPATH, "//button")
# vegetable = driver.find_element(By.CLASS_NAME, "tomatoes")

# for e in title_article:
#     print(e.text)
e = title_article.text

requiredHtml = driver.page_source
soup = BeautifulSoup(requiredHtml, 'lxml') # с помощью BeautifulSoup соберем весь html код страницы.

article_list_title, article_list_content =[], []

all_block_title_articles = soup.find_all('div', class_='mg-snippet__title')
all_block_content_articles = soup.find_all('span', class_='mg-snippet__text')
for article in all_block_title_articles:
    # article_name = article.find('span').text  # собираем названия статей
    # article_link = f'https://habr.com{article.get("href")}'  # их ссылки
    article_name = article.find('span').text
    article_list_title.append(article_name)

for article in all_block_content_articles:
    # article_name = article.find('span').text  # собираем названия статей
    # article_link = f'https://habr.com{article.get("href")}'  # их ссылки
    article_name = article.find('span').text
    article_list_content.append(article_name)

str_dobor =''
for article_title, article_content in zip(article_list_title, article_list_content):
    if text_url in article_title:
        str_dobor +=' ' + article_title
    if text_url in article_content:
        str_dobor +=' ' + article_content

str_list = str_dobor.split()
str_list_correct = []

for i in range(len(str_list)):
    str_list[i] = re.sub('(\.+)$|\d\d\.\d\d\.\d{4}|^[«]|[»]$|[—]|^(\.+)', '', str_list[i])
    if str_list[i].isdigit() or str_list[i] == '-' or str_list[i] == '':
        # str_list.pop(i)
        continue

    str_list_correct.append(str_list[i])

str_list = str_list_correct

str_count = {}
for word in str_list:
    if word not in str_count:
        str_count[word] = str_list.count(word)

rezult_all = sorted(str_count.items(), key=lambda x: x[1], reverse=True)
# print(len(rezult_all))
rezult = [x for x, y in rezult_all][:50]

# Creating the text variable
text = ' '.join(rezult)
# print(rezult)

# Generate word cloud
word_cloud = WordCloud(
    width=3000,
    height=2000,
    random_state=1,
    background_color="salmon",
    colormap="Pastel1",
    collocations=False,
    stopwords=STOPWORDS,
).generate(text)

# Display the generated Word Cloud
plt.imshow(word_cloud)
plt.axis("off")
plt.show()

time.sleep(2)