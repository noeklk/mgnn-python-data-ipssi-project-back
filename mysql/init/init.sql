CREATE DATABASE IF NOT EXISTS plane-analytics;
USE plane-analytics;

DROP TABLE IF EXISTS `planes`;
DROP TABLE IF EXISTS `flight`;

CREATE TABLE planes
(
    id INT PRIMARY KEY NOT NULL,
    tailnum VARCHAR(6),
    `type` VARCHAR(30),
    `year` YEAR
);