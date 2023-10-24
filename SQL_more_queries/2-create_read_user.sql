-- Create the 'hbtn_0d_2' database if it doesn't exist, 
-- and establish a 'user_0d_2' with SELECT privileges in 'hbtn_0d_2'.
-- Set 'user_0d_2's password to 'user_0d_2_pwd'.
-- The script won't fail if 'hbtn_0d_2' or 'user_0d_2' already exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
