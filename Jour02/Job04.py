import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='$~Bc4gB9',
    database= 'LaPlateforme'
)

cursor = mydb.cursor()

cursor.execute("SELECT nom, capacite FROM salle")

results = cursor.fetchall()

print(results)

cursor.close()
mydb.close()
