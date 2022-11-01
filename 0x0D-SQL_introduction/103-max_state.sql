-- max of al city
SELECT city, (SELECT MAX(value) FROM temperatures) FROM temperatures GROUP BY city ORDER BY state DESC;