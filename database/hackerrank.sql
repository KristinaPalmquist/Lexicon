-- SELECT city, LENGTH(city) FROM StatusDescription WHERE
-- LENGTH(city) >= (SELECT Max(LENGTH(city)) FROM station ORDER BY LENGTH(city), city)
-- OR
-- -- LENGTH(city) <= (SELECT MIN(LENGTH(city)) FROM station ORDER BY LENGTH(city), city)

-- SELECT ROUND(long_w, 4)
-- FROM station
-- WHERE lat_n = (SELECT MIN(lat_n) FROM station WHERE lat_n > 38.7780);

-- SELECT TO_CHAR(SUM(lat_n), '999999999.00'), 
--     TO_CHAR(SUM(long_w), '999999999.00') 
-- FROM station;


-- SELECT
--   TO_CHAR(
--     ABS(MAX(lat_n) - MIN(lat_n)) + ABS(MAX(long_w) - MIN(long_w)),
--     '999999999.0000'
--   ) AS manhattan_distance
-- FROM station;

-- SELECT
--   TO_CHAR(
--     SQRT(
--         POWER(MAX(lat_n) - MIN(lat_n), 2) + 
--         POWER(MAX(long_w) - MIN(long_w), 2)),
--     '999999999.0000'
--   ) AS euclidean_distance
-- FROM station;

-- SELECT PERCENTILE_CONT(0.5) 
-- WITHIN GROUP (ORDER BY lat_n)
-- FROM station;

-- SELECT lat_n FROM station 
-- ORDER BY lat_n LIMIT 1 
-- OFFSET (select count(*)/2 FROM station);

-- SELECT TO_CHAR(AVG(lat_n), '999999999.0000')
-- FROM (
--   SELECT lat_n, ROW_NUMBER() OVER (ORDER BY lat_n) AS rn, COUNT(*) OVER () AS cnt
--   FROM station
-- ) t
-- WHERE rn IN (FLOOR((cnt + 1) / 2), CEIL((cnt + 1) / 2));

-- SELECT Name, Grade, Marks
-- FROM Students JOIN Grades
-- ON Marks NETWEEN Min_Mark AND Max_Mark
-- ORDER BY Grade DESC, Name, Marks;

-- SELECT Hackers.hacker_id, Hackers.name
-- FROM Hackers 
-- JOIN Submissions ON Hackers.hacker_id = Submissions.hacker_id
-- JOIN Challenges ON Submissions.challenge_id = Challenges.challenge_id
-- JOIN Difficulty ON Challenges.difficulty_level = Difficulty.difficulty_level
-- WHERE Submissions.score = Difficulty.score 
-- GROUP BY Hackers.hacker_id, hackers.name
--     HAVING COUNT(*) > 1
--     ORDER BY COUNT(*) DESC, Hackers.hacker_id

