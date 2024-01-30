import mysql.connector

class Salarie:
    def __init__(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user='root',
            password='$~Bc4gB9',
            database='LaPlateforme2'
        )
        self.cursor = self.my_db.cursor()

    def get_employees(self):

        self.cursor.execute("SELECT employe.nom, employe.prenom, employe.salaire, service.nom AS service FROM employe JOIN service ON employe.id_service = service.id;")
        return self.cursor.fetchall()
    
    def update_service(self, nom, nouveau_service):
        self.cursor.execute("UPDATE employe SET id_service = (SELECT id FROM service WHERE nom = %s) WHERE nom = %s", (nouveau_service, nom))
        self.my_db.commit()

    def update_salaire(self, nom, nouveau_salaire):
        query = "UPDATE employe SET salaire = %s WHERE nom = %s"
        self.cursor.execute(query, (nouveau_salaire, nom))
        self.my_db.commit()

    def add_employee(self, nom, prenom, salaire, service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, (SELECT id FROM service WHERE nom = %s))"
        self.cursor.execute(query, (nom, prenom, salaire, service))
        self.my_db.commit()

    def delete_employee(self, nom):
        query = "DELETE FROM employe WHERE nom = %s"
        self.cursor.execute(query, (nom,))
        self.my_db.commit()

salarie = Salarie()
employees = salarie.get_employees()
for employee in employees:
    nom, prenom, salaire, service = employee
    salaire = float(salaire)
    print(f"{nom} {prenom} - {service} (Salaire : {salaire}€)")

salarie.cursor.close()
salarie.my_db.close()