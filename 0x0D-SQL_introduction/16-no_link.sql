-- script that lists all records of the table
-- Don't list rows without a name value, result should display score and name
-- Records listed in DESC by score
SELECT score, name FROM second_table WHERE name <> '' ORDER BY score DESC;
