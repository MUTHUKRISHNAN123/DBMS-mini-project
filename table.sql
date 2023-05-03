-- CREATE DATABASE movie_booking_system;

-- USE movie_booking_system;

-- CREATE TABLE customer (
--   id INT(11) NOT NULL AUTO_INCREMENT,
--   name VARCHAR(50) NOT NULL,
--   email VARCHAR(50) NOT NULL,
--   PRIMARY KEY (id)
-- );

-- CREATE TABLE theater (
--   id INT(11) NOT NULL AUTO_INCREMENT,
--   name VARCHAR(50) NOT NULL,
--   address VARCHAR(100) NOT NULL,
--   city VARCHAR(50) NOT NULL,
--   PRIMARY KEY (id),
--   INDEX (name)
-- );

-- CREATE TABLE movies (
--   id INT(11) NOT NULL AUTO_INCREMENT,
--   movie_name VARCHAR(50) NOT NULL,
--   theater VARCHAR(50) NOT NULL,
--   timing VARCHAR(50) NOT NULL,
--   center VARCHAR(50) NOT NULL,
--   city VARCHAR(50) NOT NULL,
--   ticket_price DECIMAL(10, 2) NOT NULL,
--   PRIMARY KEY (id),
--   FOREIGN KEY (theater) REFERENCES theater(name),
--   INDEX (city, center)
-- );