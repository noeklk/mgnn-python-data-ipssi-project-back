CREATE DATABASE IF NOT EXISTS test;
USE test;

CREATE TABLE IF NOT EXISTS planes
(
    id INT PRIMARY KEY NOT NULL,
    tailnum VARCHAR(50),
    year VARCHAR(50)
);

-- CREATE TABLE IF NOT EXISTS flight
-- (
--     id INT PRIMARY KEY NOT NULL,
--     aeroport_depart VARCHAR(50),
--     aeroport_arrive VARCHAR(50),
--     plane_id int FOREIGN KEY REFERENCES plane(id)
-- );