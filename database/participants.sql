SELECT users.name
FROM users
JOIN registrations ON registrations.user_id = users.id
WHERE registrations.event_id = :event_id
ORDER BY users.name ASC;
