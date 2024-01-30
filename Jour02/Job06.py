import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='$~Bc4gB9',
    database= 'LaPlateforme'
)

cursor = mydb.cursor()

cursor.execute("SELECT SUM(capacite) FROM salle")

results = cursor.fetchone()

print("La capacité de toute les salles est de :", results[0])

cursor.close()
mydb.close()