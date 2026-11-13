"""A partir del fichero houses.csv

- Se solicita un presupuesto y te muestra los datos de los pisos que puedes comprar ordenados de mayor a menor precio
"""
import pandas as pd

presupuesto = float(input("Introduce tu presupuesto: "))
df = pd.read_csv("houses.csv", encoding="utf-8")
df_filtrado = df[df["price"] <= presupuesto]
df_ordenado = df_filtrado.sort_values(by="price", ascending=False)
print(df_ordenado)
