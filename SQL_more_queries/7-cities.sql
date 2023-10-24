-- Create 'hbtn_0d_usa' database and 'cities' table:
-- - id: INT (auto-generated, unique, primary key)
-- - state_id: INT (not null, foreign key to 'states' table)
-- - name: VARCHAR(256, not null)

-- Won't fail if 'hbtn_0d_usa' database or 'cities' table exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT UNIQUE,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
