import mysql.connector

class Main:
    def menu(self):
        choix = int(input(""" 
                Veuillez choisir l'action à effectuer
        1. pour Ajouter un animal       4. pour Ajouter une cage        7. Pour Afficher les animaux en cage
        2. pour Retirer un animal       5. pour Modifier une cage       8. Nombre d'animaux dans le Zoo
        3. pour Modifier un animal      6. pour afficher les Animaux    9. Superficie totale des cages 
                    """))
        if choix == 1:
            gestion.add_animal()
        elif choix == 2:
            gestion.remove_animal()
        elif choix == 3:
            gestion.modify_animal()
        elif choix == 4:
            cage.add_cage()
        elif choix == 5:
            cage.modify_cage()
        elif choix == 6:
            show.afficher_animaux()
        elif choix == 7:
            show.afficher_animaux_cages()
        elif choix == 8:
            show.compter_animaux_par_cage()
        elif choix == 9:
            show.calculer_superficie_totale()
        else:
            print("Choix invalide.")

class GestionZoo(Main):
    def __init__(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user='root',
            password='$~Bc4gB9',
            database='Zoo'
        )
        self.cursor = self.my_db.cursor()

    def get_animal_nom(self):
        nom = input("Veuillez entrer le nom de l'animal : ")
        return nom
    def get_animal_race(self):
        race = input("Veuillez entrer la race de l'animal : ")
        return race
    def get_animal_cage(self):
        id_cage = input("Veuillez entrer l'identifiant de la cage : ")
        return id_cage
    def get_animal_naissance(self):
        naissance = input("Veuillez entrer la date de naissance de l'animal (YYYY-MM-DD) : ")
        return naissance
    def get_animal_origine(self):
        origine = input("Veuillez entrer le pays d'origine de l'animal : ")
        return origine
    def get_input_modification(self, nom):
        choix = int(input(f""" 
                Veuillez choisir quelle information vous souhaitez modifier pour {nom}:
                    1. Race                 4. Cage
                    2. Date de naissance    5. Nom
                    3. Pays d'origine
                    Votre choix : """))
        return choix

    def add_animal(self):
        nom, race, id_cage, naissance, origine = self.get_animal_nom(), self.get_animal_race(), self.get_animal_cage(), self.get_animal_naissance(), self.get_animal_origine()
        self.cursor.execute("INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)", (nom, race, id_cage, naissance, origine))
        self.my_db.commit()
        print("Animal ajouté avec succès.")

    def remove_animal(self):
        nom = self.get_animal_nom()
        self.cursor.execute("DELETE FROM animal WHERE nom = %s", (nom,))
        self.my_db.commit()
        print("Animal supprimé avec succès.")
        self.menu()

    def remove_animal(self):
        nom = self.get_animal_nom()
        self.cursor.execute("DELETE FROM animal WHERE nom = %s", (nom,))
        self.my_db.commit()
        print("Animal supprimé avec succès.")
    
    def modify_animal(self):
        nom = self.get_animal_nom()
        choix = self.get_input_modification(nom)
        if choix == 1:
            nouvelle_race = self.get_animal_race()
            self.cursor.execute("UPDATE animal SET race = %s WHERE nom = %s", (nouvelle_race, nom))
        elif choix == 2:
            nouvelle_date_naissance = self.get_animal_naissance()
            self.cursor.execute("UPDATE animal SET date_naissance = %s WHERE nom = %s", (nouvelle_date_naissance, nom))
        elif choix == 3:
            nouveau_pays_origine = self.get_animal_origine()
            self.cursor.execute("UPDATE animal SET pays_origine = %s WHERE nom = %s", (nouveau_pays_origine, nom))
        elif choix == 4:
            nouvelle_cage = self.get_animal_cage()
            self.cursor.execute("UPDATE animal SET id_cage = %s WHERE nom = %s", (nouvelle_cage, nom))
        elif choix == 5:
            nouvelle_cage = self.get_animal_nom()
            self.cursor.execute("UPDATE animal SET nom = %s WHERE nom = %s", (nouvelle_cage, nom))
        else:
            print("Choix invalide.")
            return
        self.my_db.commit()
        print("Informations de l'animal modifiées avec succès.")

