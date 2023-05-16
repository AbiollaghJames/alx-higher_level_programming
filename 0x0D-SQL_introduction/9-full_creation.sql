-- script that creates a table in a database and adds multiple rows in MySQL
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

INSERT INTO second_table (id INT, name VARCHAR(256), score INT)
	SELECT 1, 'John', 10
	UNION ALL
	SELECT 2, 'Alex', 3
	UNION ALL
	SELECT 3, 'Bob', 14
	UNION ALL
	SELECT 4, 'George', 8;
