"""Sobre el archivo de ventas, realizar usando la libreria Polars:
-A partir de nombre de tienda, mostrar sus ventas totales

-Mostrar la tienda con mayor gasto de personal (Nombre de tienda y cantidad)

-A partir del nombre de tienda, mes en la que esta obtuvo mayor facturación 

- Nombre de la Tienda mas antigua
"""

import polars as pl

"""df =pl.read_csv("tiendas.csv")

tienda = input("Introduce el nombre de la tienda: ")
df_tienda = df.filter(pl.col("nombre_tienda") == tienda)
print(f"Ventas totales de {tienda}: {df_tienda.select(pl.col('facturacion')).sum()}")"""

df =pl.scan_csv("tiendas.csv")

tienda = input("Introduce el nombre de la tienda: ")
df_tienda = df.filter(pl.col("nombre_tienda") == tienda).collect()["facturacion"].sum()
print(f"Facturación total de {tienda}: {df_tienda}")

# Mostrar el mayor gasto de personal de tiendas
df_gasto_personal = df.group_by("nombre_tienda").agg(pl.col("gastos_personal").sum()).sort("gastos_personal", descending=True).limit(1).collect()
print(f"Mayor gasto de personal de tiendas: {df_gasto_personal['nombre_tienda'][0]} con un gasto de {df_gasto_personal['gastos_personal'][0]}")

# A partir del nombre de tienda, mes en la que esta obtuvo mayor facturación
df_mes_facturacion = df.filter(pl.col("nombre_tienda") == tienda).sort("facturacion", descending=True).limit(1).collect()
print(f"Mes con mayor facturación para {tienda}: {df_mes_facturacion['mes'][0]} con una facturación de {df_mes_facturacion['facturacion'][0]}")





# Solucion del Profe

#df = pl.read_csv("ventas_tiendas.csv")
df = pl.scan_csv("ventas_tiendas.csv")
tienda=input("Nombre de la tienda: ")
total = df.filter(pl.col("nombre_tienda") == tienda).collect()["facturacion"].sum()
print(f"Facturación total: {total} €")

#########################################
df = pl.read_csv("ventas_tiendas.csv")
fila_max_gasto = (df.group_by("nombre_tienda")
                .agg(pl.col("gastos_personal").sum())
                .sort("gastos_personal", descending=True)
                .row(0, named=True)
)
print(
    f"Tienda con mayor gasto de personal: {fila_max_gasto['nombre_tienda']}"
    f" ({fila_max_gasto['gastos_personal']})"
) 

##########################################################

mes_buscado=df.filter(pl.col("nombre_tienda")==tienda).sort("facturacion",descending=True).row(0)[1]
print(f"Mes con mayor facturación de{tienda} es {mes_buscado}")

#############################con scan########################
df = pl.scan_csv("ventas_tiendas.csv")

fila_max_gasto = (df.group_by("nombre_tienda")
                .agg(pl.col("gastos_personal").sum())
                .sort("gastos_personal", descending=True)
                .collect()
                .row(0, named=True)
)
print(
    f"Tienda con mayor gasto de personal: {fila_max_gasto['nombre_tienda']}"
    f" ({fila_max_gasto['gastos_personal']})"
) 

mes_buscado=df.filter(pl.col("nombre_tienda")==tienda).sort("facturacion",descending=True).collect().row(0)[1]
print(f"Mes con mayor facturación de{tienda} es {mes_buscado}")