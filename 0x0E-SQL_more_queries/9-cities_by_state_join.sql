-- list all cities
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON state_id = states.id ORDER BY id;