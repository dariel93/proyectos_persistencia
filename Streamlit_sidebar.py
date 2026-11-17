"""

Al seleccionar una tienda se mostrara:
Una tabla con la información de dicha tienda. Y debajo de esa tabla:
-total de facturación
-total de gastos de personal
-mes con mayor facturación

*Al seleccionar un mes se mostrará:
Una tabla con los datos de ese mes. Y debajo de esa tabla:
-Media de facturación de todas las tiendas
-Tienda con mayor gasto de personal

"""

# Usaremos Streamlit para crear la interfaz de usuario y sidebar para la selección de tiendas y meses. Usaremos polars para mostrar los datos de manera visual y clara.
# Mostraremos graficos de barras, pastel y lineas para mostrar la información de manera visual y clara usando matplotlib y streamlit.

import streamlit as st
import polars as pl
import matplotlib.pyplot as plt

# df = pl.scan_csv("tiendas.csv")

"""with st.sidebar:
    tienda = st.selectbox("Selecciona una tienda", df.select(pl.col("nombre_tienda")).unique().collect()["nombre_tienda"].to_list())
    mes = st.selectbox("Selecciona un mes", df.select(pl.col("mes")).unique().collect()["mes"].to_list())
    
if tienda!=None:
    df_tienda = df.filter(pl.col("nombre_tienda") == tienda).collect()
    st.write(f"Información de la tienda: {tienda}")
    st.dataframe(df_tienda)
    
    total_facturacion = df_tienda.select(pl.col("facturacion")).sum()[0, 0]
    total_gastos_personal = df_tienda.select(pl.col("gastos_personal")).sum()[0, 0]
    mes_mayor_facturacion = df_tienda.sort("facturacion", descending=True).row(0)[1]
    
    st.write(f"Total de facturación: {total_facturacion} €")
    st.write(f"Total de gastos de personal: {total_gastos_personal} €")
    st.write(f"Mes con mayor facturación: {mes_mayor_facturacion}")

if mes!=None:
    df_mes = df.filter(pl.col("mes") == mes).collect()
    st.write(f"Información del mes: {mes}")
    st.dataframe(df_mes)
    
    media_facturacion = df_mes.select(pl.col("facturacion")).mean()[0, 0]
    tienda_mayor_gasto = df_mes.group_by("nombre_tienda").agg(pl.col("gastos_personal").sum()).sort("gastos_personal", descending=True).row(0)[0]
    
    st.write(f"Media de facturación de todas las tiendas: {media_facturacion} €")
    st.write(f"Tienda con mayor gasto de personal: {tienda_mayor_gasto}")"""
    
    
df = pl.read_csv("tiendas.csv")

with st.sidebar:
    st.subheader("Filtrado de datos")
    tienda_sel=st.selectbox("Seleccione tienda",df["nombre_tienda"].unique().to_list(),index=None,key=1)
    mes_sel=st.selectbox("Seleccione mes",df["mes"].unique().to_list(),index=None,key=2)
    
if tienda_sel!=None:
    df_tienda = df.filter(pl.col("nombre_tienda") == tienda).to_dicts()
    st.write(f"Información de la tienda: {df_tienda}")
    st.dataframe(df_tienda)
    
    total_facturacion = df_tienda.select(pl.col("facturacion")).sum()[0, 0]
    total_gastos_personal = df_tienda.select(pl.col("gastos_personal")).sum()[0, 0]
    mes_mayor_facturacion = df_tienda.sort("facturacion", descending=True).row(0)[1]
    
    st.write(f"Total de facturación: {total_facturacion} €")
    st.write(f"Total de gastos de personal: {total_gastos_personal} €")
    st.write(f"Mes con mayor facturación: {mes_mayor_facturacion}")

if mes_sel!=None:
    df_mes = df.filter(pl.col("mes") == mes).collect()
    st.write(f"Información del mes: {mes}")
    st.dataframe(df_mes)
    
    media_facturacion = df_mes.select(pl.col("facturacion")).mean()[0, 0]
    tienda_mayor_gasto = df_mes.group_by("nombre_tienda").agg(pl.col("gastos_personal").sum()).sort("gastos_personal", descending=True).row(0)[0]
    
    st.write(f"Media de facturación de todas las tiendas: {media_facturacion} €")
    st.write(f"Tienda con mayor gasto de personal: {tienda_mayor_gasto}")