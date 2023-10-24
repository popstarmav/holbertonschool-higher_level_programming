-- List all genres of the show 'Dexter' from 'hbtn_0d_tvshows' database.
-- Display: name.
-- Sort by genre name in ascending order.
SELECT name
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter')
ORDER BY name ASC;
