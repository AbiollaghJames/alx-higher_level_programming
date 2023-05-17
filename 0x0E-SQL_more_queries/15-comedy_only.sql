-- script that list all comedy shows in db
SELECT title FROM tv_shows JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_genres.name = 'Comedy' ORDER BY title;
