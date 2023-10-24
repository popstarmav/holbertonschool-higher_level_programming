--creates the database hbtn_0d_2 and the user user_0d_2-- 
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;

-- Create the user if it doesn't exist and set the password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privileges on the hbtn_0d_2 database to the user
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
