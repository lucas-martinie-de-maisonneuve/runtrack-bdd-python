import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='$~Bc4gB9',
    database= 'LaPlateforme'
)

cursor = mydb.cursor()

cursor.execute("SELECT SUM(superficie) FROM etage")

results = cursor.fetchone()

print(f"La superficie de la plateforme est de {results[0]} m²")

cursor.close()
mydb.close()