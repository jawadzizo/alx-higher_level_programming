-- changes the encoding of the database "hbtn_0c_0" to utf8mb4, collate utf8mb4_unicode_ci
USE hbtn_0c_0;
ALTER TABLE first_table CHANGE `name` TEXT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
