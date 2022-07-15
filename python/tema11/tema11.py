import sqlite3

db_connection = sqlite3.connect('bd1.db')
db_cursor = db_connection.cursor()

db_cursor.execute('CREATE TABLE alumnos(Id INT, Nombre TEXT, Apellido TEXT)')

db_cursor.execute("insert into alumnos VALUES(1, 'Maria', 'Lopez')")
db_cursor.execute("insert into alumnos VALUES(2, 'Pepe', 'Rodrguez')")
db_cursor.execute("insert into alumnos VALUES(3, 'Maria', 'Martinez')")
db_cursor.execute("insert into alumnos VALUES(4, 'Francisco', 'Perez')")
db_cursor.execute("insert into alumnos VALUES(5, 'Jorge', 'Herero')")
db_cursor.execute("insert into alumnos VALUES(6, 'Clara', 'Garcia')")
db_cursor.execute("insert into alumnos VALUES(7, 'Monica', 'Santamaria')")
db_cursor.execute("insert into alumnos VALUES(8, 'Pablo', 'Villanueva')")

db_connection.commit()

db_cursor.execute("SELECT * FROM alumnos WHERE Nombre = 'Pepe'")

filas = db_cursor.fetchall()

print(filas)

db_connection.close()