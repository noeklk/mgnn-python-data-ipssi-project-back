CREATE DATABASE `airport-analytics` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `airport-analytics`;

CREATE TABLE airlines
(
    carrier VARCHAR(2) PRIMARY KEY,
    `name` VARCHAR(50)
);

CREATE TABLE planes
(
    tailnum VARCHAR(6) PRIMARY KEY,
    `type` VARCHAR(30),
    `year` SMALLINT,
    manufacturer VARCHAR(50),
    model VARCHAR(30),
    engines TINYINT,
    seats SMALLINT,
    speed SMALLINT,
    engine VARCHAR(30),
    carrier VARCHAR(2)
);

CREATE TABLE flights
(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `year` TINYINT,
    `month` TINYINT,
    `day` TINYINT,
    dep_time SMALLINT,
    sched_dep_time SMALLINT,
    dep_delay SMALLINT,
    arr_time SMALLINT,
    arr_delay SMALLINT,
    carrier SMALLINT,
    flight SMALLINT,
    tailnum VARCHAR(6),
    origin VARCHAR(3),
    dest VARCHAR(3),
    air_time SMALLINT,
    distance SMALLINT,
    hour TINYINT,
    minute TINYINT,
    time_hour DATETIME
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
);

CREATE TABLE weather
(
    origin VARCHAR(3),
    `year` SMALLINT,
    `month` TINYINT,
    `day` TINYINT,
    `hour` TINYINT,
    temp FLOAT,
    dewp FLOAT,
    humid FLOAT,
    wind_dir SMALLINT,
    wind_speed FLOAT,
    wind_gust FLOAT,
    precip FLOAT,
    pressure FLOAT,
    visib FLOAT,
    time_hour DATETIME,
    PRIMARY KEY (`year`, `month`, `day`, hour, origin),
    faa VARCHAR(3)
);

CREATE TABLE airline_airport
(
    id INT NOT NULL AUTO_INCREMENT,
    airline_carrier VARCHAR(2) NOT NULL,
    airport_faa VARCHAR(3) NOT NULL,
    PRIMARY KEY (id, airline_carrier, airport_faa)
);