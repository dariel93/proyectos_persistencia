import pandas as pd

lista_reproduccion = [
    {"titulo": "Canción 1", "duracion": 3.2, "valoracion": 10},
    {"titulo": "Canción 2", "duracion": 4.5, "valoracion": 8},
    {"titulo": "Canción 3", "duracion": 2.8, "valoracion": 9}
]

# df = pd.DataFrame(lista_reproduccion)
# print(df)

df=pd.read_csv("empleados.csv", encoding="utf-8")
"""print(df)
print(df.values)
print(df.columns)"""

"""for v in df.values:
    print(v[0])"""
    
# Salario medio de los empleados
salario_medio = df["salario"].mean()
print(f"Salario medio: {salario_medio}")

# Salario medio del departamento de informatica
print(f"Salario medio del departamento de informatica: {df.query("departamento == 'informática'")["salario"].mean():.2f}")

# Quiero agruparlos por departamento y con la columna salario medio y edad maxima
agrupacion = df.groupby("departamento").agg(salario_medio=("salario", "mean"), edad_maxima=("edad", "max"))
print(agrupacion)

# Ordenasr por salario medio y la edad maxima
agrupacion_ordenada = agrupacion.sort_values(by=["salario_medio", "edad_maxima"])
print(agrupacion_ordenada)

# Incrementar el salario de todos los empleados en un 10%
df["salario"] = df["salario"].map(lambda x: x * 1.10)
print(df)