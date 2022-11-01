-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, (SELECT AVG(value) FROM temperatures) as avg_temp FROM temperatures ORDER BY value DESC;