CREATE DATABASE LaPlateforme2

CREATE TABLE employe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    salaire DECIMAL,
    id_service INT
);

INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
('Spaghetti', 'Betty', 2300, 1),
('Steak', 'Chuck', 4500, 2),
('Doe', 'John', 1800.5, 1),
('Barnes', 'Binkie', 1680, 3),
('Dupuis', 'Gertrude', 2000, 3);

SELECT * FROM employe
WHERE salaire > 3000;

CREATE TABLE service (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255)
);

INSERT INTO service (nom) VALUES
('Chef'),
('Cuisinier'),
('Serveur');

SELECT employe.nom, employe.prenom, employe.salaire, service.nom AS service
FROM employe
JOIN service ON employe.id_service = service.id;
