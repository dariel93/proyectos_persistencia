"""Proyecto gestión de alumnos:

-Alta de alumnos: A través de una ventana, se solicitan los datos de un
nuevo alumno y se guardan en la base de datos. No se admiten dnis duplicados
si se proporciona un dni que ya existe, el alumno no se añade
y se avisa mediante un mensaje al usuario.

-Busqueda de alumnos por curso. Se selecciona un curso en un combo
y debajo se muestra una tabla con los datos de todos los alumnos
de ese curso.

-Busqueda de alumno por dni. Se introduce el dni de un alumno
y se muestran todos sus datos, si no existe, mensaje de advertencia.

- Mostrar todos los alumnos: Se muestra una tabla con todos los alumnos de la base de datos. 
En cada fila, aparecerá un botón para borrar a ese alumno o actualizar sus datos.  
""" 

import mysql.connector as con

db=con.connect(host="localhost",user="root",password="root",port="3306",database="universidad")
cursordb=db.cursor(dictionary=True)


import streamlit as st
    
tab_alta,tab_buscar_curso,tab_buscar_dni,tab_mostrar_todos,tab_eliminar=st.tabs(
    ["Insertar Alumno","Buscar X Curso","Buscar X DNI","Mostrar Alumnos","Eliminar alumno"]
)

with tab_alta:
    dni=st.text_input("Introduce DNI:")
    name=st.text_input("Introduce nombre:")
    email=st.text_input("Introduce email:")
    course=st.text_input("Introduce curso:")
    note=st.number_input("Introduce nota:", min_value=0, max_value=10)
    if st.button("Guardar alumno"):
        cursordb.execute("select * from alumnos where dni=%s", (dni,))
        alumno=cursordb.fetchone()
        if not dni or not name or not email or not course:
            st.toast("Todos los campos son obligatorios.")
        elif alumno:
            st.toast("El alumno con ese DNI ya existe.")
        else:
            cursordb.execute(
                "insert into alumnos values(%s,%s,%s,%s,%s)", 
                (dni, name, email, course, note)
            )
            st.toast("Alumno guardado correctamente.")
        db.commit()
        
with tab_buscar_curso:
    cursordb.execute("select distinct course from alumnos")
    cursos=cursordb.fetchall()
    curso=st.selectbox("Cursos:", options=[c['course'] for c in cursos])
    if st.button("Buscar",key="boton1"):
        cursordb.execute("select * from alumnos where course=%s", (curso,))
        alumnos=cursordb.fetchall()
        if not curso:
            st.toast("Por favor, selecciona un curso.")
        elif alumnos:
            st.table(alumnos)
        else:
            st.toast("No se encontraron alumnos para el curso especificado.")

with tab_buscar_dni:
    dni=st.text_input("Introduce DNI buscado:")
    if st.button("Buscar",key="boton2"):
        cursordb.execute("select * from alumnos where dni=%s", (dni,))
        alumno=cursordb.fetchone()
        if not dni:
            st.toast("Por favor, introduce un DNI.")
        elif alumno:
            st.success(f"DNI: {alumno['dni']}, Nombre: {alumno['name']}, Email: {alumno['email']}, Curso: {alumno['course']}, Nota: {alumno['note']}")
        else:
            st.toast("Alumno no encontrado.")
            
with tab_mostrar_todos:
    cursordb.execute("SELECT * FROM alumnos")
    alumnos = cursordb.fetchall()

    if alumnos:
        col_dni, col_name, col_email, col_course, col_note, col_actualizar, col_borrar = st.columns([2, 3, 3, 2, 1, 1, 1])

        col_dni.write("**DNI**")
        col_name.write("**Nombre**")
        col_email.write("**Email**")
        col_course.write("**Curso**")
        col_note.write("**Nota**")
        col_actualizar.write("**Actualizar**")
        col_borrar.write("**Borrar**")

        for alumno in alumnos:
            dni = alumno["dni"]

            col_dni.write(dni)
            col_name.write(alumno["name"])
            col_email.write(alumno["email"])
            col_course.write(alumno["course"])
            col_note.write(str(alumno["note"]))

            if col_actualizar.button("",key=f"actualizar_{dni}",icon=":material/edit:",):
                st.session_state["alumno_en_edicion"] = dni
                st.rerun()

            if col_borrar.button("",key=f"borrar_{dni}",icon=":material/delete:",):
                cursordb.execute("DELETE FROM alumnos WHERE dni = %s",
                    (dni,)
                )
                db.commit()
                st.toast(f"Alumno con DNI {dni} eliminado correctamente.")
                st.rerun()

        dni_editando = st.session_state.get("alumno_en_edicion")

        if dni_editando:
            alumno = next(
                (a for a in alumnos if a["dni"] == dni_editando),
                None
            )

            if alumno:
                st.divider()

                with st.form(key=f"form_editar_{dni_editando}"):
                    new_name = st.text_input(
                        "Nuevo nombre:",
                        value=alumno["name"],
                        key=f"name_{dni_editando}"
                    )

                    new_email = st.text_input(
                        "Nuevo email:",
                        value=alumno["email"],
                        key=f"email_{dni_editando}"
                    )

                    new_course = st.text_input(
                        "Nuevo curso:",
                        value=alumno["course"],
                        key=f"course_{dni_editando}"
                    )

                    new_note = st.number_input(
                        "Nueva nota:",
                        value=float(alumno["note"]),
                        min_value=0.0,
                        max_value=10.0,
                        step=0.1,
                        key=f"note_{dni_editando}"
                    )

                    guardar = st.form_submit_button("Guardar cambios")

                    if guardar:
                        cursordb.execute(
                            """
                            UPDATE alumnos
                            SET name = %s,
                                email = %s,
                                course = %s,
                                note = %s
                            WHERE dni = %s
                            """,
                            (
                                new_name,
                                new_email,
                                new_course,
                                new_note,
                                dni_editando
                            )
                        )
                        db.commit()

                        st.session_state.pop("alumno_en_edicion", None)
                        st.success(
                            f"Alumno con DNI {dni_editando} actualizado correctamente."
                        )
                        st.rerun()
            

with tab_eliminar:
    dni=st.text_input("Introduce DNI a eliminar:")
    if st.button("Eliminar",key="boton3"):
        cursordb.execute("select * from alumnos where dni=%s", (dni,))
        alumno=cursordb.fetchone()
        if not dni:
            st.toast("Por favor, introduce un DNI.")
        elif alumno:
            cursordb.execute("delete from alumnos where dni=%s", (dni,))
            db.commit()
            st.toast("Alumno eliminado correctamente.")
        else:
            st.toast("Alumno no encontrado.")


cursordb.close()
db.close()