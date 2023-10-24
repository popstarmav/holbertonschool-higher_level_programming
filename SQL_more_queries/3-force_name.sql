-- Create the 'force_name' table on your MySQL server.
-- Description of 'force_name' table:
-- - id: Integer (INT)
-- - name: String (VARCHAR) with a maximum length of 256 characters, and it can't be null.

-- The script assumes that the database name will be passed as an argument to the mysql command.

-- The script won't fail if the 'force_name' table already exists.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
