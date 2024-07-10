-- lists all cities in "California", ordered by city id
SELECT cities.id AS id,
    state_id,
    cities.name AS 'name'
FROM states, cities
WHERE states.name = "California"
ORDER BY cities.id;
