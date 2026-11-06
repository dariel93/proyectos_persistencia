"""
Realiza un progrma para la organizacion de una libreria
un libro tiene tres propiedades: titulo, autor y precio.

Cuando se inicie el programa, se va a mostrar un menu:
1-Nuevo libro
2-Mostrar todos
3-Buscar por titulo
4-Libros por precio maximo
5-Salir

1-Se piden los datos del nuevo libro y se guardan
2-Se muestran los titulos de todos los libros
3-Se le pide el titulo y se muestran todos sus datos
4-Se le pide el precio maximo y se muestran los titulos de los libros cuyo precio sea igual o inferior al introducido
Despues de ejecutar cualquiera de las anteriores opciones, se muestra de nuevo el menu.
Asi hasta que elija la opcion 5 que sale del programa
"""

import streamlit as st

libros=[]
tab_nuevo,tab_todos,tab_buscar,tab_precios=st.tabs(["Nuevo libro","Mostrar todos","Buscar por título","Libros por precio máximo"])

with tab_nuevo:
    titulo=st.text_input("Introduce título:")
    autor=st.text_input("Introduce autor:")
    precio=st.number_input("Introduce precio:")
    if st.button("Guardar libro"):
        libros.append({"titulo": titulo, "autor": autor, "precio": precio})

with tab_buscar:
    titulo=st.text_input("Introduce el título del libro a buscar: ")
    if st.button("Buscar"):
        libs=list(filter(lambda lib:lib["titulo"].lower()==titulo.lower(),libros))
        if libs:
            st.success(f"Titulo: {libs[0]["titulo"]}, Autor: {libs[0]["autor"]}, Precio: {libs[0]["precio"]}")
        else:
            st.error("Libro no encontrado")

with tab_todos:
    st.title("Listado de libros")
    st.table(libros)