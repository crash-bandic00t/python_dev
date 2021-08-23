/* Задание 1.
 * Установите СУБД MySQL. Создайте в домашней директории файл .my.cnf, задав в нем логин и пароль, 
 * который указывался при установке.
*/

-- файл my.cnf
/* у меня стоит отдельная машина на Ubuntu, поэтому использовал удаленное подключение 
 * с основной машины. Немного не понятно как хранить пароль в открытом виде, поэтому
 * тут его не указал 
 */

[client]
user=crash
host=192.168.2.12

/* Задание 2.
 * Создайте базу данных example, разместите в ней таблицу users, 
 * состоящую из двух столбцов, числового id и строкового name.
 */ 

DROP DATABASE IF EXISTS example;
CREATE DATABASE example;
USE example;
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255)
);

SELECT * FROM users

/* Задание 3.
 * Создайте дамп базы данных example из предыдущего задания, разверните 
 * содержимое дампа в новую базу данных sample.
 */

-- Команда для дампа example:
sudo mysqldump example > dump_example.sql

-- Создаем новую базу
CREATE DATABASE sample;

-- Команда для разворачивания дампа:
sudo mysql sample < dump_example.sql


/* Задание 4.
 * (по желанию) Ознакомьтесь более подробно с документацией утилиты mysqldump. 
 * Создайте дамп единственной таблицы help_keyword базы данных mysql. 
 * Причем добейтесь того, чтобы дамп содержал только первые 100 строк таблицы.
 */

-- Команда для дампа:
mysqldump -p mysql help_keyword --where="true limit 100" > dump_keyword.sql


