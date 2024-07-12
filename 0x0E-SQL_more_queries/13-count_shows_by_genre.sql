-- lists the genres with the number of shows corresponding to them
SELECT tv_genres.name AS genre,
    COUNT(name) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id

INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id

GROUP BY genre
ORDER BY number_of_shows DESC;
