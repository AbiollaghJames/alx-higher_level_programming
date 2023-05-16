-- script that displays the top 3 of cities temp during july and august ordered by temp DESC
SELECT city, AVG(value) AS avg_temp FROM temparatures WHERE (month = 7 OR month = 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
