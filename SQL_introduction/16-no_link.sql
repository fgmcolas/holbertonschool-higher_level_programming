-- List all records of the table having a name value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;