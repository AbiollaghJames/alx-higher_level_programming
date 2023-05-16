-- script that lists all records with score >= 10 in table of database in MySQL server
-- result should display score and name
-- record should be ordered by score (DESC)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC
