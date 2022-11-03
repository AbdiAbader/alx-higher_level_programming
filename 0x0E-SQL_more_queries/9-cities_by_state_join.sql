-- list all cities
SELECT id, name, states.name FROM cities JOIN states ON state_id = states.id ORDER BY id;