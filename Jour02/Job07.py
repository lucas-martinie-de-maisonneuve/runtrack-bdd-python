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

    def get_employe_nom(self):
        nom = input("                    --> Veuillez entrer le nom de l'employé : ")
        return nom
    def get_employe_prenom(self):
        prenom = input("                    --> Veuillez entrer le prénom de l'employé : ")
        return prenom
    def get_employe_salaire(self):
        salaire = float(input("                    --> Veuillez entrer le salaire de l'employé : "))
        return salaire
    def get_employe_service(self):
        service = int(input("""           
                    --> Veuillez entrer le service de l'employé : 
                    [1] Cuisinier | [2] Chef | [3] Serveur
                                Votre choix : """))
        if service == 1:
            service = 'Cuisinier'
            return service
        elif service == 2:
            service = 'Chef'
            return service
        elif service == 3:
            service = 'Serveur'
            return service

    def get_employees(self):
        self.cursor.execute("SELECT employe.nom, employe.prenom, employe.salaire, service.nom AS service FROM employe JOIN service ON employe.id_service = service.id;")
        return self.cursor.fetchall()
    
    def update_service(self, nom, nouveau_service):
        self.cursor.execute(f"UPDATE employe SET id_service = (SELECT id FROM service WHERE nom = '{nouveau_service}') WHERE nom = '{nom}'")
        self.my_db.commit()
        self.close_continue()

    def update_salaire(self, nom, nouveau_salaire):
        self.cursor.execute(f"UPDATE employe SET salaire = {nouveau_salaire} WHERE nom = '{nom}'")
        self.my_db.commit()
        self.close_continue()

    def add_employee(self):
        nom, prenom, salaire, service = self.get_employe_nom(), self.get_employe_prenom(), self.get_employe_salaire(), self.get_employe_service()
        self.cursor.execute(f"INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('{nom}', '{prenom}', {salaire}, (SELECT id FROM service WHERE nom = '{service}'))")
        self.my_db.commit()
        self.close_continue()

    def delete_employee(self, nom):
        self.cursor.execute(f"DELETE FROM employe WHERE nom = '{nom}'")
        self.my_db.commit()
        self.close_continue()

    def print_employee(self):
        employees = self.get_employees()
        for employee in employees:
            nom, prenom, salaire, service = employee
            salaire = float(salaire)
            print(f"{nom} {prenom} - {service} (Salaire : {salaire}€)")
        self.close_continue()

    def modification(self):
        choix = int(input(f""" 
                    +------------------------------------------------------------------+                          
                    |Veuillez choisir l'action à effectuer (Entrez un chiffre de 1 à 5)|
                    +------------------------------------------------------------------+                          
                    | [1] Afficher les employées     | [4] Ajouter un employé          |
                    | [2] Mettre à jour le service   | [5] Supprimer un employé        |
                    | [3] Mettre à jour le salaire   |                                 |
                    +------------------------------------------------------------------+                          
                                              Choix : """))
        if choix == 1 :
            self.print_employee()
        elif choix == 2 :
            self.update_service(self.get_employe_nom(), self.get_employe_service())
        elif choix == 3 :
            self.update_salaire(self.get_employe_nom(), self.get_employe_salaire())
        elif choix == 4 :
            self.add_employee()
        elif choix == 5 :
            self.delete_employee()

    def close_continue(self):
        continue_choix = int(input("""                    --> Voulez vous revenir au menu ? (Entrez 1 ou 2 pour quitter) <-- """))
        if continue_choix == 1:
            self.modification()
        elif continue_choix == 2:
            return
        else:
            print("                    !!  Choix invalide !!")
            self.close_continue()


employe = Employe()

employe.print_employee()
employe.cursor.close()
employe.my_db.close()