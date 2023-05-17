-- script that lists shows contained in db that have at least one genre linked
SELECT tv_shows.title, tv_show_genre_id FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id;
