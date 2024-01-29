-- Active: 1706527955759@@127.0.0.1@3306@laplateforme
INSERT INTO etudiant (nom, prenom, age, email) VALUES
('Martin', 'Dupuis', 18, 'martin.dupuis@laplateforme.io');

SELECT *
FROM etudiant
WHERE nom = 'Dupuis';
