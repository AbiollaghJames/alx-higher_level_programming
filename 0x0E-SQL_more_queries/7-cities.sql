-- create databse and table
-- id unique, auto generated cant be null PK
-- state_id FK ref to id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, state_id INT NOT NULL FOREIGN KEY REFERENCES states(id), name VARCHAR(256) NOT NULL);
