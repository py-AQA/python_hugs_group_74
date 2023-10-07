--Есть база. В ней есть три таблицы
--1) Users(userId, age)
--2) Purchases (purchaseId, userId, itemId, date)
--3) Items (itemId, price).
--
--Необходимо:
-- А) какую сумму в среднем в месяц тратит:
-- по каждому месяцу - пользователи в возрастном диапазоне от 18 до 25 лет включительно
-- - пользователи в возрастном диапазоне от 26 до 35 лет включительно
-- Б) в каком месяце года выручка от пользователей в возрастном диапазоне 35+ самая большая
-- В) какой товар обеспечивает дает наибольший вклад в выручку за последний год
-- Г) топ-3 товаров по выручке и их доля в общей выручке за любой год

--создаем тестовые данные.
--создаем базу и таблицы. Думается, что таблица Purchases связана с Users и Items
CREATE SCHEMA IF NOT EXISTS Test_hr DEFAULT CHARACTER SET utf8 ;
USE Test_hr ;

DROP TABLE IF EXISTS Test_hr.Users ;
CREATE TABLE Test_hr.Users(
	userId INT(11) NOT NULL AUTO_INCREMENT,
	age INT(3) NOT NULL,
	PRIMARY KEY (userId)
)
COLLATE=`utf8_unicode_ci`
ENGINE=InnoDB;

DROP TABLE IF EXISTS Test_hr.Items ;
CREATE TABLE Items (
	itemId INT(11) NOT NULL AUTO_INCREMENT,
	price INT(11) NOT NULL,
	PRIMARY KEY (itemId)
)
COLLATE='utf8_unicode_ci'
ENGINE=InnoDB;

DROP TABLE IF EXISTS Test_hr.Purchases ;
CREATE TABLE Purchases(
purchaseId INT(11) NOT NULL AUTO_INCREMENT,
userId INT(11) NOT NULL,
itemId INT(11) NOT NULL,
`date`  DATE NOT NULL,
PRIMARY KEY (purchaseId),
FOREIGN KEY (userId) REFERENCES Users (userId)
    ON DELETE CASCADE
    ON UPDATE RESTRICT,
FOREIGN KEY (itemId) REFERENCES Items (itemId)
)
COLLATE='utf8_unicode_ci'
ENGINE=InnoDB;

-- Генерация 100 случайных товаров с ценами от 10 до 1000
INSERT INTO Items (itemId, price)
SELECT
  NULL,
  ROUND(RAND() * 990 + 10, 2)
FROM
  information_schema.tables
LIMIT 100;

select * from test_hr.items;

-- Генерация 100 случайных пользователей с возрастом от 18 до 60 лет
INSERT INTO Users (userId, age)
SELECT
  NULL,
  FLOOR(RAND() * 43) + 18
FROM
  information_schema.tables
LIMIT 100;

-- Генерация 100 случайных покупок с существующими userId и itemId
INSERT INTO Purchases (purchaseId, userId, itemId, date)
SELECT
  NULL,
  (SELECT userId FROM Users ORDER BY RAND() LIMIT 1),
  (SELECT itemId FROM Items ORDER BY RAND() LIMIT 1),
  DATE_ADD(CURRENT_DATE, INTERVAL -FLOOR(RAND() * 90) DAY)
FROM
  information_schema.tables
LIMIT 1000;

-- delete date Purchases
TRUNCATE TABLE Purchases;

-- delete table Purchases
drop TABLE Purchases;

select * from test_hr.purchases;

-- А) какую сумму в среднем в месяц тратит:
-- по каждому месяцу - пользователи в возрастном диапазоне от 18 до 25 лет включительно
-- select u.age, avg(i.price) as average, MONTH(pu.`date`) AS `month`
-- from test_hr.purchases as pu
-- join test_hr.users as u on u.userId = pu.userId
-- join test_hr.items as i on i.itemId = pu.itemId
-- group by `month`, u.age
-- having u.age >=18 and u.age <= 25;

-- - пользователи в возрастном диапазоне от 18 до 25 лет включительно
select age, round(avg(average), 2) as average_moth from
	(select u.age, avg(i.price) as average, MONTH(pu.`date`) AS `month`
	from test_hr.purchases as pu
	join test_hr.users as u on u.userId = pu.userId
	join test_hr.items as i on i.itemId = pu.itemId
	group by `month`, u.age
	having u.age >=18 and u.age <= 25) as ppa
group by age
order by age;

-- - пользователи в возрастном диапазоне от 26 до 35 лет включительно
select age, round(avg(average), 2) as average_moth from
	(select u.age, avg(i.price) as average, MONTH(pu.`date`) AS `month`
	from test_hr.purchases as pu
	join test_hr.users as u on u.userId = pu.userId
	join test_hr.items as i on i.itemId = pu.itemId
	group by `month`, u.age
	having u.age >=26 and u.age <= 35) as pvd
group by age
order by age;

-- Б) в каком месяце года выручка от пользователей в возрастном диапазоне 35+ самая большая
-- так как выручка = цена_продажи - цена_затрат, то найти это невозможно, т.к. нет нигда цены затрат
-- если предположить, что имелось ввиду выручка = цена_продажи, то решение следующее
select MONTH(pu.`date`) AS `month`, sum(i.price) as sum_mes
	from test_hr.purchases as pu
	join test_hr.users as u on u.userId = pu.userId
	join test_hr.items as i on i.itemId = pu.itemId
    where u.age >=35 and year(pu.`date`) = year(CURDATE())
	group by `month`
    order by sum_mes desc
    limit 1;

-- В) какой товар обеспечивает дает наибольший вклад в выручку за последний год
-- так как выручка = цена_продажи - цена_затрат, то найти это невозможно, т.к. нет нигда цены затрат
-- если предположить, что имелось ввиду выручка = цена_продажи, то решение следующее
select pu.itemId, sum(it.price) as sum_it
	from test_hr.purchases as pu
	join test_hr.items as it on pu.itemId = it.itemId
	where year(pu.`date`) = year(CURDATE())
	group by pu.itemId
    order by sum_it desc
    limit 1;

-- Г) топ-3 товаров по выручке и их доля в общей выручке за любой год
select itemId, sum_it, round(100* sum_it/all_sum_it, 2) from
	(select pu.itemId, sum(it.price) as sum_it
	from test_hr.purchases as pu
	join test_hr.items as it on pu.itemId = it.itemId
    group by pu.itemId
    order by sum_it desc
    limit 3) as t3
    join
    (select sum(it.price) as all_sum_it
	from test_hr.purchases as pu
	join test_hr.items as it on pu.itemId = it.itemId
    ) as all_sum;

select pu.itemId, sum(it.price) as sum_it
	from test_hr.purchases as pu
	join test_hr.items as it on pu.itemId = it.itemId
    group by pu.itemId
    order by sum_it desc
    limit 3;

select sum(it.price) as all_sum_it
	from test_hr.purchases as pu
	join test_hr.items as it on pu.itemId = it.itemId
    ;