-- script that lists all cities of california found in the database
SET @s_id := (SELECT id FROM states WHERE name = 'California');
SELECT * FROM cities WHERE state_id = @s_id ORDER BY id ASC;
