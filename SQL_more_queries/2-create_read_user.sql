--creates the database hbtn_0d_2 and the user user_0d_2
-- Create the hbtn_0d_2 database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Check if the user already exists
-- If the user doesn't exist, create it and grant privileges
SELECT user FROM mysql.user WHERE user = 'user_0d_2';
CREATE USER IF NOT EXISTS 'user_0d_2'@'%' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'%';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
