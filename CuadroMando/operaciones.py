import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


alumnos = pd.read_csv("alumnos.csv")
notas = pd.read_csv("notas.csv")

df = notas.merge(
    alumnos,
    on="id_alumno",
    how="left"
)


# Agrupacion por asignatura , alumnos evaluados, nota media, nota maxima, porcentaje de aprobados
resumen = df.groupby("asignatura").agg(
    alumnos_evaluados=("id_alumno", "nunique"), 
    nota_media=("nota", "mean"), 
    nota_maxima=("nota", "max"),
    nota_minima=("nota", "min"),
    aprobados=("id_alumno", lambda x: df.loc[x.index].query("nota >= 5")["id_alumno"].nunique())
)
print(resumen)






















































































"""with st.sidebar:
    st.subheader("Filtros")
    curso_sel=st.selectbox("Curso",options=["Todos"] + df.get_column("curso").unique().to_list())
    asigantura_sel=st.selectbox("Asignatura", options=["Todas"] + df.get_column("asignatura").unique().to_list())
    grupo_sel=st.selectbox("Grupo", options=["Todas"] + df.get_column("grupo").unique().to_list())
    evaluacion_sel=st.selectbox("Evaluación", options=["Todas"] + df.get_column("evaluacion").unique().to_list())"""
    

    
    
        
    
    


