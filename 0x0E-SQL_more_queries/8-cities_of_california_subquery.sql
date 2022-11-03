-- script that lists all the cities of California
use hbtn_0d_usa;
SELECT id, name FROM cities WHERE states_id IN (SELECT id FROM states WHERE name = "California") ORDER BY id;