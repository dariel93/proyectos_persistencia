import streamlit as st,json

def continentes():
    with open("countries.json","r") as f:
        return list(set(map(lambda p:p["region"],json.load(f))))

def paises_continente(continente):
    with open("countries.json","r") as f:
        return list(filter(lambda p:p["region"]==continente,json.load(f)))

continente= st.selectbox("**Seleccione continente:**",continentes())

if continente:
    paises=paises_continente(continente)
    
    col_pais,col_continente,col_poblacion,col_bandera=st.columns(4)
    
    col_pais.write("**Pais**")
    col_continente.write("**Continente**")
    col_poblacion.write("**Población**")
    col_bandera.write("**Bandera**")
    
    for pais in paises:
        col_pais,col_continente,col_poblacion,col_bandera=st.columns(4)
        col_pais.write(pais["name"])
        col_continente.write(pais["region"])
        col_poblacion.write(pais["population"])
        col_bandera.image(pais["flags"]["png"],width=50) 