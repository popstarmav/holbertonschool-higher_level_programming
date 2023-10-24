-- List shows from 'hbtn_0d_tvshows' with linked genres.
-- Display: title - genre_id.
-- Sorted by title and genre_id in ascending order.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
