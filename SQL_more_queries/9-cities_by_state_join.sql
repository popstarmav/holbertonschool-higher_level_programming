-- List all cities from the 'hbtn_0d_usa' database.
-- Display: cities.id - cities.name - states.name
-- Sorted by city ID in ascending order.
-- Use a single SELECT statement.
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
