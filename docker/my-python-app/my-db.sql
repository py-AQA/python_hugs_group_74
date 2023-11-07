# Создаём базу данных
CREATE DATABASE IF NOT EXISTS my_db;
# create schema my_db;

# Подключаемся к этой базе данных
use my_db;

# Создаём таблицы
create table user
(
    id            int auto_increment primary key,
    login         varchar(1024) charset utf8mb3 not null,
    password_hash varchar(1024) charset utf8mb3 not null
);

# Добавляем записи в БД
INSERT INTO user (login, password_hash)
    VALUE ('admin', md5('admin'));
INSERT INTO user (login, password_hash)
    VALUE ('user', md5('user'));