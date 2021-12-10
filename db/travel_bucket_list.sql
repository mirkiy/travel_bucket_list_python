DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    capital VARCHAR(255)
);

CREATE TABLE cities(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    population INT,
    review VARCHAR(255),
    -- review TEXT ??? from quest advisor - check
    sights VARCHAR(255),
    country_id INT REFERENCES countries(id)
);