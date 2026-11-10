"""Proyecto gestión de alumnos:

-Alta de alumnos: A través de una ventana, se solicitan los datos de un
nuevo alumno y se guardan en la base de datos. No se admiten dnis duplicados
si se proporciona un dni que ya existe, el alumno no se añade
y se avisa mediante un mensaje al usuario

-Busqueda de alumnos por curso. Se selecciona un curso en un combo
y debajo se muestra una tabla con los datos de todos los alumnos
de ese curso. En cada fila, aparecerá un botón para borrar a ese alumno

-Busqueda de alumno por dni. Se introduce el dni de un alumno
y se muestran todos sus datos, si no existe, mensaje de advertencia.""" 

import mysql.connector as con

db=con.connect(
    host="localhost",
    user="root",
    password="root",
    port="3306",
    database="universidad"
)
cursordb=db.cursor(dictionary=True)

# Insertar una Fila
alumno = cursordb.execute(
    "insert into alumnos values(%s,%s,%s,%s,%s)", 
    ("77777k","alumno py", "alumnopy@gmail.com", "python", 9)
)

alumnos = cursordb.execute("select * from alumnos")

for row in alumnos:
    if row["dni"] == alumno["dni"]:
        print("El alumno ya existe")
    
    
db.commit()
db.close()
