CREATE DATABASE IF NOT EXISTS `airport-analytics` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
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
    engine VARCHAR(30)
);

CREATE TABLE airports
(
    faa VARCHAR(3) PRIMARY KEY,
    `name` VARCHAR(100),
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
    FOREIGN KEY origin_fk(origin) REFERENCES airports(faa)
);

CREATE INDEX `weather_month_index` ON weather(`month`);
CREATE INDEX `weather_day_index` ON weather(`day`);
CREATE INDEX `weather_hour_index` ON weather(`hour`);
CREATE INDEX `weather_origin_index` ON weather(`origin`);

CREATE TABLE flights
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    `year` SMALLINT,
    `month` TINYINT,
    `day` TINYINT,
    dep_time SMALLINT,
    sched_dep_time SMALLINT,
    dep_delay SMALLINT,
    arr_time SMALLINT,
    sched_arr_time SMALLINT,
    arr_delay SMALLINT,
    carrier VARCHAR(2),
    flight SMALLINT,
    tailnum VARCHAR(6),
    origin VARCHAR(3),
    dest VARCHAR(3),
    air_time SMALLINT,
    distance SMALLINT,
    hour TINYINT,
    minute TINYINT,
    time_hour DATETIME,
    FOREIGN KEY tailnum_fk(tailnum) REFERENCES planes(tailnum),
    FOREIGN KEY carrier_fk(carrier) REFERENCES airlines(carrier),
    FOREIGN KEY dest_fk(dest) REFERENCES airports(faa),
    FOREIGN KEY origin_airports_fk(origin) REFERENCES airports(faa),
    FOREIGN KEY year_fk(`year`) REFERENCES weather(`year`),
    FOREIGN KEY month_fk(`month`) REFERENCES weather(`month`),
    FOREIGN KEY day_fk(`day`) REFERENCES weather(`day`),
    FOREIGN KEY hour_fk(hour) REFERENCES weather(hour),
    FOREIGN KEY origin_weather_fk(origin) REFERENCES weather(origin)
);

CREATE TABLE airline_airport
(
    id INT AUTO_INCREMENT,
    airline_carrier VARCHAR(2) NOT NULL,
    airport_faa VARCHAR(3) NOT NULL,
    PRIMARY KEY (id, airline_carrier, airport_faa),
        CONSTRAINT `constr_airline_airport_airline_fk` 
		FOREIGN KEY `airline_fk` (airline_carrier) REFERENCES airlines (carrier)
        ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT `constr_airline_airport_airport_fk` 
		FOREIGN KEY `airport_fk` (airport_faa) REFERENCES airports (faa)
        ON DELETE CASCADE ON UPDATE CASCADE
);