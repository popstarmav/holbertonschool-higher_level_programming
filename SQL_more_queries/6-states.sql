-- Create 'hbtn_0d_usa' database and 'states' table:
-- - id: INT (auto-generated, unique, primary key)
-- - name: VARCHAR(256, not null)

-- Won't fail if 'hbtn_0d_usa' database exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
