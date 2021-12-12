DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    capital VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    country_id INT REFERENCES countries(id),
    name VARCHAR(255),
    population INT,
    review INT,
    -- review TEXT ??? from quest advisor - check
    sights VARCHAR(255),
    visited BOOLEAN
);