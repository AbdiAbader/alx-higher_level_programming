-- script that lists all the cities of California
use hbtn_0d_usa;
SELECT id, name FROM cities WHERE states_id = (SELECT id FROM states WHERE name = "California") GROUP BY cities ORDER BY id ASC;