class GestionCage(Main):
    def __init__(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user='root',
            password='$~Bc4gB9',
            database='Zoo'
        )
        self.cursor = self.my_db.cursor()

    def get_cage_superficie(self):
        superficie = float(input("Veuillez entrer la superficie de la cage : "))
        return superficie

    def get_cage_capacite_max(self):
        capacite_max = int(input("Veuillez entrer la capacité maximale de la cage : "))
        return capacite_max

    def add_cage(self):
        superficie = self.get_cage_superficie()
        capacite_max = self.get_cage_capacite_max()
        self.cursor.execute("INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)", (superficie, capacite_max))
        self.my_db.commit()
        print("Cage ajoutée avec succès.")

    def modify_cage(self):
        show.afficher_all_cages()
        id_cage = int(input("Veuillez entrer l'identifiant de la cage à modifier : "))
        choix = int(input(""" 
                Veuillez choisir quelle information vous souhaitez modifier pour la cage :
                    1. Superficie
                    2. Capacité maximale
                    Votre choix : """))

        if choix == 1:
            nouvelle_superficie = self.get_cage_superficie()
            self.cursor.execute("UPDATE cage SET superficie = %s WHERE id = %s", (nouvelle_superficie, id_cage))
        elif choix == 2:
            nouvelle_capacite_max = self.get_cage_capacite_max()
            self.cursor.execute("UPDATE cage SET capacite_max = %s WHERE id = %s", (nouvelle_capacite_max, id_cage))
        else:
            print("Choix invalide.")
            return
        self.my_db.commit()
        print("Informations de la cage modifiées avec succès.")

class Afficher:
    def __init__(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user='root',
            password='$~Bc4gB9',
            database='Zoo'
        )
        self.cursor = self.my_db.cursor()

    def get_all_cages(self):
        self.cursor.execute("SELECT * FROM cage")
        cages = self.cursor.fetchall()
        return cages

    def afficher_all_cages(self):
        cages = self.get_all_cages()
        print("Liste des cages :")
        for cage in cages:
            print(f"ID: {cage[0]}, Superficie: {cage[1]}, Capacité maximale: {cage[2]}")
    
    def afficher_animaux(self):
        print("Animaux présents dans le zoo :")
        self.cursor.execute("SELECT * FROM animal")
        animaux = self.cursor.fetchall()
        for animal in animaux:
            id, nom, race, id_cage, date_naissance, pays_origine = animal
            print(f"Id:{id} {nom} {race} né le :{date_naissance} ({pays_origine}) [Cage n° {id_cage}]")


    def afficher_animaux_cages(self):
        print("Animaux présents dans les cages :")
        self.cursor.execute("SELECT * FROM cage")
        cages = self.cursor.fetchall()
        for cage in cages:
            self.cursor.execute("SELECT * FROM animal WHERE id_cage = %s", (cage[0],))
            animaux_cage = self.cursor.fetchall()
            if animaux_cage:
                print(f"----------> Cage {cage[0]} <----------")
                for animal in animaux_cage:
                    id, nom, race, id_cage, date_naissance, pays_origine = animal
                    print(f"[Id:{id}] {nom} {race} né le :{date_naissance} ({pays_origine})")
            else:
                print(f"----------> Cage {cage[0]} est vide.")

    def compter_animaux_par_cage(self):
        compteur_animaux = {}
        self.cursor.execute("SELECT id_cage, COUNT(*) FROM animal GROUP BY id_cage")
        resultats = self.cursor.fetchall()
        for id_cage, nombre_animaux in resultats:
            compteur_animaux[id_cage] = nombre_animaux
        print("Nombre d'animaux par cage :")
        for id_cage, nombre_animaux in compteur_animaux.items():
            print(f"Cage {id_cage} : {nombre_animaux} animaux")
        self.cursor.execute("SELECT COUNT(*) FROM animal")
        total_animaux = self.cursor.fetchone()[0]
        print(f"Nombre total d'animaux dans le zoo : {total_animaux}")

    def calculer_superficie_totale(self):
        self.cursor.execute("SELECT SUM(superficie) FROM cage")
        superficie_totale = self.cursor.fetchone()[0]
        print (f"La superficie totale des cages est de: {superficie_totale}")


gestion = GestionZoo()
cage = GestionCage()
show = Afficher()
main = Main()

main.menu()