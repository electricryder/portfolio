SELECT title
FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE name = 'Bradley Cooper' OR name = 'Jennifer Lawrence'
GROUP BY title
HAVING COUNT(DISTINCT name) = 2
;
