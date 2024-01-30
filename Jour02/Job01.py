import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='$~Bc4gB9',
    database= 'LaPlateforme'
)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM etudiant")

result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
mydb.close()