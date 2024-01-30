import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='$~Bc4gB9',
    database= 'LaPlateforme'
)

cursor = mydb.cursor()

cursor.execute("SELECT superficie FROM etage")

results = cursor.fetchall()

print(results)
superficie = 0
for i in results:
    superficie += i[0]

print(f"La superficie de la plateforme est de {superficie} m²")

cursor.close()
mydb.close()