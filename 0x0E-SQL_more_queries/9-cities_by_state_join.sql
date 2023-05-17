-- script that lists cities in db
SELECT id, name FROM cities UNION SELECT name FROM states ORDER BY id ASC;
