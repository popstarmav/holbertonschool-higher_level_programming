-- Create 'id_not_null' table:
-- - id: INT (default 1, not null)
-- - name: VARCHAR(256)
-- Database name is provided as an argument.

-- Won't fail if 'id_not_null' table exists.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
