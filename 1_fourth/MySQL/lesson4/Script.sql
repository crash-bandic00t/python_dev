/* 
 * Задание 1. 
 * Применил скрипт *.sql для заполнения БД с сайта http://filldb.info/. Для выполнения 4 задания изменил
 * параметр даты созданного сообщения до максимально 2100 года.
 * 
 * 
 * Задание 2. 
 * Написать скрипт, возвращающий список имен (только firstname) пользователей без повторений в алфавитном порядке.
 */
select distinct firstname from users order by firstname;


/*
 * Задание 3. 
 * Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных (поле is_active = false). 
 * Предварительно добавить такое поле в таблицу profiles со значением по умолчанию = true (или 1). 
 */

-- добавляем колонку is_active
alter table profiles 
add is_active BOOL default true;

-- деактивируем пользователей менее 18 лет.
update profiles 
set is_active = false
where 
	(YEAR(CURRENT_DATE)-YEAR(`birthday`))-(RIGHT(CURRENT_DATE,5)<RIGHT(`birthday`,5)) < 18;


/*
 * Задание 4.
 * Написать скрипт, удаляющий сообщения «из будущего» (дата больше сегодняшней)
 */

delete from messages
where created_at > now();

select * from messages;



