-- List all cities and states
-- SELECT AND JOIN
SELECT tv_g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS tv_g
JOIN tv_show_genres AS tv_sg
WHERE tv_g.id = tv_sg.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
