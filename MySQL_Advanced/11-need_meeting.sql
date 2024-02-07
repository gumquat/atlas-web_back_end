-- create a view `need_meeting` that lists all students
-- that have a score under 80 and no 'last_meeting'
-- or more than 1 month

-- create a view named 'need_meeting' that lists all students needing meeting
CREATE VIEW need_meeting AS SELECT name
-- selecting students from the 'students' table
FROM students
-- filter the students with scores less than 80, AND...
WHERE score < 80
-- check if the last meeting date is not set or happened more than 1month ago
AND (last_meeting IS NULL OR last_meeting < CURDATE() - INTERVAL 1 MONTH);
