#!/bin/bash
echo Создаём один раздел для БД
docker volume create postgres_vol_1
# Если нужен будет 2-ой раздел:
#docker volume create postgres_vol_2
echo Создаём одну сеть для двух контейнеров
docker network create app_net
#Supersett install
echo -= Запускаем PostgreSQL =-
echo БД: test_ap
echo Пользователь: postgres
echo Пароль: postgres
docker run --rm -d --name postgres_1 -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e \
POSTGRES_DB=test_ap -v postgres_vol_1:/var/lib/postgresql/data --net=app_net postgres:14
echo -= Запускаем SuperSet =-
docker run -d --rm --net=app_net -p 8080:8088 -e "SUPERSET_SECRET_KEY=1111" --name superset apache/superset

echo -= Создаём пользователя: admin:admin =-
docker exec -it superset superset fab create-admin --username admin --firstname Superset --lastname Admin --email admin@superset.com --password admin
echo -= Загружаем БД для тестов =-
docker exec -it superset superset db upgrade
docker exec -it superset superset load_examples
docker exec -it superset superset init