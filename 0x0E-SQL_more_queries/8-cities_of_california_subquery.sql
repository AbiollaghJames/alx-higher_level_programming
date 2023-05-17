-- script that lists all cities of california found in the database
SELECT id, name FROM cities, states WHERE statte_id = (SELECT id FROM states WHERE nme = "California") ORDER BY id;
