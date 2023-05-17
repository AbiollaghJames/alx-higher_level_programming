-- script that lists all cities of california found in the database
USE hbtn_0d_usa;
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
