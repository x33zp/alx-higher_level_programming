-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT ts.title, SUM(rate) AS rating
    FROM tv_shows AS ts
    LEFT JOIN tv_show_ratings AS tsr
    ON ts.id = tsr.show_id
    GROUP BY ts.title
    ORDER BY rating DESC;
