import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='$~Bc4gB9',
    database= 'LaPlateforme'
)

cursor = mydb.cursor()

cursor.execute("SELECT capacite FROM salle")

results = cursor.fetchall()

capacite = 0
for i in results:
    capacite += i[0]
print(f"La capacité de toute les salles est de : {capacite}")

cursor.close()
mydb.close()