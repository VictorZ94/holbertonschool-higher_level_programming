-- List all cities and states
-- SELECT AND JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id=states.id;
