import mysql.connector as con

db=con.connect(
    host="localhost",
    user="root",
    password="root",
    port="3306",
    database="universidad"
)
cursordb=db.cursor(dictionary=True)
cursordb.execute("select * from alumnos")
for row in cursordb:
    print(row)
db.close()
