-- List all Comedy shows in 'hbtn_0d_tvshows'.
-- Display: title.
-- Sort by show title in ascending order.
SELECT title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY title ASC;
