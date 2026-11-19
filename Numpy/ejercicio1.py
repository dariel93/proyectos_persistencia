# A partir de la coleccion de empleados de la bd empresa

# Salario medio de todos los empleados
# Edad mayor
# Lista de departamentos

import pymongo as pm
import numpy as np

url="mongodb://localhost:27017"
serv=pm.MongoClient(url)

col_empleados= serv.empresa.empleados

"""salarios=list(set(map(lambda e:e["salario"],col_empleados.find())))
edades = list(set(map(lambda e:e["edad"],col_empleados.find())))
departamentos=list(set(map(lambda e:e["departamento"],col_empleados.find())))

datos = np.array(salarios)

print(f"El salario medio de todos los espleados es: {np.average(datos)}")
print(f"La edad mayor de todos los espleados es: {np.amax(edades)}")
print(departamentos)"""

# Solucion del Profe
salarios = list(map(lambda e:e["salario"],col_empleados.find()))

salarios_unicos = np.unique(np.array(salarios))
print(salarios_unicos)

