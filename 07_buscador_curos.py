#realizar una nueva versión del ejercicio 38_buscar_cursos
#lo más reducida posible

import datetime as dt
import streamlit as st
import json

dir_fichero="alumnos.json"

with open(dir_fichero, "r") as f:
    cursos = json.load(f)["cursos"]

# Curso que finalizó antes
menor=min(
    cursos, 
    key=lambda c:dt.datetime.strptime(c["fecha_fin"],"%d/%m/%Y")
)

#Nombre del curso con la nota media más alta
mayor = max(
    cursos, 
    key=lambda c:sum(c["calificaciones"]) / len(c["calificaciones"])
)

st.title("Análisis de cursos")

st.subheader("Curso más antiguo")
st.markdown(f"El curso más antiguo es **{menor['denominacion']}**.")
st.write(menor)

st.subheader("Curso con la media más alta")
media_mayor = sum(mayor["calificaciones"]) / len(mayor["calificaciones"])
st.markdown(
    f"El curso con la media más alta es **{mayor['denominacion']}**, "
    f"con una nota media de **{media_mayor:.2f}**."
)
st.write(mayor)