-- lists all cities in the database in ascending order
SELECT cities.id AS id,
    cities.name AS name,
    states.name As name
FROM cities INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id;
