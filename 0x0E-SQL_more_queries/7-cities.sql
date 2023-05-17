-- create databse and table
-- id unique, auto generated cant be null PK
-- state_id FK ref to id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE PRIMARY KEY AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL FOREIGN KEY REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
