-- lists the number of rows with the same score in the table "second_table"
SELECT score, COUNT(score) AS number FROM second_table
ORDER BY number DESC;
