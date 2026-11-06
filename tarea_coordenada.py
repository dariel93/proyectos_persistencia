""" Se pide al usuario su posición, después el programa
le mostrará las coordenadas del punto 
más cercano a su posición """

import csv
import math

dir_fichero = "coordenadas.csv"

# 1. Pedir la posición del usuario
pos_usuario = (
    int(input("Tu posición x: ")),
    int(input("Tu posición y: "))
)

# 2. Añadir coordenadas nuevas al fichero
with open(dir_fichero, "a", newline="") as f:
    campos = ["x", "y"]
    escritor = csv.DictWriter(f, fieldnames=campos)

    while True:
        respuesta = input("¿Quieres introducir nuevas coordenadas? (s/n): ")

        if respuesta.lower() == "s":
            x = int(input("Introduce la coordenada x: "))
            y = int(input("Introduce la coordenada y: "))

            escritor.writerow({"x": x, "y": y})

        elif respuesta.lower() == "n":
            break

        else:
            print("Respuesta no válida. Escribe 's' o 'n'.")

# 3. Leer el fichero actualizado como diccionarios
with open(dir_fichero, "r") as f:
    lector = csv.DictReader(f)
    coordenadas = list(lector)

# 4. Calcular el punto más cercano
cercana = min(
    coordenadas,
    key=lambda c: math.dist(
        (int(c["x"]), int(c["y"])),
        pos_usuario
    )
)

print("El punto más cercano es:", cercana["x"], ",", cercana["y"])


# Solucion Optima

dir_fichero = "coordenadas.csv"

# 1. Pedir la posición del usuario
pos_usuario = (
    int(input("Tu posición x: ")),
    int(input("Tu posición y: "))
)

# 2. Pedir coordenadas nuevas y guardarlas en el fichero
with open(dir_fichero, "a", newline="") as f:
    escritor = csv.writer(f)

    while True:
        respuesta = input("¿Quieres introducir nuevas coordenadas? (s/n): ")

        if respuesta.lower() == "s":
            x = int(input("Introduce la coordenada x: "))
            y = int(input("Introduce la coordenada y: "))

            escritor.writerow([x, y])

        elif respuesta.lower() == "n":
            break

        else:
            print("Respuesta no válida. Escribe 's' o 'n'.")

# 3. Leer el fichero actualizado
with open(dir_fichero, "r") as f:
    next(f)  # Omite la cabecera x,y
    coordenadas = list(csv.reader(f))

# 4. Calcular el punto más cercano
cercana = min(
    coordenadas,
    key=lambda c: math.dist(
        (int(c[0]), int(c[1])),
        pos_usuario
    )
)

print("El punto más cercano es:", cercana[0], ",", cercana[1])