-- “аблица со списком друзей пользователей:
DROP TABLE IF EXISTS users_friends;
CREATE TABLE users_friends(
	user_id BIGINT UNSIGNED NOT NULL,
	friend_id BIGINT UNSIGNED NOT NULL,
  
	PRIMARY KEY (user_id, friend_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (friend_id) REFERENCES users(id)
);

-- “аблица с запланированными меропри€ти€ми
DROP TABLE IF EXISTS users_meetings; 
DROP TABLE IF EXISTS meetings; 
/*
 * интересно, что нельз€ дропнуть таблицу, 
 * до того как удалены все св€занные с ней ключи и поэтому если
 * не дропать базу полностью, перед его повторным выполнением
 * выползет ошибка 
 */
CREATE TABLE meetings(
	id SERIAL,
	name VARCHAR(150),
	date_time DATETIME NOT NULL
);

-- “аблица участников меропри€тий (встреч)


CREATE TABLE users_meetings(
	user_id BIGINT UNSIGNED NOT NULL,
	meeting_id BIGINT UNSIGNED NOT NULL,
  
	PRIMARY KEY (user_id, meeting_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (meeting_id) REFERENCES meetings(id)
);

-- “аблица с университетами, дл€ заполнени€ места учебы

DROP TABLE IF EXISTS school;
CREATE TABLE school (
	id SERIAL, 
    name VARCHAR(100),
    start_date DATE,
    end_date DATE,
	faculty VARCHAR(50),
    
    INDEX school_idx(name)
);

-- ƒобавление в таблицу profiles пол€ про университет или школу и создание внешнего ключа
ALTER TABLE profiles ADD school_id BIGINT UNSIGNED NOT NULL;
ALTER TABLE profiles 
ADD CONSTRAINT schools_fk 
FOREIGN KEY (school_id) REFERENCES school(id);

