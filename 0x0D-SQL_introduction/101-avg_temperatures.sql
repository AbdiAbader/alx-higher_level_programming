-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, (SELECT AVG(value) FROM temperatures) FROM temperatures ORDER BY value DESC;