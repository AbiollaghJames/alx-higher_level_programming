-- script that display max temp of each state
SELECT state, MAX(value) AS "max_temp" FROM temparatures GROUP BY state ORDER BY state;
