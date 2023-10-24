-- List all shows from 'hbtn_0d_tvshows'.
-- Display: title - genre_id.
-- Sort by title and genre_id in ascending order.
-- Show NULL for shows without a genre.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
