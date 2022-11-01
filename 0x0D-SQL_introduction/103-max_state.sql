-- max of al city
SELECT state, (SELECT MAX(value) FROM temperatures) as max_temp FROM temperatures GROUP BY state ORDER BY state DESC;