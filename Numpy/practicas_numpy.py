import numpy as np

datos = np.array([10,11,8,20]) # Array de una dimension
datos2 = np.array([[4,8,-1], [5,3,11]]) # Array de dos dimensiones

print(datos[0]) #10
print(datos2[1][1]) #3

for fila in datos2:
    for celda in fila:
        print(celda)

a1 = np.array([200,120,30])
a2 = np.array([130,50,85])

suma = np.add(a1,a2) # [330 170 115]
print(suma)

print(np.average(suma)) # Media 205

edades = np.array([23,34,18,22,67,45,31])
print(f"Edad mayor: {np.amax(edades)}") # 67
print(f"Posicion del mayor: {np.argmax(edades)}") # 4
print(f"Edad mayor: {np.argmin(edades)}") # 2


