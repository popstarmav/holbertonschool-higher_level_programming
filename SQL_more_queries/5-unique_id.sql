-- Create 'unique_id' table with:
-- - id: INT (default 1, unique)
-- - name: VARCHAR(256)
-- Database name is provided as an argument.

-- Won't fail if 'unique_id' table exists.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
