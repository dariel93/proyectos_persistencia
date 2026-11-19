import pandas as pd

df=pd.read_csv("empleados.csv", encoding="utf-8")

# Salario medio de los empleados
salario_medio = df["salario"].mean()
print(salario_medio)

# Salario medio del departamento de informatica
salario_medio_informatica = df.query("departamento == 'Informática'")["salario"].mean()
print(salario_medio_informatica)

# Quiero agruparlos por departamento y con la columna salario medio y edad maxima
agrupacion = df.groupby("departamento").agg(salario_medio=("salario", "mean"), edad_maxima=("edad", "max")).sort_values(by=["salario_medio", "edad_maxima"])
print(agrupacion)

# Rendimiento academico

