USE LaPlateforme;

CREATE TABLE etudiant (
id INT AUTO_INCREMENT PRIMARY KEY,
nom VARCHAR(255) NOT NULL,
prenom VARCHAR(25) NOT NULL,
age INT NOT NULL,
email VARCHAR(255) NOT NULL
);

SHOW TABLES;