-- show the average temperature by city, ordered in descending order
SOURCE temperatures.sql;
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
