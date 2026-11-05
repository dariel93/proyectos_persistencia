import csv

"""# Con CSVreadader
with open("empleados.csv", "r") as f:
    datos = csv.reader(f, delimiter=",")
    for row in datos:
        print(row)
        
# Con DictReader
with open("empleados.csv", "r") as f:
    datos = csv.DictReader(f)
    for row in datos:
        print(row)

# Con List y reader
with open("empleados.csv", "r") as f:
    datos = list(csv.reader(f))
    print(datos)

# Con Dict y reader
with open("empleados.csv", "r") as f:
    datos = list(csv.DictReader(f))
    print(datos)"""


# Solicta la instroduccion de un departamento y te muestra 
# los nombres de las personas de ese departamento

with open("empleados.csv", "r") as f:
    datos = csv.DictReader(f)
    for row in datos:
        print(row)


# Con Dict y reader
departamento=input("Introduce un departamento: ")
with open("empleados.csv", "r") as f:
    datos = csv.DictReader(f)
    for row in datos:
        if row["departamento"] == departamento:
            print(row["empleado"])

with open("empleados.csv", "r") as f:
    datos = list(csv.DictReader(f))
    print(datos)
    
# Nombre del empleado con mayor salario

mayor = 0
with open("empleados.csv", "r") as f:
    datos = list(csv.DictReader(f))
    for row in datos["empleado"]:
        if row["salario"] > mayor:
            mayor = row["salario"]
            nombre_empleado = row["nombre"]
    print(f"El empleado {nombre_empleado} tiene el mayor salario {mayor}")


with open("empleados.csv", "r") as f:
    lista_empleados = list(csv.DictReader(f))
    empleado_max = max(lista_empleados, key=lambda e:int(e["salario"]()))
    print(f"El empleado {empleado_max["nombre"]}  gana {empleado_max["salario"]}")
    