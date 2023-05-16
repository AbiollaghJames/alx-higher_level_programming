-- script that creates a table in a database and adds multiple rows in MySQL
INSERT INTO IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT) VALUES
	(1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8);
