import polars as pl

"""
¿Por que Polars
    1- Estilo y metodos mas modernos
    2 - Mas eficiente
    
"""

datos = [ 
    {"nombre": "Ana", "edad": 25, "salario": 25000,"departamento":"ventas"}, 
    {"nombre": "Luis", "edad": 32, "salario": 32000,"departamento":"informática"}, 
    {"nombre": "Marta", "edad": 28, "salario": 28000,"departamento":"informática"}, 
    {"nombre": "Pedro", "edad": 41, "salario": 41000,"departamento":"ventas"} 
] 

df = pl.DataFrame(datos) 
print(df)

# Acceso a filas y columnas
print(df["edad"].to_list()) # Columna en lista de valores
print(df.row(0, named=True)) # Diccionario en los datos de la fila
print(df.to_dicts()) # Convierte todo el DF en un diccionario

# filtrado
print(df.filter(pl.col("salario")>30000))
print(df.filter( (pl.col("salario")>30000) & (pl.col("edad")<50) ))

# Ordenacion
print(df.sort(by="edad", descending=False))
print(
    df.sort(by="salario", descending=True) #Ordena descendente en salario
    .row(0)[0] # Se queda con la priemra fila, y de esta con el primer elemneto
) 

# Funciones para calculos min(), max(), mean(), count(), unique()

print("salario mas alto", df["salario"].max())
print("Edad mas baja", df["edad"].min())

# Seleccion 
resultado=df.select(pl.col("salario").mean().alias("Salario Medio"), pl.col("edad").mean().alias("Edad Media"))
print(resultado)

# Muestra lista de departamentos sin duplicados
print(df["departamento"].unique().to_list())

# Agrupaciones
df.group_by("departamento").agg(pl.col("salario").mean().alias("Salario Medio"), pl.col("nombre").count().alias("Total Empleados"))
print(df)

# Recorrido de un Data Frame
for e in df.iter_rows():
    print(e)
    
# Cargar un archivo
df = pl.scan_csv("houses.csv")
filtro = df.filter(pl.col("rooms")>2)
print(filtro.collect())

