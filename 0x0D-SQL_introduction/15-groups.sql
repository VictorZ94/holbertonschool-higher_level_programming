-- aliad avg and to get averange of field score
SELECT score, COUNT(name) AS "number"
FROM second_table
GROUP BY score
ORDER BY number DESC;
