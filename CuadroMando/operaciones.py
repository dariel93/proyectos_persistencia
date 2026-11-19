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

# Curso: todos o cada uno de los cursos existentes.
cursos = df["curso"].unique().tolist()
print(cursos)
# Asignatura: todas o una asignatura concreta.
asignaturas = df["asignatura"].unique().tolist()
print(asignaturas)
# Evaluación: todas, primera o segunda
evaluaciones = df["evaluacion"].unique().tolist()
print(evaluaciones)
grupos = df["grupo"].unique().tolist()
print(grupos)

# Alumnnos evaluados por curso
group_curso = df.groupby("curso").agg(
    alumnos_evaluados=("id_alumno", "nunique")
)
print(group_curso)

# Nota media de todas las calificaciones
nota_media = df["nota"].mean()
print(nota_media)

# Rendimiento por alumno(id_aluno, nombre,, curso. grupo, noata media. asgnatiras evaluadas, asignturas probandas)
datos_alumno = ["id_alumno", "nombre", "curso", "grupo"]

# Media de cada asignatura por alumno
medias_asignaturas = df.groupby(datos_alumno + ["asignatura"]).agg(nota_asignatura=("nota", "mean"))


# Resumen de rendimiento por alumno
rendimiento = medias_asignaturas.groupby(datos_alumno).agg(
        nota_media=("nota_asignatura", "mean"),
        asignaturas_evaluadas=("nota_asignatura", "count"),
        asignaturas_aprobadas=(
            "nota_asignatura",
            lambda notas: (notas >= 5).sum()
        )
).round({"nota_media": 2})


print(rendimiento)

























































































"""with st.sidebar:
    st.subheader("Filtros")
    curso_sel=st.selectbox("Curso",options=["Todos"] + df.get_column("curso").unique().to_list())
    asigantura_sel=st.selectbox("Asignatura", options=["Todas"] + df.get_column("asignatura").unique().to_list())
    grupo_sel=st.selectbox("Grupo", options=["Todas"] + df.get_column("grupo").unique().to_list())
    evaluacion_sel=st.selectbox("Evaluación", options=["Todas"] + df.get_column("evaluacion").unique().to_list())"""
    

    
    
        
    
    


