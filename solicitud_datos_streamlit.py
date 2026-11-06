import streamlit as st

name = st.text_input("Introduce tu nombre: ")
age = st.number_input("Introduce tu edad: ", value=0)
affiliate = st.checkbox("Afiliado: ")
course = st.radio("Elige curso: ", ["Python", "C++", "Java"])
center = st.selectbox("Elige centro: ",["Leganés","Getafe","Alcobendas","San Blas"])
if st.button("Pulsar"):
    st.success(f"Te llamas {name}, tienes {age} años, has elegido el curso {course} en el centro {center}") 

aula = [ 
    {"id": 1, "nombre": "Juan", "edad": 25}, 
    {"id": 2, "nombre": "Ana", "edad": 30}, 
    {"id": 3, "nombre": "Pedro", "edad": 22} 
] 
st.table(aula)