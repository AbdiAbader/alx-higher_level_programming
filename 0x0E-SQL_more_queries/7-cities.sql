--  creates the database hbtn_0d_usa and the table cities
E DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, CONSTRAINT Customers_pk PRIMARY KEY (id), state_id INT NOT NULL FOREIGN KEY (state_id) REFERENCES states(state_id));