-- script that creates the MySQL server user
-- The user should have all priviledges on MySQL server
-- The user password should be set
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
