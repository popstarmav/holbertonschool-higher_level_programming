-- List cities in California from the 'hbtn_0d_usa' database.
-- Results sorted by city ID in ascending order.
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
