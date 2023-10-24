-- List genres from 'hbtn_0d_tvshows' with the number of linked shows.
-- Display: <Genre> - <Number of shows>.
-- First column: genre.
-- Second column: number_of_shows.
-- Exclude genres without linked shows.
-- Sort by the number of shows in descending order.
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
