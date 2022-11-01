-- tops 3 temprature
SELECT city, avg_temp FROM tempratures where month = 7 AND month = 8 ORDER BY avg_temp DESC LIMIT 3