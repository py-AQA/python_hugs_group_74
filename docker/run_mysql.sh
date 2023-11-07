#!/bin/bash
# Запустить контейнер MySQL
export DATA=/Users/x/Desktop/my-super-sql/
docker run --name my-super-sql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=my-secret-pw -v $DATA:/var/lib/mysql mysql:latest

# Параметры:
# --name mysql-x                - Имя, которое вы хотите присвоить вашему контейнеру
# -e MYSQL_ROOT_PASSWORD=...    - Установить переменную окружения MYSQL_ROOT_PASSWORD,
#                                 которая определяет пароль пользователя root в MySQL
# -d                           - Запустить контейнер в фоновом режиме
# mysql:tag                    - Имя образа и его тег; tag может быть, например, 'latest'
# -p 3306:3306                 - Чтобы подключаться к MySQL c хост машины
# Для сохранения данных, которые будут сохраняться после перезапуска контейнера, вы должны примонтировать том