-- script that creates database
--- create a table with following descriptions
-- id int unique auto generated can't be null and name varchar
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL IDENTITY(1, 1) PRIMARY KEY UNIQUE,
	name VARCHAR(256) NOT NULL
);