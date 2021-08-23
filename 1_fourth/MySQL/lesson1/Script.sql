/* ������� 1.
 * ���������� ���� MySQL. �������� � �������� ���������� ���� .my.cnf, ����� � ��� ����� � ������, 
 * ������� ���������� ��� ���������.
*/

-- ���� my.cnf
/* � ���� ����� ��������� ������ �� Ubuntu, ������� ����������� ��������� ����������� 
 * � �������� ������. ������� �� ������� ��� ������� ������ � �������� ����, �������
 * ��� ��� �� ������ 
 */

[client]
user=crash
host=192.168.2.12

/* ������� 2.
 * �������� ���� ������ example, ���������� � ��� ������� users, 
 * ��������� �� ���� ��������, ��������� id � ���������� name.
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

/* ������� 3.
 * �������� ���� ���� ������ example �� ����������� �������, ���������� 
 * ���������� ����� � ����� ���� ������ sample.
 */

-- ������� ��� ����� example:
sudo mysqldump example > dump_example.sql

-- ������� ����� ����
CREATE DATABASE sample;

-- ������� ��� �������������� �����:
sudo mysql sample < dump_example.sql


/* ������� 4.
 * (�� �������) ������������ ����� �������� � ������������� ������� mysqldump. 
 * �������� ���� ������������ ������� help_keyword ���� ������ mysql. 
 * ������ ��������� ����, ����� ���� �������� ������ ������ 100 ����� �������.
 */

-- ������� ��� �����:
mysqldump -p mysql help_keyword --where="true limit 100" > dump_keyword.sql


