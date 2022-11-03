-- Dexter
-- SELECT tv_genres.name AS name FROM tv_shows JOIN tv_genres ON  tv_shows.id = tv_genres.id JOIN tv_show_genres ON tv_show_genres.show_id = tv_genres.id;
-- SELECT * FROM tv_genres;
-- SELECT * from tv_show_genres;
-- SELECT * FROM tv_shows;
SELECT tv_genres.name FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id where tv_shows.title = "Dexter";