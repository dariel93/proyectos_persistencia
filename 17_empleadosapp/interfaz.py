"""
-Alta de nuevos empleados
-Filtrar empleados: opcion por departamento o rango salarial.
Si se elige departamento, se muestra combo con departamentos y al
seleccionar uno muestra empleados. 
Si selige rango salarial,
aparecen dos campos de textos (min y max) y un botón que al pulsarlo
muestra empleados 
"""

import streamlit as st
import pymongo as pm
url="mongodb://localhost:27017"
serv=pm.MongoClient(url)

col_empleados= serv.empresa.empleados

tab_alta,tab_buscar_departamento,tab_buscar_rango_salarial=st.tabs(
    ["Insertar Empleado","Buscar X Departamento","Buscar X Rango Salarial"]
)

with tab_alta:
    empleado=st.text_input("Introduce nombre:")
    edad=st.number_input("Introduce edad:", min_value=0, max_value=120)
    salario=st.number_input("Introduce salario:", min_value=0, max_value=1000000)
    departamento=st.text_input("Introduce departamento:")
    if st.button("Guardar empleado"):
        if not empleado or not departamento:
            st.toast("Todos los campos son obligatorios.")
        else:
            col_empleados.insert_one({
                'empleado': empleado,
                'edad': edad,
                'salario': salario,
                'departamento': departamento
            })
            serv.close()
            st.toast("Empleado guardado correctamente.")
    

with tab_buscar_departamento:
    departamentos=list(set(map(lambda e:e["departamento"],col_empleados.find())))
    departamento=st.selectbox("Departamentos:", options=departamentos)
    if st.button("Buscar",key="boton1"):
        empleados = list(col_empleados.find({"departamento":departamento}))
        if not departamento:
            st.toast("Por favor, selecciona un departamento.")
        elif empleados:
            col_name, col_edad, col_salario, col_departamento = st.columns([2, 3, 3, 2])
            col_name.write("**Nombre**")
            col_edad.write("**Edad**")
            col_salario.write("**Salario**")
            col_departamento.write("**Departamento**")
    
            for empleado in empleados:
                col_name.write(empleado["empleado"])
                col_edad.write(str(empleado["edad"]))
                col_salario.write(str(empleado["salario"]))
                col_departamento.write(empleado["departamento"])
        else:
            st.toast("No se encontraron empleados para el departamento especificado.")