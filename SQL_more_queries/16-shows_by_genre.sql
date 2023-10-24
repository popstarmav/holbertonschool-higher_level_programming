-- List shows and their linked genres from 'hbtn_0d_tvshows'.
-- Display: title - name.
-- If a show doesn’t have a genre, display NULL in the genre column.
-- Sort by title and genre name in ascending order.
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
RIGHT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
