-- script to list all genres of the show Dexter
SELECT name FROM tv_genres JOIN tv_shows ON id = tv_show_genres.genre_id WHERE tv_shows.title = 'Dexter' ORDER BY name;
