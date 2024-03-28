-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tg.name genre, count(tsg.show_id) number_of_shows
    FROM tv_genres tg INNER JOIN tv_show_genres tsg
        ON tg.id = tsg.genre_id
    GROUP BY genre
    ORDER BY number_of_shows DESC;
