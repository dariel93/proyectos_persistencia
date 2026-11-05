import math
#Solicitar al usuario la introducción de unas coordenadas (x,y),
#cada pareja de coordenadas se guarda en una lista. 
#Cada vez que solicitamos coordenadas
#preguntamos si quiere introducir nuevas coordenadas. 
#En caso afirmativo, se solicitan de nuevo
#si responde que no, finaliza el programa mostrando la lista 
#de coordenadas
coordenadas=[]
def distancia(punto1,punto2):
   return math.hypot(punto1[0]-punto2[0],punto1[1]-punto2[1]) 
resp="S"
while resp=="S" or resp=="s":
    x=int(input("X de la tienda: "))
    y=int(input("Y de la tienda: "))
    coordenadas.append((x,y))
    resp=input("¿Quiere introducir nuevas coordenadas (S/N)?")
print(coordenadas)
#Se pide al usuario su posición, después el programa
#le mostrará las coordenadas del punto 
#más cercano a su posición

pos_usuario=(int(input("Tu posición x: ")),int(input("Tu posición y: ")))
#En esta variable se obtendrá la distnacia más corta
distancia_corta=distancia(coordenadas[0],pos_usuario)
#En esta variable se deberá obtener la tupla de la tienda más cercana
coordenada_tienda=coordenadas[0]
#recorremos las coordenadas y para cada una de ellas,
#obtenemos la distancia con la posición del usuario. Si encontramos que esa distancia
#es inferior distancia_corta, actualizamos tanto las variables distancia_corta
#como coordenada_tienda
for coord in coordenadas:
    dist=distancia(coord,pos_usuario)
    if dist<distancia_corta:
        distancia_corta,coordenada_tienda=dist,coord
print(f"La tienda mas cercana a {pos_usuario} tiene de coordenadas {coordenada_tienda}")