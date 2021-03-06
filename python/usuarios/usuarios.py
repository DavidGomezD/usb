#Conexion y consulta a base de datos en mysql
import mysql.connector

mydb = mysql.connector.connect(
	host="mx72.hostgator.mx",
	user="gomezde1_gd",
	password="161070298",
	database="gomezde1_db_usuarios"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM usuarios")

myresult = mycursor.fetchall()

print ("\nUsuarios\n")

for x in myresult:
    print(x)
