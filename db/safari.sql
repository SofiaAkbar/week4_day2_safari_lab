DROP TABLE IF EXISTS staff;

CREATE TABLE staff (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    start_date VARCHAR(255),
    dept VARCHAR(255),
    performance INT
    );