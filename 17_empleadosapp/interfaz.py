"""
-Alta de nuevos empleados
-Filtrar empleados: opcion por departamento o rango salarial.
Si se elige departamento, se muestra combo con departamentos y al
seleccionar uno muestra empleados. 
Si selige rango salarial,
aparecen dos campos de textos (min y max) y un botón que al pulsarlo
muestra empleados
- Recibe una lista con todos los empleados y los muestra en una tabla con sus datos usando dataframe de streamlit y que se pueda actualizar. 
"""

from bson import ObjectId
import streamlit as st
import pymongo as pm

url="mongodb://localhost:27017"
serv=pm.MongoClient(url)

col_empleados= serv.empresa.empleados

tab_alta,tab_buscar,tab_mostrar_empleados=st.tabs(
    ["Insertar Empleado","Buscar","Mostrar empleados"]
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
    

with tab_buscar:
    opcion=st.radio("Filtrar por:", options=["Departamento","Rango salarial"])
    if opcion=="Departamento":
        departamentos=list(set(map(lambda e:e["departamento"],col_empleados.find())))
        departamento=st.selectbox("Departamentos:", options=departamentos)
        if st.button("Buscar",key="boton1"):
            empleados=list(col_empleados.find({"departamento":departamento}))
            if not empleados:
                st.toast("No se encontraron empleados para el departamento especificado.")
            else:
                st.table(empleados)
    else:
        min_salario=st.number_input("Salario mínimo:", min_value=0, max_value=1000000, key="min_salario")
        max_salario=st.number_input("Salario máximo:", min_value=0, max_value=1000000, key="max_salario")
        if st.button("Buscar",key="boton2"):
            empleados=list(col_empleados.find({"salario":{"$gte":min_salario,"$lte":max_salario}}))
            if not empleados:
                st.toast("No se encontraron empleados en el rango salarial especificado.")
            else:
                st.table(empleados) 
            

with tab_mostrar_empleados:
    empleados = list(col_empleados.find())
    empleados_editados = st.data_editor(empleados, disabled=["_id"], key="editor_empleados")

    if st.button("Actualizar"):
        for empleado in empleados_editados:
            col_empleados.update_one(
                {"_id": ObjectId(empleado["_id"])},
                {
                    "$set": {
                        "empleado": empleado["empleado"],
                        "salario": empleado["salario"],
                        "edad": empleado["edad"],
                        "departamento": empleado["departamento"],
                    }
                },
            )
        st.toast("Empleados actualizados correctamente.")
        
serv.close()
            
    
