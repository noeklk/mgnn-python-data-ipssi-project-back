CREATE DATABASE IF NOT EXISTS `airport-analytics` CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `airport-analytics`;

DROP TABLE IF EXISTS `planes`;
DROP TABLE IF EXISTS `flights`;
DROP TABLE IF EXISTS `airports`;
DROP TABLE IF EXISTS `airlines`;

CREATE TABLE airlines
(
    carrier VARCHAR(2) PRIMARY KEY NOT NULL,
    `name` VARCHAR(50)
) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE TABLE planes
(
    tailnum VARCHAR(6) PRIMARY KEY NOT NULL,
    `type` VARCHAR(30),
    `year` SMALLINT,
    manufacturer VARCHAR(50),
    model VARCHAR(30),
    engines TINYINT,
    seats SMALLINT,
    speed SMALLINT,
    engine VARCHAR(30),
    carrier VARCHAR(2),
    FOREIGN KEY (carrier) REFERENCES airlines (`carrier`)
) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_general_ci;

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
) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_general_ci;

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
    time_hour DATETIME,
    FOREIGN KEY (tailnum) REFERENCES planes (tailnum)
) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_general_ci;

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
    faa VARCHAR(3),
    FOREIGN KEY (faa) REFERENCES airports (faa)
) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE TABLE airline_airport
(
    id INT NOT NULL AUTO_INCREMENT,
    airline_carrier VARCHAR(2) NOT NULL,
    airport_faa VARCHAR(3) NOT NULL,
    PRIMARY KEY (id, airline_carrier, airport_faa),
    CONSTRAINT `constr_airline_airport_airline_fk` 
		FOREIGN KEY `airline_fk` (airline_carrier) REFERENCES airlines (carrier)
        ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT `constr_airline_airport_airport_fk` 
		FOREIGN KEY `airport_fk` (airport_faa) REFERENCES airports (faa)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_general_ci;