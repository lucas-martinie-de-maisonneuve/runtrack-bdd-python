CREATE DATABASE zoo;

USE zoo;

CREATE TABLE animal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    race VARCHAR(255),
    id_cage INT,
    date_naissance INT,
    pays_origine VARCHAR(255)
);

CREATE TABLE cage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    superficie DECIMAL,
    capacite_max INT
);

INSERT INTO cage (superficie, capacite_max) VALUES (80, 20);