--creates the database hbtn_0d_2 and the user user_0d_2-- 
-- Create the hbtn_0d_2 database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the 'user_0d_2' user at 'localhost' and set the password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to the 'user_0d_2' on the 'hbtn_0d_2' database
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
