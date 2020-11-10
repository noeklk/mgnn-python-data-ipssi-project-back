CREATE DATABASE IF NOT EXISTS `plane-analytics`;
USE `plane-analytics`;

DROP TABLE IF EXISTS `planes`;
DROP TABLE IF EXISTS `flight`;

CREATE TABLE planes
(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    tailnum VARCHAR(6),
    `type` VARCHAR(30),
    `year` YEAR,
    manufacturer VARCHAR(50),
    model VARCHAR(20),
    engines TINYINT,
    seats SMALLINT,
    speed SMALLINT,
    engine VARCHAR(20)
);

CREATE TABLE airports
(
    faa VARCHAR(3) PRIMARY KEY NOT NULL,
    `name` VARCHAR(50),
    lat FLOAT,
    lon FLOAT,
    alt SMALLINT,
    tz SMALLINT,
    dst CHAR,
    tzone VARCHAR(30)
)
