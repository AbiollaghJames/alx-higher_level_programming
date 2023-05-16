-- script that lists number of records with same score in the table
-- result should display the score, number of records for this score with the label number
-- list should be sorted by number of records (DESC)
SELECT score, COUNT('score') AS number FROM second_table GROUP BY score ORDER BY score DESC;
