-- lists all rows with non-null name values in the table "second_table"
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
