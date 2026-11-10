import mysql.connector as con
import json
from pathlib import Path


ruta = Path(__file__).parent.parent / "countries.json"

with open(ruta, "r", encoding="utf-8") as f:
    paises_json = json.load(f)

continentes = list(set(pais["region"] for pais in paises_json))

db = con.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="mundo"
)

cursor = db.cursor()

# Insertar continentes sin id manual
cursor.executemany(
    "INSERT IGNORE INTO continentes (continente) VALUES (%s)",
    [(continente,) for continente in continentes]
)
db.commit()

# Leer los continentes ya insertados
cursor.execute("SELECT idContinente, continente FROM continentes")
continentes_bd = dict(cursor.fetchall())

print(continentes_bd)

# Preparar países
datos_paises = []

for pais in paises_json:
    nombre = pais["name"]
    poblacion = pais["population"]
    bandera = pais["flags"]["svg"]
    continente = pais["region"]
    id_continente = continentes_bd[continente]

    datos_paises.append((
        nombre,
        poblacion,
        bandera,
        id_continente
    ))

# Insertar países
cursor.executemany(
    """
    INSERT INTO paises
    (pais, poblacion, bandera, idContinente)
    VALUES (%s, %s, %s, %s)
    """,
    datos_paises
)

db.commit()

cursor.close()
db.close()

print("Países insertados correctamente.")