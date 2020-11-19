-- List all cities and states
-- SELECT AND JOIN
SELECT tv_s.title, tv_sg.genre_id
FROM tv_shows AS tv_s
INNER JOIN tv_show_genres AS tv_sg
ON tv_s.id=tv_sg.show_id
ORDER BY tv_s.title, tv_sg.genre_id;
