/*
 * Задание 1.
 * Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем. 
 */

DROP DATABASE IF EXISTS main;
CREATE DATABASE main;
USE main;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL, 
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    birthday DATE default null,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP
    );
    
insert into users (firstname, lastname, birthday, created_at, updated_at) values # Это если юзеров нет в таблице
	('Maria', 'Ivanova', '2002-05-25', now(), now()),
	('Stepan', 'Petrov', '1992-11-02', now(), null),
	('Sasha', 'Fedorov', '1994-08-15', null, null);

update users 	# Это если юзеры уже есть в таблице
	set created_at = now(),
		updated_at = now();

/*
 * Задание 2.
 * Таблица users была неудачно спроектирована.
 * Записи created_at и updated_at были заданы типом VARCHAR и в них
 * долгое время помещались значения в формате "20.10.2017 8:10".
 * Необходимо преобразовать поля к типу DATETIME, сохранив введеные ранее значения.
 * "20.10.2017 8:10" 
 */

DROP TABLE IF EXISTS dt;
CREATE TABLE dt (
	created_at VARCHAR(50),
	updated_at VARCHAR(50)
	);
insert into dt (created_at, updated_at)
values ('20.10.2017 8:10', '11.12.2019 3:45');

update dt
	set created_at = STR_TO_DATE(`created_at`, '%d.%m.%Y %l:%i'),
		updated_at = STR_TO_DATE(`updated_at`, '%d.%m.%Y %l:%i');

alter table dt
	modify created_at DATETIME,
	modify updated_at DATETIME; 

select * from dt

/*
 * Задание 3.
 * В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры:
 * 0, если товар закончился и выше нуля, если на складе имеются запасы.
 * Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения
 * значения value. Однако, нулевые запасы должны выводиться в конце, после всех записей.
 */

DROP TABLE IF EXISTS storehouses_products;
CREATE TABLE storehouses_products (
	name VARCHAR(50),
	value SMALLINT unsigned
	);

insert into storehouses_products (name, value)
values 
	('видеокарты', 2500),
	('процессоры', 0),
	('ОЗУ', 500),
	('монитор', 0),
	('SSD', 30),
	('HDD', 1);

select name, value,
    if(value > 0, 1, 0) as `count`
from storehouses_products order by `count` desc, value;

		










































		
	