-- creating a view need_meeting

CREATE VIEW need_meeting AS SELECT name FROM students
WHERE score < 80 AND (last_meeting IS NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH));
