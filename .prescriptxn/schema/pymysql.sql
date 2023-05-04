DROP SCHEMA IF EXISTS prescriptxn;
CREATE SCHEMA prescriptxn;
USE prescriptxn;

DROP TABLE IF EXISTS users;
CREATE TABLE users(
    userID SMALLINT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    birthday DATE NOT NULL,
    address VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    province VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY(userID)
);
