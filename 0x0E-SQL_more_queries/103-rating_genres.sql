-- A script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT g.name, SUM(r.rate) as rating
FROM tv_genres AS g
INNER JOIN tv_show_genres AS s
ON g.id = s.genre_id

INNER JOIN tv_show_ratings as r
ON r.show_id = s.show_id
GROUP BY g.name
ORDER BY rating DESC;
