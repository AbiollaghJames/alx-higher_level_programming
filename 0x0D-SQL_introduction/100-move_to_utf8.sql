-- script that converts db_name, tb_name, col_name to UTF8(utf8mb4, collate utf8mb4_unicode_ci)
USE hbtn_0c_0i;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
