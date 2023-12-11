**Что такое Docker и как он может быть полезен для QA?**

Установка и настройка Docker
============================

**Установка Docker в Windows**

https://docs.docker.com/desktop/install/windows-install/

Проверка, что Docker работает:

```sh
docker --version
```

У меня в Windows выводится:

```
Docker version 24.0.6, build ed223bc
```

Проверка, что Docker работает:

```sh
docker run hello-world
```

**Установка Docker в Linux и MacOS**
https://docs.docker.com/desktop/install/mac-install/

```sh
brew install docker docker-compose docker-machine
brew install --cask virtualbox
```

```sh
docker-machine create --driver virtualbox default
```

https://hub.docker.com/repositories/stden

Авторизуйтесь в Docker Hub через командную строку:

```sh
docker login
```

Основы Dockerfile: создание образа для тестовой среды.
Интеграция Docker с Python.

```Dockerfile
# Используем официальный образ Python как родительский образ
FROM python:latest
# Установим рабочий каталог в контейнере
WORKDIR /app
# Скопируем файл с зависимостями в рабочий каталог
COPY requirements.txt ./
# Установим все необходимые библиотеки из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Установим команду tree внутрь контейнера
RUN apt-get update && apt-get install -y tree
# Копируем файл скрипта в рабочую директорию
COPY my-test.py /app
# Скопируем содержимое локального каталога в рабочий каталог контейнера
COPY . .
# Команда, которая будет выполнена при запуске контейнера
CMD ["python", "./my-test.py"]
```

Docker Compose
==============

Чтобы собрать среду с Python и MySQL для запуска модульных тестов, вам потребуется использовать Docker Compose.
Docker Compose позволяет определить и запустить много-контейнерные приложения Docker с помощью простого файла YAML. Вот
как это можно сделать:

```sh
docker-compose up --build
```

```sh
docker-compose exec app python -m unittest discover -s tests
```

Тома и хранение данных: сохранение результатов тестов.

Запуск баз данных, таких как MySQL и PostgreSQL, в Docker можно выполнить с использованием официальных образов из
Docker Hub.

```sh
# Запустить контейнер MySQL
export DATA=/Users/x/Desktop/mysql-data
docker run -d mysql:latest --name mysql-x -p 3306:3306 -e MYSQL_ROOT_PASSWORD=admin12345 $DATA:/var/lib/mysql

# Параметры:
# --name mysql-x                - Имя, которое вы хотите присвоить вашему контейнеру
# -e MYSQL_ROOT_PASSWORD=...    - Установить переменную окружения MYSQL_ROOT_PASSWORD,
#                                 которая определяет пароль пользователя root в MySQL
# -d                           - Запустить контейнер в фоновом режиме
# mysql:tag                    - Имя образа и его тег; tag может быть, например, 'latest'
# -p 3306:3306                 - Чтобы подключаться к MySQL c хост машины
# Для сохранения данных, которые будут сохраняться после перезапуска контейнера, вы должны примонтировать том
```

```sh
docker stop mysql-x
docker rm -f mysql-x 
```

PostgreSQL
----------

```sh
# Запустить контейнер PostgreSQL
docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres:latest

# Параметры:
# --name some-postgres          - Имя, которое вы хотите присвоить вашему контейнеру
# -e POSTGRES_PASSWORD=...      - Установить переменную окружения POSTGRES_PASSWORD,
#                                 которая определяет пароль для пользователя postgres
# -d                           - Запустить контейнер в фоновом режиме
# postgres:tag                 - Имя образа и его тег; tag может быть, например, 'latest'
```

Для сохранения базы данных на хост-машине, вы можете использовать тома:

```sh
docker run --name some-postgres -v /my/own/datadir:/var/lib/postgresql/data -e POSTGRES_PASSWORD=mysecretpassword -d postgres:tag
```

Уборка Docker:
--------------

```sh
docker container prune -f
docker volume prune -f
docker network prune -f
```

Уборка всего мусора:

```sh
docker system prune -f
```