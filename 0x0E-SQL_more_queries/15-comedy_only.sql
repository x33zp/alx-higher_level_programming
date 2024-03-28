-- Lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT ts.title
    FROM tv_shows AS ts INNER JOIN tv_show_genres AS tsg
    ON ts.id = tsg.show_id
    INNER JOIN tv_genres AS tg
    ON tg.id = tsg.genre_id
    WHERE tg.name = 'Comedy'
    ORDER BY ts.title;
