-- script that display average temp by city order by temp in DESC
SELECT city, AVG(values) AS avg_temp FROM temperature GROUP BY city ORDER BY avg_temp DESC;
