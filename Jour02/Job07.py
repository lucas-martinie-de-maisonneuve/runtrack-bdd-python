import mysql.connector

class Employe:
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
        self.cursor.execute(f"UPDATE employe SET id_service = {nouveau_service} WHERE nom = {nom}")
        self.my_db.commit()

    def update_salaire(self, nom, nouveau_salaire):
        self.cursor.execute(f"UPDATE employe SET salaire = {nouveau_salaire} WHERE nom = {nom}")
        self.my_db.commit()

    def add_employee(self, nom, prenom, salaire, service):
        self.cursor.execute(f"INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ({nom}, {prenom}, {salaire}, (SELECT id FROM service WHERE nom = {service}))")
        self.my_db.commit()

    def delete_employee(self, nom):
        self.cursor.execute(f"DELETE FROM employe WHERE nom = {nom}")
        self.my_db.commit()

    def print_employee(self):
        employees = self.get_employees()
        for employee in employees:
            nom, prenom, salaire, service = employee
            salaire = float(salaire)
            print(f"{nom} {prenom} - {service} (Salaire : {salaire}€)")

employe = Employe()

employe.print_employee()
employe.cursor.close()
employe.my_db.close()