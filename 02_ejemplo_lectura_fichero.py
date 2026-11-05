"""f=open("dias.txt", "r")
linea=f.readline()
while linea!="":
    print(linea)
    linea=f.readline()
f.close()"""

with open("dias.txt", "r") as f:
    linea = f.readline()
    while linea!="":
        print(linea)
        linea=f.readline()
    print(f.readlines())
    
with open("dias.txt", "r") as f:
    lista_dias=f.readlines()
print(lista_dias)

    
lista_limpia = list(map(lambda a:a.strip(), lista_dias))
print(lista_limpia)

lista_limpia=[a.strip() for a in lista_dias]
print(lista_limpia)