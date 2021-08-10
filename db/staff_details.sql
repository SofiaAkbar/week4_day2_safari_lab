DROP TABLE IF EXISTS staff_details;

CREATE TABLE staff_details (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    start_date VARCHAR(255),
    dept VARCHAR(255),
    perfomance INT
    );