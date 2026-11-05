#Al iniciar el programa se debe mostrar el siguiente menú:
#1.- Añadir nota
#2.- Mostrar notas extremas
#3.- Total de aprobados
#4.- Nota media
#5.- Mostrar todas
#6.- Salir

#El usuario elige una opción (1 al 6) y el programa le muestra o le pide
#los datos necesarios para llevar a cabo ea acción. Despues, vuelve a salir el menú
#y así hasta que elija la opción de salir. 
#Las notas se guardan en un fichero

opcion_elegida=0
while opcion_elegida!=6 :
    print("1.- Añadir nota")
    print("2.- Mostrar notas extremas")
    print("3.- Total de aprobados")
    print("4.- Nota media")
    print("5.- Mostrar todas")
    print("6.- Salir")
    opcion_elegida=int(input("Elige opción: "))
    match opcion_elegida:
        case 1:
            f=open("notas.txt","a")
            nota=input("Introduce nota: ")
            f.write(nota+"\n")
            f.close()
        case 2:
            with open("notas.txt", "r") as f:
                notas=f.readlines()
                #notas_limpia = list(map(lambda a:int(a.strip()), notas))
                #print(f"nota más alta {max(notas_limpia)}")
                #print(f"nota más baja {min(notas_limpia)}")
                print(min(notas, key=lambda e:int(e.strip())))
                print(max(notas, key=lambda e:int(e.strip())))
        case 3:
            with open("notas.txt", "r") as f:
                aprobados=0
                nota=f.readline()
                while(nota!=""):
                    if int(nota.strip())>=5:
                        aprobados+=1
                    nota=f.readline()
                print(f"total de aprobados {aprobados}")
        case 4:
            suma=0
            with open("notas.txt", "r") as f:
                notas=f.readlines()
                notas_limpia = list(map(lambda a:int(a.strip()), notas))
                for nota in notas_limpia:
                    suma+=nota
                if(len(notas_limpia)==0):
                    print("No hay notas")
                else:
                    print(f"nota media {suma/len(notas_limpia)}")
        case 5:
            with open("notas.txt", "r") as f:
                notas=f.readlines()
                notas_limpia = list(map(lambda a:int(a.strip()), notas))
            print(notas_limpia)
            f.close()
        case 6:
            print("Fin del programa!")
        case _:
            print("opción no válida")
            
            
#Al iniciar el programa se debe mostrar el siguiente menú:
#1.- Añadir nota
#2.- Mostrar notas extremas
#3.- Total de aprobados
#4.- Nota media
#5.- Mostrar todas
#6.- Salir

#El usuario elige una opción (1 al 6) y el programa le muestra o le pide
#los datos necesarios para llevar a cabo ea acción. Despues, vuelve a salir el menú
#y así hasta que elija la opción de salir. 
#Las notas se guardan en un fichero
dir_fichero="notas.txt"
#funciones propias

try:
    f=open(dir_fichero, "r")
    f.close()
except FileNotFoundError:
    f=open(dir_fichero, "w")
    f.close()


def menu():
    print("1.- Añadir nota")
    print("2.- Mostrar notas extremas")
    print("3.- Total de aprobados")
    print("4.- Nota media")
    print("5.- Mostrar todas")
    print("6.- Salir")
def nueva_nota(nota):
    with open(dir_fichero,"a") as f:
        f.write(nota+"\n")
        
def aprobados():
    with open(dir_fichero,"r") as f:      
        aprobados=0
        linea=f.readline()
        while(linea!=""):
            if int(linea.strip())>=5:
                aprobados+=1
            linea=f.readline()
    return aprobados
def nota_baja():
    with open(dir_fichero,"r") as f:
        notas=f.readlines()
    return min(notas,key=lambda n:int(n.strip()))
def nota_alta():
    with open(dir_fichero,"r") as f:
        notas=f.readlines()
    return max(notas,key=lambda n:int(n.strip()))
def media():
    with open(dir_fichero,"r") as f:
        notas=f.readlines()
    if not notas:
        return 0
    return sum([int(n.strip()) for n in notas])/len(notas)
def mostrar_notas():
    with open(dir_fichero,"r") as f:
        linea=f.readline()
        while linea!="":
            print(linea.strip())
            linea=f.readline()
#programa principal
opcion_elegida=0
while opcion_elegida!=6 :
    menu()
    opcion_elegida=int(input("Elige opción: "))
    match opcion_elegida:
        case 1:
            nueva_nota(input("Introduce nota "))
        case 2:
            print(f"nota más alta {nota_alta()}")
            print(f"nota más baja {nota_baja()}")
        case 3:
            print(f"total de aprobados {aprobados()}")
        case 4:
            print(f"La nota media es {media()}")
        case 5:
            mostrar_notas()
        case 6:
            print("Fin del programa!")
        case _:
            print("opción no válida") 