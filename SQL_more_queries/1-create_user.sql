-- Create a user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant specific privileges to the user
GRANT SELECT, INSERT, UPDATE ON your_database.* TO 'user_0d_2'@'localhost';`
