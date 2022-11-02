-- script that lists all the cities of California
use hbtn_0d_usa;
SELECT id, name FROM cities WHERE states.id = 1;