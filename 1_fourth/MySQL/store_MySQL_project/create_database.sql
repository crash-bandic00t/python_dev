DROP DATABASE IF EXISTS store;
CREATE DATABASE store;
USE store;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL, 
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    email VARCHAR(120) UNIQUE,
 	password_hash VARCHAR(100),
	phone BIGINT UNSIGNED UNIQUE, 
	
    INDEX users_firstname_lastname_idx(firstname, lastname)
);

DROP TABLE IF EXISTS profiles;
CREATE TABLE profiles (
	user_id BIGINT UNSIGNED NOT NULL UNIQUE,
    gender CHAR(1),
    birthday DATE,
	photo_id BIGINT UNSIGNED NULL,
    created_at DATETIME DEFAULT NOW(),
    hometown VARCHAR(100),
	FOREIGN KEY (user_id) REFERENCES users (id)
);


DROP TABLE IF EXISTS discounts;
CREATE TABLE discounts (
	id SERIAL,
    name VARCHAR(255),
    discount_percent TINYINT UNSIGNED
);


DROP TABLE IF EXISTS product_category;
CREATE TABLE product_category (
	id SERIAL,
    name VARCHAR(255)
);

DROP TABLE IF EXISTS products;
CREATE TABLE products (
	id SERIAL,
    name VARCHAR(255),
    category_id BIGINT UNSIGNED NOT NULL,
    price INT UNSIGNED,
    discount_id BIGINT UNSIGNED NULL,
    FOREIGN KEY (discount_id) REFERENCES discounts(id),
    FOREIGN KEY (category_id) REFERENCES product_category(id),

    INDEX products_name (name)
);

DROP TABLE IF EXISTS media_types;
CREATE TABLE media_types(
	id SERIAL,
    name VARCHAR(255)
);

DROP TABLE IF EXISTS media;
CREATE TABLE media(
	id SERIAL,
    media_type_id BIGINT UNSIGNED NOT NULL,
    `filename` VARCHAR(255),
	metadata TEXT,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (media_type_id) REFERENCES media_types(id)
);

DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews(
	id SERIAL,
    product_id BIGINT UNSIGNED NOT NULL,
    body TEXT,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

DROP TABLE IF EXISTS likes;
CREATE TABLE likes(
	id SERIAL,
    product_id BIGINT UNSIGNED NOT null,
    user_id BIGINT UNSIGNED NOT null,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS products_desc;
CREATE TABLE products_desc (
	product_id BIGINT UNSIGNED NOT NULL UNIQUE,
    `description` TEXT,
    media_id BIGINT UNSIGNED NOT null,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (media_id) REFERENCES media(id)
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders(
	id SERIAL,
    user_id BIGINT UNSIGNED NOT null,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
    status ENUM('created', 'declined', 'executed'),
    delivery_status ENUM('packaging', 'sent', 'delivered'),
    payment_status ENUM('paid', 'not paid'),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS order_products;
CREATE TABLE order_products(
    order_id BIGINT UNSIGNED NOT null,
    product_id BIGINT UNSIGNED NOT null,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);




