SELECT t.title, t.description, s.name AS status
FROM tasks t
LEFT JOIN status s ON t.status_id = s.id
WHERE t.user_id = 30;

SELECT title, description
FROM tasks
WHERE status_id = (SELECT id FROM status WHERE name = 'new');

UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress')
WHERE id = 2;

SELECT * FROM users
WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Prepare report', 'Prepare monthly report for data collection', 1, 1);

SELECT *
FROM tasks
WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

DELETE FROM tasks
WHERE id = 1;

SELECT *
FROM users
WHERE email LIKE '%gmail.com';

UPDATE users
SET fullname = 'Julia Roberts'
WHERE id = 1;

SELECT status.name, COUNT(tasks.id) AS task_count
FROM tasks
JOIN status ON tasks.status_id = status.id
GROUP BY status.name;

SELECT tasks.*
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@hotmail.com';

SELECT *
FROM tasks
WHERE description IS NULL OR description = '';

SELECT u.fullname, t.title, t.description
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
INNER JOIN status s ON t.status_id = s.id
WHERE s.name = 'in progress';

SELECT u.fullname, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;
