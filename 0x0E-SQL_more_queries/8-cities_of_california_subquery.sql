-- script that lists all cities of california found in the database
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id ASC;
