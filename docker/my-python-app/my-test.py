#!/usr/bin/env python3
# Импортируем необходимые библиотеки
import os

import mysql.connector as db
import requests


# Функция для проверки статуса веб-страницы
def check_website(url):
    try:
        response = requests.get(url)  # GET-запрос
        # Выводим статус-код ответа
        print(f'Статус-код ответа для {url}: {response.status_code}')
        assert response.status_code == 200, 'Страница открылась'
    except requests.exceptions.RequestException as e:
        # В случае ошибки выводим сообщение
        print(f'Ошибка при запросе к {url}: {e}')


def my_db():
    print('Подключаемся к базе данных')
    mydb = db.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
    )

    cur = mydb.cursor()
    print(f"Получили курсор {cur}")
    cur.execute("SELECT * FROM user")
    r = cur.fetchall()
    for row in r:
        print(row)


# Основная точка входа в программу
if __name__ == '__main__':
    print('Привет от Docker! Вы такие молодцы!!!')
    # Задаем URL, который будем проверять
    test_url = 'https://www.google.com'
    # Вызываем функцию проверки
    check_website(test_url)
    my_db()
